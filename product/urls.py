from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'product'

urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    # navbar
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('capabilites/', views.capability, name='capability'),
    # footer
    path('company/', views.company, name='company'),
    path('quality/', views.quality, name='quality'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.website, name='website'),
    path('terms-of-sales/', views.terms_sales, name='terms_sales'),
    path('purchase-terms/', views.purchase_terms, name='purchase_terms'),
    path('anti-bribery/', views.anti_bribery, name='anti_bribery'),
    path('environmental-policy/', views.environmental, name='environmental'),
    path('equal-opportunities/', views.equal_opportunities, name='equal_opportunities'),
    path('health-safety/', views.health, name='health'),
    path('obsolescence/', views.obsolescence, name='obsolescence'),
    path('risk-management/', views.risk_management, name='risk_management'),
    path('products/', views.products, name='products'),
    path('categories/<int:id>', views.category, name='category'),
    path('detail32&-1r34/<int:id>', views.product_detail, name='product_detail'),
]