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
import random

from .forms import StudentSolicitationForm
from .models import Solicitation
from .status import status
# Get the custom user from settings
User = get_user_model()

class HomeAlunoView(FormView, LoginRequiredMixin):
	
	template_name = 'index.html'
	form_class = StudentSolicitationForm

	def form_valid(self, form):

		email = form.cleaned_data['email']
		course = form.cleaned_data['course']
		semester = form.cleaned_data['semester']
		classs = form.cleaned_data['classs']
		phone_one = form.cleaned_data['phone_one']
		phone_two = form.cleaned_data['phone_two']
		justification = form.cleaned_data['justification']
		solicitation = form.cleaned_data['solicitations']

		new_solicitation = Solicitation(
			student=self.request.user,
			order=str(random.randint(1,101)),
			student_semester=semester,
			classs=classs,
			solicitation=solicitation,
			reason=justification,
			status=status[1]
		)

		new_solicitation.save()

		return HttpResponseRedirect('/accounts/home/aluno/')


	def get_queryset(self):

		student = self.request.user
		return student