# howdy/urls.py
from django.conf.urls import url, include
from homepage import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'login.html',views.Login.as_view()),
    url(r'contact_Us.html',views.contact_Us.as_view()),
    url(r'about_Us.html',views.about_Us.as_view()),
    url(r'render_Page.html', views.render_Page.as_view())
]