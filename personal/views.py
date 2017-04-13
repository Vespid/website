from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "personal/home.html")

def food_club(request):
	return render(request, "personal/food_club.html")