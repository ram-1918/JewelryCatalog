from django.urls import path
from products import views

urlpatterns = [
    path("category/", views.listCategoryView.as_view()),
    path("gold-price/", views.createGoldPriceView.as_view()),
    path("update-gold-price/<int:pk>", views.updateGoldPriceView.as_view()),
    path("details/", views.listProductsView.as_view()),
    path("details/<int:pk>", views.getProductsView.as_view()),
    path("with-prices/", views.listPriceView.as_view()),
    path("with-prices/<int:pk>", views.getPriceView.as_view()),
]