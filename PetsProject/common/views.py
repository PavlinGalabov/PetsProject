from django.shortcuts import render


# Create your views here.
def home_page(request):
    context = {}
    return render(request, "common/home-page.html", context)
