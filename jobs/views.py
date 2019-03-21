from django.shortcuts import render

#get acces from the model to send to the view
from .models import job 

def home(request):
    jobs = job.objects     # get all jobs 
    return render(request, 'jobs/home.html', {'jobs':jobs})

# Create your views here.
