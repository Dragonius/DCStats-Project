from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from stats.models import Pilot
from home.forms import SignUpForm, UserProfileForm, PilotProfileForm
from django.core.exceptions import ObjectDoesNotExist
import datetime
import pytz

def home(request):
    time = datetime.datetime.now(pytz.utc)
    return render(request, 'home/home.html', {'time':time})

def logout_view(request):
    logout(request)
    return render(request, 'home/logout.html')
    
def login(request):
    return render(request, 'home/login.html')

def inactive(request):
    return render(request, 'home/inactive.html')
    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            auth_login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'home/signup.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        userform=UserProfileForm(request.POST, instance=request.user)
        if userform.is_valid():
            userform.save()
            change = 'Change Submitted'
        if not userform.is_valid():
            change = 'Problem sumbitting request, please contact administrator'
    else:
        userform = UserProfileForm(instance=request.user)
        change = ''
    try:
        pilot = Pilot.objects.get(user=request.user)
        pilotform=PilotProfileForm(instance=pilot)
    except ObjectDoesNotExist:
        pilotform = None
        pilot = {'rank_id':"Welcome Guest!"}
    
    return render(request, 'home/profile.html', {'userform':userform, 'pilot':pilot, 'change':change, 'pilotform':pilotform})