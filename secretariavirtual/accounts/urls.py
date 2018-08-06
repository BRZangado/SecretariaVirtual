from django.contrib import admin
from django.urls import include, path
from .views import (
	HomeAlunoView, HomeSecretaryView, AnalysisSecretaryView,
	send_solitation_to_bib, send_solitation_to_napes, send_solitation_to_finance,
	send_solitation_to_direct, send_solitation_to_coord
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
	path('home/secretaria/enviarsolicitacaobib/<int:sol_id>',
		send_solitation_to_bib,
		name='enviarsolicitacaobib'
	),
	path('home/secretaria/enviarsolicitacaonapes/<int:sol_id>',
		send_solitation_to_napes,
		name='enviarsolicitacaonapes'
	),
	path('home/secretaria/enviarsolicitacaofin/<int:sol_id>',
		send_solitation_to_finance,
		name='enviarsolicitacaofin'
	),
	path('home/secretaria/enviarsolicitacaodirect/<int:sol_id>',
		send_solitation_to_direct,
		name='enviarsolicitacaodirect'
	),
	path('home/secretaria/enviarsolicitacaocoord/<int:sol_id>',
		send_solitation_to_coord,
		name='enviarsolicitacaocoord'
	),

]