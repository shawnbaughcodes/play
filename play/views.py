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
def login(request):
    is_valid = User.objects.login_validate(request.POST)
    if is_valid['status'] == True:
        request.session['user_id'] = is_valid['user'].id
        return redirect('/home')
    else:
        if is_valid['status'] == False:
            messages.error(request, is_valid['message'])
            return redirect('/')
# LOGOUT
def logout(request):
    request.session.clear()
    return redirect('/')
# RENDER HOME
def home(request):
    user = current_user(request)
    sports_ids = []
    for sport in user.sports.all():
        sports_ids.append(sport.id)
    events = Event.objects.all() #.where(location =)
    context = {
        'current_user': user,
        'sports': Sport.objects.all(),
        'user_sports': user.sports.all(),
        'sports_ids': sports_ids,
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
    'events': events,
    'sports_ids': sports_ids,
    }
    return render(request, 'play/sport.html', context)
# ADD SPORT
def add_sport(request, id):
    user = current_user(request)
    sport = Sport.objects.get(id=id)
    user.sports.add(sport)
    return redirect('/sports')
# REMOVE SPORT
def remove_sport(request, id):
    user = current_user(request)
    sport = Sport.objects.get(id=id)
    user.sports.remove(sport)
    return redirect('/sports')
# SHOW SPORT EVENT PAGE
def sport_event(request, id):
    sport = Sport.objects.get(id=id)
    user = current_user(request)
    events = Event.objects.filter(sport = sport)
    users_sports = sport.users.all()
    context = {
        'sport': sport,
        'current_user': user,
        'events': events,
        'users_sports': users_sports
    }
    return render(request, 'play/event_sport.html', context)
# NEW GAME PAGE
def new_game(request, id):
    sport = Sport.objects.get(id=id)
    context = {
        'sport': sport,
        'current_user': current_user(request),
        'users': User.objects.filter(sports = sport)
    }
    return render(request, 'play/new_game.html', context)
# ADD EVENT
def add_event(request, id):

    return redirect('/games/id')
