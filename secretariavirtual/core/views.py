# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _
from django.http.response import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import FormView

# Application imoports
from secretariavirtual.core.forms import LoginForm

# Get the custom user from settings
User = get_user_model()

class LoginView(FormView):

    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        """
        Receive the form already validated.
        Logs the user into the system.
        """

        # Get the user saved by form.
        username = form.cleaned_data['login']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            if user.usuario.is_student:
                return HttpResponseRedirect(reverse('accounts:homealuno'))
            elif user.usuario.is_secretary:
                return HttpResponseRedirect(reverse('accounts:homesecretaria'))
            elif user.usuario.is_director:
                return HttpResponseRedirect(reverse('accounts:homediretoria'))
            elif user.usuario.is_coordination:
                return HttpResponseRedirect(reverse('accounts:homecoordination'))
            elif user.usuario.is_library:
                return HttpResponseRedirect(reverse('accounts:homelibrary'))
            elif user.usuario.is_finance:
                return HttpResponseRedirect(reverse('accounts:homefinance'))
            elif user.usuario.is_napes:
                return HttpResponseRedirect(reverse('accounts:homenapes'))
        else:
            return HttpResponseRedirect(reverse('accounts:invalid'))


