from django.urls import path
from . import views

urlpatterns = [
    path('create-sushi/', views.create_sushi_card, name='create_sushi_card'),
    path('delete-sushi/<int:card_id>/', views.delete_sushi_card, name='delete_sushi_card'),
    path('update/<int:card_id>/', views.update_sushi_card, name='update_sushi_card'),
    # другие URL
] 

