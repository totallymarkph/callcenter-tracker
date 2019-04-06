from django.shortcuts import render

def calltracker_homepage(request):
    return render(request, 'calltracker/homepage.html')