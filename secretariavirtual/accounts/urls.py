from django.contrib import admin
from django.urls import include, path
from .views import (
	HomeAlunoView, HomeSecretaryView, AnalysisSecretaryView,
	change_status, logout, HomeDirectorView, AnalysisDirectorView,
	AnalysisCoordinationView, HomeCoordinationView, HomeLibraryView,
	AnalysisLibraryView, HomeFinanceView, AnalysisFinanceView,
	HomeNapesView, AnalysisNapesView, StudentTrackSolicitationsView,
	ClosedSolicitationsView, ClosedSolicitationsByYearView, write_solicitation_to_docx,
	HomeCAAView, AnalysisCAAView
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
	path('home/secretaria/requerimentos-encerrados/',
		ClosedSolicitationsView.as_view(),
		name='closedsolicitations'
	),
	path('home/secretaria/requerimentos-encerrados/<int:sol_year>',
		ClosedSolicitationsByYearView.as_view(),
		name='closedsolicitationsbyyear'
	),
	path('home/secretaria/requerimentos-encerrados/imprimir/<int:sol_id>',
		write_solicitation_to_docx,
		name='writedocument'
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
	path('home/caa/',
		HomeCAAView.as_view(),
		name='homecaa'
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
	path('home/caa/analisarsolicitacao/<int:sol_id>',
		AnalysisCAAView.as_view(),
		name='caasolicitationanalysis'
	),
	path('home/secretaria/trocar-status/<int:sol_id>/<int:status_to>',
		change_status,
		name='changestatus'
	),

]