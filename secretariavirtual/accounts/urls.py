from django.contrib import admin
from django.urls import include, path
from .views import (
	HomeAlunoView, HomeSecretaryView, AnalysisSecretaryView,
	send_solitation_to, logout, HomeDirectorView, AnalysisDirectorView,
	AnalysisCoordinationView, HomeCoordinationView, HomeLibraryView,
	AnalysisLibraryView, HomeFinanceView, AnalysisFinanceView,
	HomeNapesView, AnalysisNapesView, StudentTrackSolicitationsView
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
	path('home/financeiro/',
		HomeFinanceView.as_view(),
		name='homefinance'
	),
	path('home/napes/',
		HomeNapesView.as_view(),
		name='homenapes'
	),
	path('home/logout/',
		logout,
		name='logout'
	),
	path('home/aluno/acompanharsolicitacao/',
		StudentTrackSolicitationsView.as_view(),
		name='mysolicitations'
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
	path('home/financeiro/analisarsolicitacao/<int:sol_id>',
		AnalysisFinanceView.as_view(),
		name='finsolicitationanalysis'
	),
	path('home/napes/analisarsolicitacao/<int:sol_id>',
		AnalysisNapesView.as_view(),
		name='napessolicitationanalysis'
	),
	path('home/secretaria/enviarsolicitacao/<int:sol_id>/<int:status_to>',
		send_solitation_to,
		name='enviarsolicitacao'
	),

]