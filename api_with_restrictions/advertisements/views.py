from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.filters import AdvertisementFilter

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    filterset_fields = ['creator', 'status', 'created_at']

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []
