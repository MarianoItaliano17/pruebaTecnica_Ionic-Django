# message/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create-message/', views.create_message, name='create_message'),
    path('messages/', views.get_message, name='get_message'),
    path('message/<int:message_id>/edit/', views.edit_message, name='edit_message'),  # Editar mensaje
    path('message/<int:message_id>/delete/', views.delete_message, name='delete_message'),  # Eliminar mensaje
# Corregido
]