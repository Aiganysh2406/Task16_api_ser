from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Vaccina
from .serializers import VaccinaSerializer

@api_view(['GET'])
def get_vaccina(request):
    queryset = Vaccina.objects.all()
    serializer = VaccinaSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_vacina(request):
    serialzer = VaccinaSerializer(data=request.data)
    if serialzer.is_valid():
        serialzer.save()
        return Response(serialzer.data, status=status.HTTP_201_CREATED)
    return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['Get'])
def get_one_vaccina(request, pk):
    try:
        product = Vaccina.objects.get(pk=pk)
    except Vaccina.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serilizer = VaccinaSerializer(product)
    return Response(serilizer.data)





