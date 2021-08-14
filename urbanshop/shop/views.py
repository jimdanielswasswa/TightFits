from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from .models import Sale
from .serializers import SaleSerializer

@csrf_exempt
def index(request):
    if request.method == 'GET':
        sales = Sale.objects.all()
        serializer = SaleSerializer(sales, many = True)
        return JsonResponse(serializer.data, safe = False)
