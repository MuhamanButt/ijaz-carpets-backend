from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .mongodb import *
from .serializers import *
from .models import *

@api_view(['GET'])
def get_settings(request):
    settings = settings_collection.find_one()
    if settings:
        serializer = SettingsSerializer(settings)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'message': 'Settings not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def set_settings(request):
    serializer = SettingsSerializer(data=request.data)
    
    if serializer.is_valid():
        validated_data = serializer.validated_data
        
        result = settings_collection.replace_one({}, validated_data, upsert=True)
        
        if result.modified_count or result.upserted_id:
            return Response({'message': 'Settings updated successfully'}, status=status.HTTP_200_OK)
        
        return Response({'message': 'No changes made to settings'}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)