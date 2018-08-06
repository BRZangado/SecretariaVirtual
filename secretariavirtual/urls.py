from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('secretariavirtual.core.urls'), name="core"),
	path('', include('secretariavirtual.accounts.urls'), name="accounts"),
    path('admin/', admin.site.urls),
]
