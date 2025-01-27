from django.views.generic import ListView

from offers.models import City, Offer


class IndexView(ListView):
    model = Offer
    template_name = 'offers/index.html'
    context_object_name = 'offers'

    def get_queryset(self):
        return Offer.objects.select_related('city__region', 'author').all()


class CityListView(ListView):
    model = City
    template_name = 'offers/cities.html'
    context_object_name = 'cities'

    def get_queryset(self):
        return City.objects.select_related('region').all()

