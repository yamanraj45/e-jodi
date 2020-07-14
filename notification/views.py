from django.shortcuts import render

def notification(request):
    return render(request,'home/notification.html')