from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from .models import UserProfile
from django.core.files.storage import FileSystemStorage
from .models import UserProfile, Gender
from .forms import UserProfileForm





def index(request):
    
    userdetail = UserProfile.objects.all()
    context ={
        
        'userprofiles':userdetail
    }
    
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
        title = "Update You User Profile"
        context ={
        
        'userprofile': userdetail,
        'title': title
        }
        if request.method== 'POST':
                
                
                bio = request.POST['bio']
                userdetail.bio=bio
                
                
                age = request.POST['age']
                userdetail.age = age
                
                
                hobby = request.POST['hobby']
                userdetail.hobby = hobby
                location = request.POST['location']
                userdetail.location = location
                userdetail.save()
                # print(gender)
                # location = request.POST['location']
                # if request.POST['avatar']:
                #     avatar = request.FILES['avatar']
                # userprofile = UserProfile(user=user,bio=bio,age=age,gender=gender,location=location,hobby=hobby,avatar=avatar)
                # print(userprofile)
                
                return redirect('profile')
        

        return render(request,'home/update.html',context)
    else:
        
        if request.method == 'GET':
            form = UserProfileForm()
            
        
            title = "Create Your Profile"
            
            
            return render(request, 'home/update.html',{'form':form,'title':title})


            
        else:
            if request.method== 'POST':
                gender =''
                
                bio = request.POST['bio']
                user = request.user
                age = request.POST['age']
                avatar = request.FILES['avatar']
                gender = request.POST['gender']
                print(gender)
                gender = Gender.objects.get(gender= gender)
                print(gender)
                location = request.POST['location']
                hobby = request.POST['hobby']
                userprofile = UserProfile(user=user,bio=bio,age=age,gender=gender,location=location,hobby=hobby,avatar=avatar)
                userprofile.save()
                
                return redirect('profile')
            else:
            
                return render(request,'home/profile.html')
                
            
        
    return redirect('index')
    