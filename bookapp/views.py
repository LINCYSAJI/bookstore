from django.shortcuts import render,redirect

from bookapp.forms import SignUpForm

from django.views.generic import View

class RegistrationView(View):
    
    def get(self,request,*args, **kwargs):
        
        form_instance=SignUpForm()
        
        return render(request,"register.html",{"form":form_instance})
    
    def post(self,request,*args, **kwargs):
        
        form_instance=SignUpForm(request.POST)
        
        if form_instance.is_valid():
            
            form_instance.save()
            
            print("Account created")
            
            return redirect("register")
        
        return render(request,"register.html",{"form":form_instance})


