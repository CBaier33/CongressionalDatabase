from django.shortcuts import render
from . import util
from . import models

# Create your views here.

def index(request):
    state = util.State()
    state_list = state.list
    return render(request, 'index.html', {
        "states": state_list
        })

def state(request, state_name):
    return render(request, 'state.html', {
        "state_name": state_name
        })

def senate(request, state_name):
    table = models.Senators
    table = table.objects.filter(state=state_name)
    print(table)
    members = list(senator.name for senator in table)
    return render(request, 'branch.html', {
        "state_name": state_name,
        "branch_name": "Senate",
        "members": members
        })

def house(request, state_name):
    table = models.Representatives.objects.filter(state=state_name)
    members = list(representative.name for representative in table)
    return render(request, 'branch.html', {
        "state_name": state_name,
        "branch_name": "House",
        "members": members
        })
