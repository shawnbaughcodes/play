from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.

# CURRENT USER
def current_user(request):
    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])

# INDEX ROUTE
def index(request):
    return render(request, 'play/index.html')
# END INDEX ROUTE
# REGISTER USER
def process(request):
    is_valid = User.objects.register_validate(request.POST)
    if type(is_valid) == dict:
        for error in is_valid['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        user = User.objects.create_user(request.POST)
        request.session['user_id'] = user.id
        return redirect('/home')
# LOGIN

# RENDER HOME
def home(request):
    user = current_user(request)
    context = {
        'current_user': user
    }
    return render(request, 'play/home.html', context)
