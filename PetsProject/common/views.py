from django.shortcuts import render

from PetsProject.pets.models import Pet


# Create your views here.
def index(request):
    context = {
        'pet_photos': Pet.objects.all()
    }
    return render(request, "common/home-page.html", context)

