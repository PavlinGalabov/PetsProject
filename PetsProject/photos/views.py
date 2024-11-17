from django.shortcuts import render


# Create your views here.
def add_photos(request):
    context = {}
    return render(request, "photos/photo-add-page.html", context)


def details_photos(request):
    context = {}
    return render(request, "photos/photo-details-page.html", context)


def edit_photos(request):
    context = {}
    return render(request, "photos/photo-edit-page.html", context)
