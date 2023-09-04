from django.urls import path, include

from . import views

app_name = "bot_app"
urlpatterns = [
    path("", views.rocket_view, name="rocket"),
]
