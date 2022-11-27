from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets, permissions
from rest_framework.decorators import action

from .filters import AdFilter
from .models import Ad,Comment
from .serializers import AdSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter
    serializer_class = AdSerializer

    def get_queryset(self):
        if self.action == 'me':
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create', 'me']:
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

    @action(detail=False, methods=['get'])
    def me(self,request, *args,**kwargs):
        return super().list(self,request, *args,**kwargs)
class CommentViewSet(viewsets.ModelViewSet):
    # queryset = Comment.objects.all()
    # permission_classes=
    pass

