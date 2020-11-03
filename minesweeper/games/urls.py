from django.conf import settings
from django.urls import path

from games import views

app_name = 'games'

urlpatterns = [
    path(
        '', views.GameListCreateView.as_view(),
        name='list_create'
    ),
    path(
        '<uuid:pk>/', views.GameRetrieveUpdateView.as_view(),
        name='retrieve_update'
    ),
]
