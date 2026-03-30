from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q

from landing.models import Brand, CarModel, Category, Good, Images


class LandingView(TemplateView):
    template_name = 'landing/Blackline/html/landing.html'

class CarModelCatalogView(ListView):
    template_name = 'landing/Blackline/html/model_list.html'
    def get_queryset(self):
        global brand
        brand = Brand.objects.get(id=self.kwargs['brand_pk'])
        queryset = CarModel.objects.filter(brand=brand)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['brand'] = brand
        return context

class CategoryListPage(ListView):
    template_name = 'landing/Blackline/html/category_list.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand_pk'] = self.kwargs['brand_pk']
        context['model_pk'] = self.kwargs['model_pk']
        return context



class GoodCatalogPage(ListView):
    template_name = 'landing/Blackline/html/goods_list.html'
    model = Good

    def get_queryset(self):
        category = Category.objects.get(id=self.kwargs['cat_pk'])
        brand = Brand.objects.get(id=self.kwargs['brand_pk'])
        car_model = CarModel.objects.get(id=self.kwargs['model_pk'])
        queryset = Good.objects.filter(Q(category=category) & Q(brand=brand) & Q(car_model=car_model))
        return queryset


class GoodPageView(DetailView):
    template_name = 'landing/Blackline/html/cardPage.html'
    model = Good

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['images'] = Images.objects.filter(good=self.get_object().pk)
        return context


