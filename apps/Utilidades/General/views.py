from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class homeView(View):
    def get(self, request):
        return render(request, 'home.html')