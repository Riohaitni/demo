from django.urls import path
from django.contrib import admin
from . import views
from .views import (friend_list, send_friend_invitation, friend_requests,
                    accept_friend_request, send_friend_request)


urlpatterns = [
    path('home/', views.home, name='home'),
    path('base/', views.base, name="base"),
    path('', views.loginPage, name="login"),
    path('dskb/', views.list, name='dskb'),
    path('dsloimoikb/', views.friend_invitation_view, name='dsloimoikb'),
    # path('send_friend_invitation/<int:receiver_id>/', send_friend_invitation, name='send_friend_invitation'),
    path('requests/', friend_requests, name='friend_requests'),
    path('accept_request/<int:request_id>/', accept_friend_request, name='accept_friend_request'),
    path('friend-list/', friend_list, name='friend_list'),
    path('dsbb/', views.friendship_view, name='dsbb'),




]