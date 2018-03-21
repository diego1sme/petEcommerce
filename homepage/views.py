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
class render_Page(TemplateView):
    def get(self, request, **kwargs):
            return render(request,'render_Page.html', context=None)

def post_list(request):
    today = timezone.now().date()
    queryset_list = Post.objects.active()
    query = request.Get.get("q")
    if query:
        queryset_list = queryset_list.filter(title_icontains=query)