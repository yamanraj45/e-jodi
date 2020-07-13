from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
def index(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Invalid Syntax')
            return redirect('/')
    else:
        return render(request,'home/home.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1== pass2:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'Username has been taken')
                return redirect('/signup')

            elif User.objects.filter(email=email).exists():
                messages.warning(request,'Email already exist')
                return redirect('/signup')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=pass1)
                user.save()
                messages.success(request,"UserCreated")
            return redirect('signup')   
        else:
            messages.error(request,'Password Didnot Matched')
            return redirect('index') 
        
    else:
        return render(request,'home/signup.html')




def logout(request):
    auth.logout(request)
    return redirect('/')
