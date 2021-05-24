from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import uuid
from .models import TimeStamp

# Create your views here.
@api_view(['GET'])
def generate_id(request):
    if request.method == 'GET':

        generated_uuid =  uuid.uuid4()
        
        
        TimeStamp.objects.create(uuid = generated_uuid)
        
        timestamps = TimeStamp.objects.all().order_by('-time')

        data = { time.time.strftime("%Y-%m-%d %H:%M:%S.%f") : time.uuid for time in timestamps}
        
    
        return Response(data, status=status.HTTP_200_OK)


