# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views.generic import TemplateView
from cart.forms import CartAddProductForm

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'home.html', context=None)

class Login(TemplateView):
    def get(self, request, **kwargs):
            return render(request,'login.html', context=None)

class Profile(TemplateView):
    def get(self, request, **kwargs):
            return render(request,'profile.html', context=None)

class about_Us(TemplateView):
    def get(self, request, **kwargs):
            return render(request,'about_Us.html', context=None)

class contact_Us(TemplateView):
    def get(self, request, **kwargs):
            return render(request,'contact_Us.html', context=None)
class render_Page(TemplateView):
    def get(self, request, **kwargs):
            return render(request,'render_Page.html', context=None)

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})