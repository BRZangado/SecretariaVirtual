from django.contrib import admin
from django.urls import include, path
from secretariavirtual.core.views import LoginView, LoginViewAuthError

app_name = 'core'

urlpatterns = [
	path('', LoginView.as_view(), name='index'),
	path('authentication-error/', LoginViewAuthError.as_view(), name='indexerror'),
	path('accounts/', include('secretariavirtual.accounts.urls'), name="accounts"),
]