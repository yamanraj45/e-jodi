from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from .models import UserProfile
from django.contrib.gis.geoip2 import GeoIP2

from .models import UserProfile






def index(request):
    g = GeoIP2()
    locationdetail = g.country('113.199.168.246')
    userdetail = UserProfile.objects.all()
    context ={
        "location":locationdetail,
        'userprofiles':userdetail
    }
    UserProfile.location = locationdetail
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.warning(request,'Invalid Syntax')
            return redirect('/')
    else:
        return render(request,'home/home.html', context)







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
                return redirect('/')
            return redirect('signup')   
        else:
            messages.error(request,'Password Didnot Matched')
            return redirect('index') 
        
    else:
        return render(request,'home/signup.html')







def logout(request):
    auth.logout(request)
    return redirect('/')







def profile(request):
    
    
    if UserProfile.objects.filter(user=request.user).exists():
        userdetail = UserProfile.objects.get(user =request.user)
    
        context ={
        
        'userprofile': userdetail
        }
        return render(request,'home/profile.html',context)
    else:
        return redirect('updateuserprofile')
    return redirect('index')


def updateuserprofile(request):
    if UserProfile.objects.filter(user=request.user).exists():
        userdetail = UserProfile.objects.get(user =request.user)
    
        context ={
        
        'userprofile': userdetail
        }
        return render(request,'home/update.html',context)
    else:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'core/simple_upload.html', {
                'uploaded_file_url': uploaded_file_url
            })
        else:
            return render(request,'home/update.html')
    return redirect('index')
    