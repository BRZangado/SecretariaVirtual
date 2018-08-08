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

from .forms import (
	StudentSolicitationForm, SecretarySolicitationForm, GenericFeedbackForm
)
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


class StudentTrackSolicitationsView(TemplateView, LoginRequiredMixin):

	template_name = 'mysolicitations.html'

	def get_context_data(self, **kwargs):

		context = super(StudentTrackSolicitationsView, self).get_context_data(**kwargs)
		solicitations = Solicitation.objects.filter(
			student=self.request.user
		)

		context['solicitations'] = solicitations

		return context

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

		solicitation = self.get_solicitation()

		for feedback in solicitation.feedbacks.all():
			if feedback.feedbacker.usuario.is_secretary:
				solicitation.feedbacks.remove(feedback)
				feedback.delete()

		student_academic_situation = form.cleaned_data['student_academic_situation']
		feedback_from_form = form.cleaned_data['feedback']

		new_feedback = Feedback(
			feedbacker=self.request.user,
			feedback=feedback_from_form
		)

		new_feedback.save()

		solicitation.student_academic_situation = student_academic_situation
		solicitation.save()

		solicitation.feedbacks.add(new_feedback)
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
	form_class = GenericFeedbackForm

	def form_valid(self, form):

		solicitation = self.get_solicitation()

		for feedback in solicitation.feedbacks.all():
			if feedback.feedbacker.usuario.is_director:
				solicitation.feedbacks.remove(feedback)
				feedback.delete()

		feedback_from_form = form.cleaned_data['feedback']

		new_feedback = Feedback(
			feedbacker=self.request.user,
			feedback=feedback_from_form
		)

		new_feedback.save()

		solicitation.feedbacks.add(new_feedback)
		solicitation.save()

		solicitation.status = status[1]
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


class HomeCoordinationView(TemplateView, LoginRequiredMixin):

	template_name = 'homecoord.html'

	def get_context_data(self, **kwargs):

		context = super(HomeCoordinationView, self).get_context_data(**kwargs)
		solicitations = Solicitation.objects.all()

		context['solicitations'] = solicitations

		return context


class AnalysisCoordinationView(FormView, LoginRequiredMixin):
	
	template_name = 'coordinationanalysis.html'
	form_class = GenericFeedbackForm

	def form_valid(self, form):

		solicitation = self.get_solicitation()

		for feedback in solicitation.feedbacks.all():
			if feedback.feedbacker.usuario.is_coordination:
				solicitation.feedbacks.remove(feedback)
				feedback.delete()

		feedback_from_form = form.cleaned_data['feedback']

		new_feedback = Feedback(
			feedbacker=self.request.user,
			feedback=feedback_from_form
		)

		new_feedback.save()

		solicitation.feedbacks.add(new_feedback)
		solicitation.save()

		solicitation.status = status[1]
		solicitation.save()

		return HttpResponseRedirect(reverse('accounts:homecoordination'))
		
	def get_context_data(self, **kwargs):

		context = super(AnalysisCoordinationView, self).get_context_data(**kwargs)
		solicitation = self.get_solicitation()
		context['solicitation'] = solicitation

		return context

	def get_solicitation(self):

		solicitation = Solicitation.objects.get(pk=self.kwargs.get('sol_id'))
		return solicitation


class HomeLibraryView(TemplateView, LoginRequiredMixin):

	template_name = 'homelibrary.html'

	def get_context_data(self, **kwargs):

		context = super(HomeLibraryView, self).get_context_data(**kwargs)
		solicitations = Solicitation.objects.all()

		context['solicitations'] = solicitations

		return context


class AnalysisLibraryView(FormView, LoginRequiredMixin):
	
	template_name = 'libraryanalysis.html'
	form_class = GenericFeedbackForm

	def form_valid(self, form):

		solicitation = self.get_solicitation()

		for feedback in solicitation.feedbacks.all():
			if feedback.feedbacker.usuario.is_library:
				solicitation.feedbacks.remove(feedback)
				feedback.delete()

		feedback_from_form = form.cleaned_data['feedback']

		new_feedback = Feedback(
			feedbacker=self.request.user,
			feedback=feedback_from_form
		)

		new_feedback.save()

		solicitation.feedbacks.add(new_feedback)
		solicitation.save()

		solicitation.status = status[1]
		solicitation.save()

		return HttpResponseRedirect(reverse('accounts:homelibrary'))

	def get_context_data(self, **kwargs):

		context = super(AnalysisLibraryView, self).get_context_data(**kwargs)
		solicitation = self.get_solicitation()
		context['solicitation'] = solicitation

		return context

	def get_solicitation(self):

		solicitation = Solicitation.objects.get(pk=self.kwargs.get('sol_id'))
		return solicitation


class HomeFinanceView(TemplateView, LoginRequiredMixin):

	template_name = 'homefinance.html'

	def get_context_data(self, **kwargs):

		context = super(HomeFinanceView, self).get_context_data(**kwargs)
		solicitations = Solicitation.objects.all()

		context['solicitations'] = solicitations

		return context


class AnalysisFinanceView(FormView, LoginRequiredMixin):
	
	template_name = 'financeanalysis.html'
	form_class = GenericFeedbackForm

	def form_valid(self, form):

		solicitation = self.get_solicitation()

		for feedback in solicitation.feedbacks.all():
			if feedback.feedbacker.usuario.is_finance:
				solicitation.feedbacks.remove(feedback)
				feedback.delete()

		feedback_from_form = form.cleaned_data['feedback']

		new_feedback = Feedback(
			feedbacker=self.request.user,
			feedback=feedback_from_form
		)

		new_feedback.save()

		solicitation.feedbacks.add(new_feedback)
		solicitation.save()

		solicitation.status = status[1]
		solicitation.save()

		return HttpResponseRedirect(reverse('accounts:homefinance'))

	def get_context_data(self, **kwargs):

		context = super(AnalysisFinanceView, self).get_context_data(**kwargs)
		solicitation = self.get_solicitation()
		context['solicitation'] = solicitation

		return context

	def get_solicitation(self):

		solicitation = Solicitation.objects.get(pk=self.kwargs.get('sol_id'))
		return solicitation


class HomeNapesView(TemplateView, LoginRequiredMixin):

	template_name = 'homenapes.html'

	def get_context_data(self, **kwargs):

		context = super(HomeNapesView, self).get_context_data(**kwargs)
		solicitations = Solicitation.objects.all()

		context['solicitations'] = solicitations

		return context


class AnalysisNapesView(FormView, LoginRequiredMixin):
	
	template_name = 'napesanalysis.html'
	form_class = GenericFeedbackForm

	def form_valid(self, form):

		solicitation = self.get_solicitation()

		for feedback in solicitation.feedbacks.all():
			if feedback.feedbacker.usuario.is_napes:
				solicitation.feedbacks.remove(feedback)
				feedback.delete()

		feedback_from_form = form.cleaned_data['feedback']

		new_feedback = Feedback(
			feedbacker=self.request.user,
			feedback=feedback_from_form
		)

		new_feedback.save()

		solicitation.feedbacks.add(new_feedback)
		solicitation.save()

		solicitation.status = status[1]
		solicitation.save()

		return HttpResponseRedirect(reverse('accounts:homenapes'))

	def get_context_data(self, **kwargs):

		context = super(AnalysisNapesView, self).get_context_data(**kwargs)
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