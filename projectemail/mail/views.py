from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.core.mail import send_mail
def home(request):
    
    
    return render(request,'home.html')

def login(request):
    email= request.POST.get('email')
    password= request.POST.get('password')
    user=auth.authenticate(username=email,password=password)  
    print(user)
    if user is not None:
        username = user.username
        email=user.email   
        first_name = user.first_name
        last_name = user.last_name
        return render(request,'email.html',{"username":username})
        
    else:
        messages.info(request,"invalid credintials")       
    
    return render(request,'login.html')



def compose(request):
    if request.method == 'POST':
        subject=request.POST.get("subject")
        message=request.POST.get('message')
        receiver=request.POST.get('receiver')    
        from_email = 'erhariharan7697@gmail.com'
        recipient_list = [receiver]
        send_mail(subject, message, from_email, recipient_list)
        
        return redirect('email')
    return render(request,"compose.html")

def email(request):
    
    return render(request,"email.html")








def register(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        username = email

        if password == password1:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('register')
            
            elif User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            else:               
                user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            print("Passwords do not match")

    return render(request, 'register.html')


