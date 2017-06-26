from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.

# INDEX ROUTE
def index(request):
    return render (request, 'play/index.html')
# END INDEX ROUTE
# REGISTER USER
def process(request):
    is_valid = User.objecst.register_validate(request.POST)
    if type(is_valid) == dict:
        for error in is_valid['errors']:
            messages.error(request, error)
            return redirect('/')
    else:
        user = User.objects.create_user(request.POST)
        return render(request, 'play/home.html')
