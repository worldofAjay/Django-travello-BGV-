from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

def BGVindex(request):
    return render(request, 'BGVindex.html')

def forms(request):
    pass