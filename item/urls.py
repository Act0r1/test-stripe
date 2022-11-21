from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('item/<int:item_id>', views.item, name='item'),
    path('config/', views.stripe_config),
    path('create_checkout_session/', views.create_checkout_session),
    path('success/', views.SuccessPage.as_view()),
    path('stripe_webhook/', views.stripe_webhook),
    path('cancel/', views.CancellPage.as_view()),
]


