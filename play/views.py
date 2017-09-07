from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import operator, datetime
import boto3
# Create your views here.

# CURRENT USER
def current_user(request):
    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])

# INDEX ROUTE
def index(request):
    if current_user(request):
        return redirect('/home')
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
def add_user_photo(request):
    pass
# RENDER HOME
def home(request):
    # class PlaySearchListView(PlayListView):
    #     paginate_by = 10
    #     def get_queryset(self):
    #         result = super(PlaySearchListView, self).get_queryset()
    #
    #         query = self.request.GET.get('search')
    #         if query:
    #             query_list = query.split()
    #             result = result.filter(
    #             reduce(operator.or_,
    #                 (Q(title__icontains=search)))
    #             )
    user = current_user(request)
    sports_ids = []
    for sport in user.sports.all():
        sports_ids.append(sport.id)
    event =  Event.objects.all()
    # for user in

    events = Event.objects.prefetch_related('users').all().order_by('-created_at')
    friends = user.friend.all()
    users = User.objects.all()
    context = {
        'current_user': user,
        'sports': Sport.objects.all(),
        'teams': Team.objects.all(),
        'user_sports': user.sports.all(),
        'sports_ids': sports_ids,
        'friends': friends,
        'events': events,
        'users': users,
    }
    return render(request, 'play/home.html', context)

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
# ADD TEAM
def add_team(request):
    users_array = [int(x) for x in request.POST.getlist('players')]
    team = Team.objects.create(
        title=request.POST['title'],
        sport=Sport.objects.get(id=request.POST['sport'])
    )
    for user_id in users_array:
        team.user.add(User.objects.get(id=user_id))
    # team.sport.add(Sport.objects.get(id=request.POST['sport']))
    return redirect('/home')
# ADD EVENT
def add_event(request):
    users_array = [int(x) for x in request.POST.getlist('players')]
    teams_array = [int(x) for x in request.POST.getlist('teams')]
    # print users_array
    user = current_user(request)
    event = Event.objects.create(
        name=request.POST['name'],
        date=request.POST['date'],
        time=request.POST['time'],
        description=request.POST['description'],
        location=request.POST['location'],
        sport=Sport.objects.get(id=request.POST['sport']),
        user=user,
    )
    for user_id in users_array:
        event.users.add(User.objects.get(id=user_id))
    for team_id in teams_array:
        event.teams.add(Team.objects.get(id=team_id))
    event.teams.add(Team.objects.get(id=request.POST['teams']))
    # event = Event.objects.create_event(request.POST)
    # event.users.add(User.objects.get(id=request.POST['user']))
    # event.sport.add(Sport.objects.get(id=request.POST['sport']))

    return redirect('/home')

def chat_room(request, label):
    room, created = Room.objects.get_or_create(label=label)

    messages = reversed(room.messages.order_by('-timestamp')[:50])

    return render(request, "play/room.html", {
        'room': room,
        'messages': messages,
    })
