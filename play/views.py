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
# RENDER SPORT PAGE
def sport(request):
    user = current_user(request)
    # user_sports = user.sports.all()
    sports_ids = []

    for sport in user.sports.all():
        sports_ids.append(sport.id)

    context = {
    'current_user': user,
    'sports': Sport.objects.all(),
    'user_sports': user.sports.all(),
    'sports_ids': sports_ids,
    }
    return render(request, 'play/sport.html', context)
# ADD SPORT
def add_sport(request, id):
    user = current_user(request)
    sport = Sport.objects.get(id=id)
    user.sports.add(sport)
    return redirect('/sports')
