from django.shortcuts import render,redirect
from dryclean.models import feedback , order ,pricing,login
from dryclean.forms import feedbackform , orderform ,pricingform,loginform
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User
from cart.forms import CartAddProductForm


# Create your views here.
class demoview(TemplateView):
    template_name="demo.html"
class aboutview(TemplateView):
    template_name="about.html"
class homeview(TemplateView):
    template_name="home.html"
class pageview(TemplateView):
    template_name="page.html"
class homelaundry(TemplateView):
    template_name="homelaundry.html"
class ourblogview(TemplateView):
    template_name="ourblog.html"
class feedbackview(TemplateView):
    template_name="feedback.html"
class pagesview(TemplateView):
    template_name="pages.html"
class demoprojectview(TemplateView):
    template_name="demoproject.html"  
class servicesview(TemplateView):
    template_name="services.html"
class about1view(TemplateView):
    template_name="about1.html"
class formview(TemplateView):
    template_name="form.html"
class orderview(TemplateView):
    template_name="order.html"
class practiceview(TemplateView):
    template_name="practice.html"
class cartdetailview(TemplateView):
    template_name="cartdetail.html"
class paymentview(TemplateView):
    template_name="payment.html"
class loginview(TemplateView):
    template_name="login.html"


def product_list(request):
    products = pricing.objects.all()  
    cart_product_form = CartAddProductForm()
    context = {
        'products': products,
        'cart_product_form': cart_product_form
    }
    return render(request, 'pricing.html', context)    
    
    
    
    
    
def insert(request):
    if request.method=='POST':
        form=feedbackform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/feedback/')
            except:
                pass
        else:
            form=feedbackform()
        return render(request,'feedback.html',{'form':form})
        

       
    
def insertorder(request):
    if request.method=='POST':
        form=orderform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/order/')
            except:
                pass
        else:
            form=orderform()
        return render(request,'order.html',{'form':form})
        
def insert(request):
    if request.method=='POST':
        form=loginform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/login/')
            except:
                pass
        else:
            form=loginform()
        return render(request,'login.html',{'form':form})