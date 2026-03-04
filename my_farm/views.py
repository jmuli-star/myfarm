from django.shortcuts import render , redirect
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
     
     
        
    
        