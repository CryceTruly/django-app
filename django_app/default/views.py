from django.shortcuts import render
from django.views import View
from django.http import response
# Create your views here.


class DefaultView(View):
    def get(self, request):
        return response.HttpResponse("Hello world")
