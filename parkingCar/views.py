import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from parkingCar.models import  History, Places
from parkingCar.serializers import  HistorySerializer, PlacesSerializer

from django.core.files.storage import default_storage

from django.core.exceptions import ObjectDoesNotExist

from django.conf import settings

# Create your views here.




#---------------------------- // -- end point app , Parking Car -- // ----------------------------

@csrf_exempt
def saveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)













#--------------------- Project Parking Car ---------------------


@csrf_exempt
def placesApi(request, id=0):
    try:
        if request.method == 'GET':
            if id == 0:
                # Récupérer tous les éléments
                places = Places.objects.all().order_by('-Time') 
                places_serializer = PlacesSerializer(places, many=True)
                return JsonResponse(places_serializer.data, safe=False)
            else:
                try:
                    # Récupérer un élément spécifique par son ID
                    place = Places.objects.get(PlaceNumero=id)
                    place_serializer = PlacesSerializer(place)
                    return JsonResponse(place_serializer.data, safe=False)
                except ObjectDoesNotExist:
                    return JsonResponse("La place demander n'existe pas ", safe=False)
                
        elif request.method == 'POST':
            place_data = JSONParser().parse(request)
            
            # Vérifier si 'PlaceNumero' est présent et non vide
            if 'PlaceNumero' not in place_data or not place_data['PlaceNumero']:
                return JsonResponse("Désolé, le numéro de place est obligatoire pour ajouter une nouvelle place", safe=False)
            
            # Vérifier si 'PlaceNumero' existe déjà dans la base de données
            if Places.objects.filter(PlaceNumero=place_data['PlaceNumero']).exists():
                return JsonResponse("Impossible d'ajouter un même numéro de place deux fois", safe=False)
                
            # Vérifier si DateEdit est présent, sinon définir la date du jour
            if 'DateCreatePlace' not in place_data:
                place_data['DateCreatePlace'] = datetime.date.today()
                
            if 'DateEdit' not in place_data:
                place_data['DateEdit'] = datetime.date.today()
                
            print ("Debug: ", place_data)
            places_serializer = PlacesSerializer(data=place_data)
            if places_serializer.is_valid():
                places_serializer.save()
                return JsonResponse("Ajouté avec succès", safe=False)
            return JsonResponse("Échec de l'ajout", safe=False)
        elif request.method == 'PUT':
            place_data = JSONParser().parse(request)
            
            if 'DateCreatePlace' not in place_data:
                place_data['DateCreatePlace'] = datetime.date.today()
            # Vérifier si DateEdit est présent, sinon définir la date du jour
            if 'DateEdit' not in place_data :
                place_data['DateEdit'] = datetime.date.today()
                
            place = Places.objects.get(PlaceId=place_data['PlaceId'])
            places_serializer = PlacesSerializer(place, data=place_data)
            if places_serializer.is_valid():
                places_serializer.save()
                return JsonResponse("Mis à jour avec succès", safe=False)
            return JsonResponse("Échec de la mise à jour", safe=False)
        elif request.method == 'DELETE':
            place = Places.objects.get(PlaceNumero=id)
            place.delete()
            return JsonResponse("Supprimé avec succès", safe=False)
    except ObjectDoesNotExist:
        return JsonResponse("L'objet n'existe pas", safe=False)
    except Exception as e:
        return JsonResponse(f"Erreur: {str(e)}", safe=False)






@csrf_exempt
def reservePlace(request):
    if request.method == 'PUT':
        try:
            place_data = JSONParser().parse(request)
            
            if 'MatriculeCar' not in place_data or not place_data['MatriculeCar']:
                return JsonResponse("Veuillez entrer le Matricule de votre Vehicule est obligatoire", safe=False)
            
            place = Places.objects.get(PlaceNumero=place_data['PlaceNumero'])
            
            
            place.MatriculeCar = place_data['MatriculeCar']
            place.Reserver = True
            place.DateEdit = datetime.date.today()
            # --  pour generer un code Qr de la place , concatener le numero de la place et le matricule de la voiture avec le timestamp
            
            # Générer un code QR unique pour la place
            qr_code_gen = f"{place.PlaceNumero}_{place.MatriculeCar}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
            print("Debug (code QR non Crypter): ", qr_code_gen)
            
            # Chiffrer le code QR
            encrypted_qr_code = settings.CIPHER_SUITE.encrypt(qr_code_gen.encode()).decode()
            place.PlaceCodeQr = encrypted_qr_code
            print("Debug (Encrypted): ", place.PlaceCodeQr)
            
            history = History()
            history.NumeroPlace = place.PlaceNumero
            history.PlaceCodeQr = place.PlaceCodeQr
            history.MatriculeCar = place.MatriculeCar
            history.DateCreate = datetime.date.today()
            history.TypeMouvement = "Reserver"
            
            place.save()
            history.save()
            
            return JsonResponse("Place réservée avec succès", safe=False)
        except ObjectDoesNotExist:
            return JsonResponse("L'objet n'existe pas", safe=False)
        except Exception as e:
            return JsonResponse(f"Erreur: {str(e)}", safe=False)
    else:
        return JsonResponse("Méthode non autorisée", safe=False)




@csrf_exempt
def libererPlace(request):
    if request.method == 'PUT':
        try:
            
            place_data = JSONParser().parse(request)
            
            place = Places.objects.get(PlaceNumero=place_data['PlaceNumero'])
            
            history = History()
            history.NumeroPlace = place.PlaceNumero
            history.PlaceCodeQr = place.PlaceCodeQr
            history.MatriculeCar = place.MatriculeCar
            history.DateCreate = datetime.date.today()
            history.TypeMouvement = "Liberer"
            
            
            place.Reserver = False
            place.MatriculeCar = Places._meta.get_field('MatriculeCar').default
            place.DateEdit = datetime.date.today()
            place.PlaceCodeQr = Places._meta.get_field('PlaceCodeQr').default
            
            
            place.save()
            history.save()
            return JsonResponse("Place libérée avec succès", safe=False)
        except ObjectDoesNotExist:
            return JsonResponse("L'objet n'existe pas", safe=False)
        except Exception as e:
            return JsonResponse(f"Erreur: {str(e)}", safe=False)
    else:
        return JsonResponse("Méthode non autorisée", safe=False)
    
    
    
    
@csrf_exempt
def libererPlaceQrCode(request):
    if request.method == 'PUT':
        try:
            
            place_data = JSONParser().parse(request)
            
            place = Places.objects.get(PlaceCodeQr=place_data['PlaceCodeQr'])
            
            history = History()
            history.NumeroPlace = place.PlaceNumero
            history.PlaceCodeQr = place.PlaceCodeQr
            history.MatriculeCar = place.MatriculeCar
            history.DateCreate = datetime.date.today()
            history.TypeMouvement = "Liberer"
            
            
            place.Reserver = False
            place.MatriculeCar = Places._meta.get_field('MatriculeCar').default
            place.DateEdit = datetime.date.today()
            place.PlaceCodeQr = Places._meta.get_field('PlaceCodeQr').default
            
            
            place.save()
            history.save()
            return JsonResponse("Place libérée avec succès", safe=False)
        except ObjectDoesNotExist:
            return JsonResponse("L'objet n'existe pas", safe=False)
        except Exception as e:
            return JsonResponse(f"Erreur: {str(e)}", safe=False)
    else:
        return JsonResponse("Méthode non autorisée", safe=False)
    
    
    
    

@csrf_exempt
def historyApi(request, id=0):
    try:
        if request.method == 'GET':
            history = History.objects.all().order_by('-Time') 
            history_serializer = HistorySerializer(history, many=True)
            return JsonResponse(history_serializer.data, safe=False)
        elif request.method == 'POST':
            history_data = JSONParser().parse(request)
            history_serializer = HistorySerializer(data=history_data)
            if history_serializer.is_valid():
                history_serializer.save()
                return JsonResponse("Ajouté avec succès", safe=False)
            return JsonResponse("Échec de l'ajout", safe=False)
        elif request.method == 'PUT':
            history_data = JSONParser().parse(request)
            history = History.objects.get(Id=history_data['Id'])
            history_serializer = HistorySerializer(history, data=history_data)
            if history_serializer.is_valid():
                history_serializer.save()
                return JsonResponse("Mis à jour avec succès", safe=False)
            return JsonResponse("Échec de la mise à jour", safe=False)
        elif request.method == 'DELETE':
            history = History.objects.get(Id=id)
            history.delete()
            return JsonResponse("Supprimé avec succès", safe=False)
    except ObjectDoesNotExist:
        return JsonResponse("L'objet n'existe pas", safe=False)
    except Exception as e:
        return JsonResponse(f"Erreur: {str(e)}", safe=False)
    
    
    
    
    
    
    
# Fonction pour décrypter le code QR
def decrypt_qr_code(encrypted_qr_code):
    try:
        decrypted_qr_code = settings.CIPHER_SUITE.decrypt(encrypted_qr_code.encode()).decode()
        return decrypted_qr_code
    except Exception as e:
        print("Erreur de déchiffrement: ", str(e))
        return None