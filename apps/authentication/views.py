from cgi import print_environ
from cmath import log
from http.client import HTTPResponse
import json
from multiprocessing import context
from pyexpat.errors import messages
from re import U
import re
from urllib import response
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import BaseForm, LoginForm, SignUpForm
import requests


def logout_user(request):
    response = redirect("login")
    response.delete_cookie("isLogin")
    response.delete_cookie("token")
    logout(request)
    return response

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            # user = authenticate(username=username, password=password)
            data = {
                "username":username,
                "password":password
            }
            try:      
                login_user = requests.post(url="http://smcity.herokuapp.com/customer/gettoken/",data=data)
                login_user = json.loads(login_user.content)
                print(login_user)
                auth_token = login_user['token']
            except Exception as e:
                print(e)
                auth_token = None

            if auth_token is not None:
                response = redirect("/")
                response.set_cookie("token",auth_token)
                response.set_cookie("isLogin",True)
                return response
            else:
                msg = 'Invalid credentials'
                return redirect("login")
                # return render(request, "accounts/login.html", {"form": form, "msg": msg})

        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        print("post")
        data = {
            "username": request.POST.get("username"),
            "password": request.POST.get("password1")
        }
        isRegister = requests.post(
            url="http://smcity.herokuapp.com/customer/register/", data=data)

        print(type(isRegister.content))
        isRegister = json.loads(isRegister.content)
        print(isRegister["resp"])
        if isRegister["resp"] == "username-not-available":
            return redirect("register")
        else:
            auth_token = isRegister["token"]
            
            headers = {
                "Authorization": f"Token {auth_token}"
            }

            updateData = {
                "user_name": request.POST.get("username"),
                "user_type": request.POST.get("u_type"),
                "is_agent": False,
                "user_phone": request.POST.get("mobile_no"),
                "user_email": request.POST.get("email"),
                "is_verified": True
            }

            updateUser = requests.post(
                url="http://smcity.herokuapp.com/customer/userprofile/", headers=headers, data=updateData)
            print(updateUser.status_code)
            if updateUser.status_code == 200:
                updateUser = json.loads(updateUser.content)
                print(
                    "user created successfully and updated profile. with user type "+updateUser["user_type"])
                
                if request.POST.get('user_type') == "Agent":
                    return redirect("agent").set_cookie("token",auth_token)

                elif request.POST.get('user_type') == 'Supervisor':
                    return redirect("agent").set_cookie("token",auth_token)

                else:
                    return redirect("agent").set_cookie("token",auth_token)

            else:
                print("Updation Faled due to ", updateUser.content)
    return render(request, "accounts/register.html", {"form": form})


def agent(request):
    form = BaseForm()
    if request.method == "POST":
        data = {
            "service_provider": request.POST.get("service_provider"),
            "bank_acc_no": request.POST.get("bank_acc_no"),
            "bank_name": request.POST.get("bank_name"),
            "bank_acc_name": request.POST.get("bank_acc_type"),
            "bank_ifsc": request.POST.get("bank_ifsc"),
            "agent_is_active": False
        }
        registerAgent = requests.post(
            url="https://smcity.herokuapp.com/agent/register/", data=data,)

        print(registerAgent.content)
    return render(request, "accounts/profile.html", {"form": form})


def superVisor(request):
    form = BaseForm()
    return render(request, "accounts/profile.html", {"form": form})


def orgainsation(request):
    form = BaseForm()
    return render(request, "accounts/profile.html", {"form": form})


def profile_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            return render(request, "home/Agent.html")

        elif request.POST.get('u_type') == 'Agent':
            form = AgentForm()
            return render(request, "accounts/profile.html", {"form": form})

        elif request.POST.get('u_type') == 'Supervisor':
            form = SupervisorForm()
            return render(request, "accounts/profile.html", {"form": form})

        else:
            form = OrgForm()
            return render(request, "accounts/profile.html", {"form": form})

        msg = 'User created - please <a href="/login">login</a>.'
        success = True

    else:
        return(render(request, '<p>Invalid attempt</p>'))


def org_home(request):
    org = True
    return render(request, "layouts/home_org.html", {'org': org})


def home1(request):
    org = False
    return render(request, "layouts/home_org.html", {'org': org})


def req(request, org):
    return render(request, "home/send_req.html", {'org': org})


def accept_req(request, org):
    return render(request, "home/accept_req.html", {'org': org})


def view_agent(request, org):
    return render(request, "home/Agent.html", {'org': org})


def view_device(request, org):
    return render(request, "home/Devices.html", {'org': org})


def view_supervisor(request, org):
    return render(request, "home/Supervisors.html", {'org': org})
