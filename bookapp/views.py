from django.shortcuts import render

from bookapp.forms import SignUpForm

from django.views.generic import View

class RegistrationView(View):
    
    def get(self,request,*args, **kwargs):
        
        form_instance=SignUpForm()
        
        return render(request,"register.html",{"form":form_instance})

