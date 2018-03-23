# howdy/urls.py
from django.conf.urls import url, include
from homepage import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'home.html$', views.HomePageView.as_view()),
    url(r'login.html',views.Login.as_view()),
    url(r'contact_Us.html',views.contact_Us.as_view()),
    url(r'about_Us.html',views.about_Us.as_view()),
    url(r'profile.html',views.Profile.as_view()),
    url(r'render_Page.html$', views.product_list, name='product_list'),
    url(r'render_Page.html(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    url(r'render_Page.html(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
]