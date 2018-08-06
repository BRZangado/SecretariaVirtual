from django.contrib import admin
from django.urls import include, path
from .views import (
	HomeAlunoView, HomeSecretaryView, AnalysisSecretaryView,
	send_solitation_to
	)

app_name = 'accounts'

urlpatterns = [

	path('home/aluno/',
		HomeAlunoView.as_view(),
		name='homealuno'
	),
	path('home/secretaria/',
		HomeSecretaryView.as_view(),
		name='homesecretaria'
	),
	path('home/secretaria/analisarsolicitacao/<int:sol_id>',
		AnalysisSecretaryView.as_view(),
		name='secsolicitationanalysis'
	),
	path('home/secretaria/enviarsolicitacao/<int:sol_id>/<int:status_to>',
		send_solitation_to,
		name='enviarsolicitacao'
	),

]