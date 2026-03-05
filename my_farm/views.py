from django.shortcuts import render 
from rest_framework import status, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import IntegrityError
from .serializers import *
from .models import *
from django.contrib import messages
# Create your views here.
def greeting(request):
    context = {"mesaage": 'hello world'}
    return render(request, 'index.html', context)

def farm(request):
    farmhands = FarmHand.objects.all() 
    return render (request , 'farm.html',{"farmhands":farmhands})

  
def service(request):
    return render (request , 'service.html')

def forms(request):
    if request.method == "POST":
        f_name = request.POST.get("f_name")
        username = request.POST.get("username")
        phone = request.POST.get("phone")
        certification = request.POST.get("certification")
       
    
        new_farmhand.objects.create(
            f_name = f_name,
            username=username,
            phone=phone,
            certification=certification
            )

    return render(request, "forms.html")

# def forms(request):
#     if request.method == 'POST':
#          username = request.POST.get('username')
#          phone = request.POST.get('phone')
#          certification = request.POST.get('certificatioin')
         
         
#          if new_farmhand.objects.filter(username = username).exists():
#               messages.error(request, "username already in use")
#          else:
#              new_farmhand.objects.create( username = username, phone = phone, certification= certification)
#             #  username = new_farmhand(username = username)
#             #  username.save()
#             #  messages.success(request , "thank you for enlisting") 
#             #  return redirect('forms')    
#     return render (request , "forms.html")    
     
     
class FarmCreateAPIView(APIView):
    def get(self,request):
        farms = Farm.objects.select_related('farmhand').all()
        serializer = FarmSerializer(farms, many = True)
        return Response(serializer.data)
    def post(self,request):
        serializer= FarmSerializer(data = request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data , status= status.HTTP_201_CREATED) 
            except IntegrityError:
                return Response({'detail': 'Invalid data'}, status= status.HTTP_409_CONFLICT)
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
        