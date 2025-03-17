
from django.urls import path
from .views import steganography_view
from stegnoapp import views

urlpatterns = [
    path('', steganography_view, name='steganography'),
    path('',views.encode_message, name='encode'),
    path('',views.decode_message, name='decode')
]