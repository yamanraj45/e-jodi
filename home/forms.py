from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ('user',)
       
    def __init__(self, *args, **kwargs):
        super(UserProfileForm,self).__init__()
        self.fields['gender'].empty_label = 'Select Your Gender'
        self.fields['avatar'].required = False
        self.fields['hobby'].required = False
        self.fields['bio'].required = False
        self.fields['age'].required = False
        self.fields['location'].required = False
        self.fields['gender'].required = False

    
        
        