from django.shortcuts import render,redirect
from My_Celery_App.tasks import add,mul,send_mail_func
from django.contrib import messages
from .models import Signup


# Create your views here.
def index(request):
    add.delay(10,29)
    return render (request,'My_Celery_App/index.html')


def home(request):
    mul.delay(10,50*70)
    return render(request,'My_Celery_App/home.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
    
        
        if not first_name or not last_name or not email or not phone_number or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return redirect('register')
        
    
        if Signup.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('register')
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        
        
        signup = Signup.objects.create(
            first_name=first_name,
            last_name=last_name,
            email_id=email,
            phone_number=phone_number,
            password=password, 
            confirm_password=confirm_password,

        )
        signup.save()
        send_mail_func()
        return redirect('index')
    return render(request, 'My_Celery_App/register.html')