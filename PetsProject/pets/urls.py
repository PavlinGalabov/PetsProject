from django.urls import path, include

from PetsProject.pets import views

urlpatterns = (
    path("add/", views.add_pets, name="add pets"),
    path("<str:username>/pet/<slug:pet_slug>/", include([
        path("", views.details_pets, name="details pets"),
        path("edit/", views.edit_pets, name="edit pets"),
        path("delete/", views.delete_pets, name="delete pets"),])
    )
)