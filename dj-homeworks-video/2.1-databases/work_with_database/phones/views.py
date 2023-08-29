from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    rez = request.GET.get('sort')
    template = 'catalog.html'
    phone = Phone.objects.all()
    list_ = ['name','min_price','max_price']

    context = {'phones': phone.order_by(('name','price','-price')[list_.index(rez)]) if rez else phone}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)
    context = {'phones': phone}
    return render(request, template, context)
