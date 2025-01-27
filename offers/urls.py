from django.urls import path

from offers.views import CityListView, IndexView

app_name = 'offers'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cities/', CityListView.as_view(), name='cities'),
]
