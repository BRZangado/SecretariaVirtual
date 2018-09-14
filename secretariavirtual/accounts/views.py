# Django imports
from __future__ import print_function
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model, logout
from django.contrib.auth import logout as django_logout
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView, FormView
from django.core.files.storage import FileSystemStorage
import random

from .forms import (
	StudentSolicitationForm, SecretarySolicitationForm, GenericFeedbackForm
)
from .models import Solicitation, Feedback
from .status import status
import datetime
from datetime import date
from .writefile import WriteAndDownload
from secretariavirtual.settings import STATICFILES_DIRS
# Get the custom user from settings
User = get_user_model()

class HomeAlunoView(FormView, LoginRequiredMixin):

	'''
	Main Student View.
	'''
	
	template_name = 'index.html'
	form_class = StudentSolicitationForm

	def form_valid(self, form):

		'''
		Receive form already validated
		'''

		email = form.cleaned_data['email']
		code = form.cleaned_data['code']
		course = form.cleaned_data['course']
		semester = form.cleaned_data['semester']
		classs = form.cleaned_data['classs']
		phone_one = form.cleaned_data['phone_one']
		phone_two = form.cleaned_data['phone_two']
		justification = form.cleaned_data['justification']
		solicitation = form.cleaned_data['solicitations']

		now = datetime.datetime.now()
		if Solicitation.objects.count() < 100:
			prefix = "00"+str(Solicitation.objects.count())
		else:
			prefix = str(Solicitation.objects.count())

		solicitation_order = str(prefix)+"-"+str(now.year)

		'''
		Get attachments if uploaded
		'''

		attachment_rg = form.cleaned_data['attachment_rg']
		attachment_voters_title = form.cleaned_data['attachment_voters_title']
		attachment_cpf = form.cleaned_data['attachment_cpf']
		attachment_proof_electoral_discharge = form.cleaned_data['attachment_proof_electoral_discharge']
		attachment_reservist = form.cleaned_data['attachment_reservist']
		attachment_birth_marriage_certificate = form.cleaned_data['attachment_birth_marriage_certificate']
		attachment_highschool_certificate = form.cleaned_data['attachment_highschool_certificate']
		attachment_school_historic = form.cleaned_data['attachment_school_historic']
		attachment_academic_bond_certificate = form.cleaned_data['attachment_academic_bond_certificate']
		attachment_discipline_menu = form.cleaned_data['attachment_discipline_menu']
		attachment_degree = form.cleaned_data['attachment_degree']

		'''
		Create new solicitation
		'''

		new_solicitation = Solicitation(
			email=email,
			phone1=phone_one,
			phone2=phone_two,
			student=self.request.user,
			order=solicitation_order,
			student_semester=semester,
			classs=classs,
			solicitation=solicitation,
			reason=justification,
			status=status[1],
			code=code,
			attachment_rg=attachment_rg,
			attachment_voters_title=attachment_voters_title,
			attachment_cpf=attachment_cpf,
			attachment_proof_electoral_discharge=attachment_proof_electoral_discharge,
			attachment_reservist=attachment_reservist,
			attachment_birth_marriage_certificate=attachment_birth_marriage_certificate,
			attachment_highschool_certificate=attachment_highschool_certificate,
			attachment_school_historic=attachment_school_historic,
			attachment_academic_bond_certificate=attachment_academic_bond_certificate,
			attachment_discipline_menu=attachment_discipline_menu,
			attachment_degree=attachment_degree,
		)

		new_solicitation.save()

		return HttpResponseRedirect(reverse('accounts:homealuno'))


class StudentTrackSolicitationsView(TemplateView, LoginRequiredMixin):

	'''
	View for students to track submitted solicitations
	'''

	template_name = 'mysolicitations.html'

	def get_context_data(self, **kwargs):

		context = super(StudentTrackSolicitationsView, self).get_context_data(**kwargs)
		solicitations = Solicitation.objects.filter(
			student=self.request.user
		)

		context['solicitations'] = solicitations

		return context

class HomeSecretaryView(TemplateView, LoginRequiredMixin):

	'''
	Home View for Secretary. Lists solicitations.
	'''
	
	template_name = 'homesec.html'

	def get_context_data(self, **kwargs):

		context = super(HomeSecretaryView, self).get_context_data(**kwargs)
		solicitations = Solicitation.objects.all()

		context['solicitations'] = solicitations

		return context


class AnalysisSecretaryView(FormView, LoginRequiredMixin):

	'''
	View for Secretary fill his/her solicitation feedbac
	and student academic situation
	'''
	
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


class ClosedSolicitationsView(TemplateView, LoginRequiredMixin):

	'''
	View to list closed solicitations by year 
	'''
	
	template_name = 'closedsolicitations.html'

	def get_context_data(self, **kwargs):

		context = super(ClosedSolicitationsView, self).get_context_data(**kwargs)

		years = []

		closed_solicitations = Solicitation.objects.filter(
			status=status[0]
		)

		for solicitation in closed_solicitations:
			years.append(solicitation.created_at.year)

		unique_years = set(years)

		for year in unique_years:
			print(year)

		context['years'] = unique_years

		return context


class ClosedSolicitationsByYearView(TemplateView, LoginRequiredMixin):

	'''
	View for Secretary manage the chosen closed solicitation
	'''

	template_name = 'closed_solicitations_by_year.html'

	def get_context_data(self, **kwargs):

		context = super(ClosedSolicitationsByYearView, self).get_context_data(**kwargs)
		context['closed_solicitations_by_year'] = self.get_solicitations()

		return context

	def get_solicitations(self):

		closed_solicitations_by_year = []

		solicitations = Solicitation.objects.filter(
			status=status[0]
		)

		for solicitation in solicitations:
			if solicitation.created_at.year == self.kwargs.get('sol_year'):
				closed_solicitations_by_year.append(solicitation)

		return closed_solicitations_by_year


class HomeDirectorView(TemplateView, LoginRequiredMixin):

	'''
	Home view for Director
	'''

	template_name = 'homedir.html'

	def get_context_data(self, **kwargs):

		context = super(HomeDirectorView, self).get_context_data(**kwargs)
		solicitations = Solicitation.objects.all()

		context['solicitations'] = solicitations

		return context


class AnalysisDirectorView(FormView, LoginRequiredMixin):

	'''
	View for Director fill his/her solicitation feedback
	'''
	
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

	'''
	Home View for coordination
	'''

	template_name = 'homecoord.html'

	def get_context_data(self, **kwargs):

		context = super(HomeCoordinationView, self).get_context_data(**kwargs)
		solicitations = Solicitation.objects.all()

		context['solicitations'] = solicitations

		return context


class AnalysisCoordinationView(FormView, LoginRequiredMixin):

	'''
	View for coordinator fill his/her feedback
	'''
	
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

class HomeCAAView(TemplateView, LoginRequiredMixin):

	template_name = 'homecaa.html'

	def get_context_data(self, **kwargs):

		context = super(HomeCAAView, self).get_context_data(**kwargs)
		solicitations = Solicitation.objects.all()

		context['solicitations'] = solicitations

		return context


class AnalysisCAAView(FormView, LoginRequiredMixin):
	
	template_name = 'caa_analysis.html'
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

		return HttpResponseRedirect(reverse('accounts:homecaa'))

	def get_context_data(self, **kwargs):

		context = super(AnalysisCAAView, self).get_context_data(**kwargs)
		solicitation = self.get_solicitation()
		context['solicitation'] = solicitation

		return context

	def get_solicitation(self):

		solicitation = Solicitation.objects.get(pk=self.kwargs.get('sol_id'))
		return solicitation


def change_status(request, sol_id, status_to):

	solicitation_status = status[status_to]

	solicitation = Solicitation.objects.get(pk=sol_id)
	solicitation.status = solicitation_status

	solicitation.save()

	return HttpResponseRedirect(reverse('accounts:homesecretaria'))

def logout(request):
	django_logout(request)
	return HttpResponseRedirect(reverse('core:index'))

def write_solicitation_to_docx(request, sol_id):

	solicitation = Solicitation.objects.get(pk=sol_id)
	new_write = WriteAndDownload(solicitation)

	new_write.write_file()
	response = new_write.download()

	return response

def download_attachment(request, sol_id, file):

	solicitation = Solicitation.objects.get(pk=sol_id)

	if file == 'rg':
		path_to_file = solicitation.attachment_rg
		name = solicitation.attachment_rg.name
	elif file == 'school_historic':
		path_to_file = solicitation.attachment_school_historic
		name = solicitation.attachment_school_historic.name
	elif file == 'academic_bond_certificate':
		path_to_file = solicitation.attachment_academic_bond_certificate
		name = solicitation.attachment_academic_bond_certificate.name
	elif file == 'discipline_menu':
		path_to_file = solicitation.attachment_discipline_menu
		name = solicitation.attachment_discipline_menu.name
	elif file == 'highschool_certificate':
		path_to_file = solicitation.attachment_highschool_certificate
		name = solicitation.attachment_highschool_certificate.name
	elif file == 'birth_marriage_certificate':
		path_to_file = solicitation.attachment_birth_marriage_certificate
		name = solicitation.attachment_birth_marriage_certificate.name
	elif file == 'degree':
		path_to_file = solicitation.attachment_degree
		name = solicitation.attachment_degree.name
	elif file == 'reservist':
		path_to_file = solicitation.attachment_reservist
		name = solicitation.attachment_reservist.name
	elif file == 'proof_electoral_discharge':
		path_to_file = solicitation.attachment_proof_electoral_discharge
		name = solicitation.attachment_proof_electoral_discharge.name
	elif file == 'cpf':
		path_to_file = solicitation.attachment_cpf
		name = solicitation.attachment_cpf.name

	with open("secretariavirtual/common-static/media/"+str(path_to_file), 'rb') as fh:
		response = HttpResponse(fh.read(), content_type="application/force-download")
		response['Content-Disposition'] = 'inline; filename=' + name

	return response