from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required
def index(request):
    return render(request,'statiune/index.html'
                          '')
def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'statiune/index.html')
    context['form']=form
    return render(request,'registration/sign_up.html',context)

def logout_view(request):
    logout(request)
    return render(request,'registration/logged_out.html'
                          '')

