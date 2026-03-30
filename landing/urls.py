from django.urls import path
from .views import *

urlpatterns = [
    path('', LandingView.as_view(), name='landing_view'),
    path('brand/<int:brand_pk>/', CarModelCatalogView.as_view(), name='brand_view'),
    path('brand/<int:brand_pk>/model/<int:model_pk>/', CategoryListPage.as_view(), name='modelcatalog_view'),
    path('brand/<int:brand_pk>/model/<int:model_pk>/category/<int:cat_pk>/', GoodCatalogPage.as_view(), name='goods_list'),
    path('good/<int:pk>/', GoodPageView.as_view(), name='good_detail'),
]