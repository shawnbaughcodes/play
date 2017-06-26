from django.shortcuts import render
from .models import *
# Create your views here.

# INDEX ROUTE
def index(request):
    return render (request, 'play/index.html')
