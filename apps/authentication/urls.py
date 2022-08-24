# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/",logout_user, name="logout"),
    path('agent/',agent, name="agent"),
    path('profile/',profile_user, name="profile"),
    path('org_home/',org_home,name="org_home"),
    path('home1/',home1 ,name="home1"),
    path('send request/<str:org>',req, name="req"),
    path('accept request/<str:org>',accept_req, name="accept_req"),
    path('agents list/<str:org>',view_agent, name="agents"),
    path('devices list/<str:org>',view_device, name="devices"),
    path('supervisors list/<str:org>',view_supervisor, name="supervisors"),
]
