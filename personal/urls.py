from django.urls import path
from django.contrib import admin
from . import views
from .views import (friend_list, friend_invitations, send_friend_invitation, friend_requests,
                    accept_friend_request)


urlpatterns = [
    path('',views.home,name="home"),
    path('dskb/',views.dskb,name="dskb"),
    path('dsbb/',views.dsbb,name="dsbb"),
    path('dsloimoikb/',views.dsloimoikb,name="dsloimoikb"),


    path('invitations/', friend_invitations, name='friend_invitations'),
    path('send_invitation/<int:receiver_id>/', send_friend_invitation, name='send_friend_invitation'),

    path('list/', friend_list, name='friend_list'),


    path('requests/', friend_requests, name='friend_requests'),
    path('accept_request/<int:request_id>/', accept_friend_request, name='accept_friend_request'),



]