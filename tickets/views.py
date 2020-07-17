from .models import Ticket
from rest_framework import viewsets, generics
from .serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
