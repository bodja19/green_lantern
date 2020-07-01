from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from common.forms import LoginForm


class LoginView(View):
    def get(self, request):
        return render(request, 'log_page.html', {'log_form': LoginForm()})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request,
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'],
                                )

            if user:
                login(request, user)
                return HttpResponseRedirect('/admin/')
            return render(request, 'log_page.html', {'form':form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
