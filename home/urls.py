from django.urls import path
from . import views
from notification.views import notification

urlpatterns=[
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('notification',notification,name='notification'),
    path('profile/update',views.updateuserprofile,name='updateuserprofile'),
    
    
]