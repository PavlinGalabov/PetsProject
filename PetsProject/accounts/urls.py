from django.urls import path, include

from PetsProject.accounts.views import (signup_user, signin_user,
                                       signout_user, details_profile,
                                       delete_profile, edit_profile)

urlpatterns = (
    path("register/", signup_user, name="signup user"),
    path("login/", signin_user, name="signin user"),

    path("profile/<int:pk>/", include([
        path("", details_profile, name="details profile"),
        path("edit/", edit_profile, name="edit profile"),
        path("delete/", delete_profile,name="delete_profile"),
        ]),
    )
)
