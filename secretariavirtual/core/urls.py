from django.contrib import admin
from django.urls import include, path
from secretariavirtual.core.views import LoginView

app_name = 'core'

urlpatterns = [
	path('', LoginView.as_view(), name='index'),
	path('accounts/', include('secretariavirtual.accounts.urls')),
]