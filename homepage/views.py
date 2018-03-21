from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class Login(TemplateView):
    def get(self, request, **kwargs):
            return render(request,'login.html', context=None)

class about_Us(TemplateView):
    def get(self, request, **kwargs):
            return render(request,'about_Us.html', context=None)

class contact_Us(TemplateView):
    def get(self, request, **kwargs):
            return render(request,'contact_us.html', context=None)