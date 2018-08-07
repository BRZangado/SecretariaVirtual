# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _
from django.http.response import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model, logout
from django.contrib.auth import logout as django_logout
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView, FormView
import random

from .forms import StudentSolicitationForm, SecretarySolicitationForm, DirectorSolicitationForm
from .models import Solicitation, Feedback
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

		return HttpResponseRedirect(reverse('accounts:homealuno'))

class HomeSecretaryView(TemplateView, LoginRequiredMixin):
	
	template_name = 'homesec.html'

	def get_context_data(self, **kwargs):

		context = super(HomeSecretaryView, self).get_context_data(**kwargs)
		solicitations = Solicitation.objects.all()

		context['solicitations'] = solicitations

		return context


class AnalysisSecretaryView(FormView, LoginRequiredMixin):
	
	template_name = 'secanalysis.html'
	form_class = SecretarySolicitationForm

	def form_valid(self, form):

		student_academic_situation = form.cleaned_data['student_academic_situation']
		feedback = form.cleaned_data['feedback']

		feedback = Feedback(
			feedbacker=self.request.user,
			feedback=feedback
		)

		feedback.save()
		
		solicitation = self.get_solicitation()
		solicitation.student_academic_situation = student_academic_situation
		solicitation.save()

		solicitation.feedbacks.add(feedback)
		solicitation.save()

		return HttpResponseRedirect(reverse('accounts:homesecretaria'))

	def get_context_data(self, **kwargs):

		context = super(AnalysisSecretaryView, self).get_context_data(**kwargs)
		solicitation = self.get_solicitation()
		context['solicitation'] = solicitation

		return context

	def get_solicitation(self):

		solicitation = Solicitation.objects.get(pk=self.kwargs.get('sol_id'))
		return solicitation


class HomeDirectorView(TemplateView, LoginRequiredMixin):

	template_name = 'homedir.html'

	def get_context_data(self, **kwargs):

		context = super(HomeDirectorView, self).get_context_data(**kwargs)
		solicitations = Solicitation.objects.all()

		context['solicitations'] = solicitations

		return context


class AnalysisDirectorView(FormView, LoginRequiredMixin):
	
	template_name = 'directoranalysis.html'
	form_class = DirectorSolicitationForm

	def form_valid(self, form):
		feedback = form.cleaned_data['feedback']

		feedback = Feedback(
			feedbacker=self.request.user,
			feedback=feedback
		)

		feedback.save()
		
		solicitation = self.get_solicitation()
		solicitation.status = status[1]
		solicitation.save()

		solicitation.feedbacks.add(feedback)
		solicitation.save()

		return HttpResponseRedirect(reverse('accounts:homediretoria'))

	def get_context_data(self, **kwargs):

		context = super(AnalysisDirectorView, self).get_context_data(**kwargs)
		solicitation = self.get_solicitation()
		context['solicitation'] = solicitation

		return context

	def get_solicitation(self):

		solicitation = Solicitation.objects.get(pk=self.kwargs.get('sol_id'))
		return solicitation

def send_solitation_to(request, sol_id, status_to):

	solicitation_status = status[status_to]

	solicitation = Solicitation.objects.get(pk=sol_id)
	solicitation.status = solicitation_status

	solicitation.save()

	return HttpResponseRedirect(reverse('accounts:homesecretaria'))

def logout(request):
	django_logout(request)
	return HttpResponseRedirect(reverse('core:index'))