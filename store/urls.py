from django.urls import path
from .views import ProductListView

urlpatterns = [
    path('store/',ProductListView.as_view()),
]
