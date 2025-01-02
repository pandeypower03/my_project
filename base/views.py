from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

#it will check if the user is logged inn or not if not logged in then redirect to home page
@login_required
#after successful registration in login and signup
def home(request):
    return render(request,"home.html",{})

def authView(request):
    #to save the form in signup
    if request.method=="POST":
        form=UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form=UserCreationForm
    return render(request, "registration/signup.html",{"form":form})

# Create your views here.
