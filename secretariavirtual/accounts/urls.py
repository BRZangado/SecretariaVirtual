from django.contrib import admin
from django.urls import include, path
from .views import HomeAlunoView

app_name = 'accounts'

urlpatterns = [
	path('home/aluno/', HomeAlunoView.as_view(), name='homealuno'),

]