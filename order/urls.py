from .views import OrderPageView,detail
from django.urls import path


urlpatterns = [
    path('',OrderPageView.as_view(),name='order'),
    path('<int:pk>/',detail,name='detail'),
]