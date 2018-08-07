from django.contrib import admin
from django.urls import include, path
from .views import (
	HomeAlunoView, HomeSecretaryView, AnalysisSecretaryView,
	send_solitation_to, logout, HomeDirectorView, AnalysisDirectorView,
	AnalysisCoordinationView, HomeCoordinationView, HomeLibraryView,
	AnalysisLibraryView
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
	path('home/diretoria/',
		HomeDirectorView.as_view(),
		name='homediretoria'
	),
	path('home/coordenacao/',
		HomeCoordinationView.as_view(),
		name='homecoordination'
	),
	path('home/biblioteca/',
		HomeLibraryView.as_view(),
		name='homelibrary'
	),
	path('home/logout/',
		logout,
		name='logout'
	),
	path('home/secretaria/analisarsolicitacao/<int:sol_id>',
		AnalysisSecretaryView.as_view(),
		name='secsolicitationanalysis'
	),
	path('home/diretoria/analisarsolicitacao/<int:sol_id>',
		AnalysisDirectorView.as_view(),
		name='dirsolicitationanalysis'
	),
	path('home/coordenacao/analisarsolicitacao/<int:sol_id>',
		AnalysisCoordinationView.as_view(),
		name='coordsolicitationanalysis'
	),
	path('home/biblioteca/analisarsolicitacao/<int:sol_id>',
		AnalysisLibraryView.as_view(),
		name='libsolicitationanalysis'
	),
	path('home/secretaria/enviarsolicitacao/<int:sol_id>/<int:status_to>',
		send_solitation_to,
		name='enviarsolicitacao'
	),

]