from django.urls import path
from .views import create_sushi_card

urlpatterns = [
    path('create/', create_sushi_card, name='sushi_card_list'),
]
