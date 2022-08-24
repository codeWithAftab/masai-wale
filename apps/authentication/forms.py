from lib2to3.pytree import Base
from operator import truediv
from random import choices
from re import T
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# from apps.authentication.views import agent


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    mobile_no = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Phone number",
                "class": "form-control"
            }
        ), required=False
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))
    Country = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Country",
                "class": "form-control"
            }
        ))
    State = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "State",
                "class": "form-control"
            }
        ))
    City = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "City",
                "class": "form-control"
            }
        ))
    Address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Address",
                "class": "form-control"
            }
        ))
    usertype=(
        ('Choose Your Type','Choose'),
        ('Agent','Agent'),
        ('Supervisor','Supervisor'),
        ('Organization','Organization')
    )
    u_type = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control"
            },
            choices=usertype
        )
        
    )

    class Meta:
        model = User
        fields = ('username', 'email','mobile_no', 'password1', 'password2', 'Country', 'State', 'City', 'Address','u_type')

 
class BaseForm(forms.Form):
    service_provider = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Service Provide",
                "class": "form-control"
            }
        ), required=False
    )
    bank_acc_no = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Bank account number",
                "class": "form-control"
            }
        ), required=False
    )
    bank_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Bank Name",
                "class": "form-control"
            }
        ), required=False
    )
    
    bank_type=(
        ('---','Type of Bank Account'),
        ('type','Saving Account'),
        ('type','Current Account'),
    )
    bank_ifsc = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ifsc Code",
                "class": "form-control"
            }
        ),required=True
    )
    bank_acc_type = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-control"
            },
            choices=bank_type
        ), required=False
    )


# class AgentForm(BaseForm):

# class SupervisorForm(BaseForm):

# class OrgForm(BaseForm):

# class SupervisorForm(forms.Form):
#     pincode_sup = forms.IntegerField(
#         widget=forms.NumberInput(
#             attrs={
#                 "placeholder": "Pin Code",
#                 "class": "form-control"
#             }
#         ), required=False
#     )


# class OrgForm(forms.Form):
#     pincode_org = forms.IntegerField(
#         widget=forms.NumberInput(
#             attrs={
#                 "placeholder": "Pin Code",
#                 "class": "form-control"
#             }
#         ), required=False
#     )

#     bank_acc_org = forms.IntegerField(
#         widget=forms.NumberInput(
#             attrs={
#                 "placeholder": "Bank account number",
#                 "class": "form-control"
#             }
#         ), required=False
#     )
    