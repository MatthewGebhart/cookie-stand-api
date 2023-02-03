from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CookieStand
from .serializers import StandSerializer
from .permissions import IsOwnerOrReadOnly

class StandList(ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = StandSerializer


class StandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = StandSerializer
