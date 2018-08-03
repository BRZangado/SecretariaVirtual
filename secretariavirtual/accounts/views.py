# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _
from django.http.response import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView, FormView

from .forms import StudentSolicitationForm
# Get the custom user from settings
User = get_user_model()

class HomeAlunoView(FormView, LoginRequiredMixin):
	
	template_name = 'index.html'
	form_class = StudentSolicitationForm