from core.views import ConditionPageView, IndexPageView, contact, CarPageView
from django.urls import path


urlpatterns = [
    path('',IndexPageView.as_view(),name='index'),
    path('condition/',ConditionPageView.as_view(),name='condition'),
    path('contact/',contact,name='contact'),
    path('car/',CarPageView.as_view(),name='car'),
]
