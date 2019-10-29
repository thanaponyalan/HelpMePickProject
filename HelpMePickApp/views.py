from django.shortcuts import render, redirect

from .forms import ActivityForm
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def act(request):
    return render(request,'activity.html')

def getAct(request):
    if request.method=='POST':
        form=ActivityForm(request.POST)
        if form.is_valid():
            filteredAct=Activity.objects.filter(ageRange=form.data['ageRange'],actType=form.data['actType'])
            #filteredAct.random()
            return render(request,'showActivity.html',{'data': filteredAct.random()})
    
    return redirect('activity')