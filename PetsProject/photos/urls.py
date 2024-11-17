from django.urls import path

from PetsProject.photos import views

urlpatterns = (
    path("add/", views.add_photos, name="add photos"),
    path("<int:pk>/", views.details_photos, name="details photos"),
    path("<int:pk>/edit/", views.edit_photos, name="edit photos"),
)