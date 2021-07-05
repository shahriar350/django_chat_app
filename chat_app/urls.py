
from django.urls import path
from . import views

urlpatterns = [
    # path('<str:room_name>/', views.room, name='room'),
    path('', views.chat_view, name="index"),
    path('message/<int:user_id>/', views.message_id, name="message"),
    path('registration/', views.registration, name="registration"),
    path('login/', views.login_set, name="login"),
]
