from django.urls import path
from .views import *

app_name = "groceryapp"
urlpatterns = [
    path("base/", BaseView.as_view(), name="home"),
    path("category/", AboutView.as_view(), name="category"),
    path("", HomeView.as_view(), name="Home"),
    path("all-product/", AllProductView.as_view(), name="allproducts"),
    path("product/<slug:slug>/", ProdectDetailView.as_view(), name="productdetail"),
    path("add-to-card<int:pro_id>/", AddToCartView.as_view(), name="addtocard"),
    path("my-cart/", MyCartView.as_view(), name="mycart"),
    path("manage-cart/<int:cp_id>/",ManageCartView.as_view(),name="managecart"),
    path("empty-cart/", EmptyCartView.as_view(), name="emptycart"),
    path("checkout/", CheckoutView.as_view(), name="checkout1"),


]
