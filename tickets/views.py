from functools import wraps

from django.core.cache import caches

from .models import Ticket
from rest_framework.viewsets import ModelViewSet
from .serializers import TicketSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.viewsets import ModelViewSet


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(300))
    def dispatch(self, *args, **kwargs):
        return super(TicketViewSet, self).dispatch(*args, **kwargs)
