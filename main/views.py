from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.forms import ProductForm
from main.models import Product


def home(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Skystore',
        'title_comments': 'Skystore - это отличный вариант выбора товара на любой вкус!'
    }
    return render(request, 'main/home.html', context)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'main/contacts.html')


class ProductListView(ListView):
    model = Product
    template_name = 'main/home.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product.html'

class ProductCreatelView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     CategoryFormset = inlineformset_factory(Product, form=ProductForm, extra=1)
    #     if self.request.method == 'POST':
    #         formset = CategoryFormset(self.request.POST)
    #     else:
    #         formset = CategoryFormset()
    #     context['formset'] = formset
    #     return context
    # def form_valid(self, form):
    #
    #     return super().form_valid(form)
    def get_success_url(self):
        return reverse('main:home')

class ProductUpdatelView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'

    def get_success_url(self):
        return reverse('main:product', args=[self.kwargs.get('pk')])

class ProductDeleteView(DeleteView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:home')
