from rest_framework import serializers

from parkingCar.models import Places, History



        
        
        
        



#--------------------- Project Parking Car ---------------------

class PlacesSerializer(serializers.ModelSerializer):
    DateCreatePlace = serializers.DateField(format="%Y-%m-%d")
    DateEdit = serializers.DateField(format="%Y-%m-%d")
    
    class Meta:
        model = Places
        '''fields = ('PlaceId',
                  'PlaceNumero',
                  'PlaceCodeQr',
                  'DateCreatePlace',
                  'DateEdit',
                  'Reserver',
                  'MatriculeCar') '''
        
        fields = '__all__'  # Inclut toutes les colonnes du modèle
        # Ou spécifiez explicitement les champs
        # fields = ['id', 'name', 'new_column']
        
        

class HistorySerializer(serializers.ModelSerializer):
    DateCreate = serializers.DateField(format="%Y-%m-%d")
    
    class Meta:
        model = History
        '''fields = ('Id',
                  'NumeroPlace',
                  'PlaceCodeQr',
                  'MatriculeCar',
                  'DateCreate',
                  'TypeMouvement') '''
        fields = '__all__'  # Inclut toutes les colonnes du modèle
        # Ou spécifiez explicitement les champs
        # fields = ['id', 'name', 'new_column']