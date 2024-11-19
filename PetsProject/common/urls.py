from django.urls import path
from PetsProject.common.views import index

urlpatterns = (
    path("", index, name="index"),
)