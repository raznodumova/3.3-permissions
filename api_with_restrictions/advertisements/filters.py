from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры

    created_at = filters.DateTimeFilter(field_name="created_at", lookup_expr='gt')
    status = filters.ChoiceFilter(field_name="status")

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']
