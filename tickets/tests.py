import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Ticket, Responsible, Client
from .serializers import TicketSerializer


client = Client()


class GetAllTicketsTest(TestCase):
    def setUp(self):
        resp1 = Responsible.objects.create(fio='resp-fio1', position='pos1')
        cli1 = Client.objects.create(fio='cli-fio1', phone='+11111111')
        Ticket.objects.create(text='some text', responsible=resp1, client=cli1)

        resp2 = Responsible.objects.create(fio='resp-fio2', position='pos2')
        cli2 = Client.objects.create(fio='cli-fio2', phone='+11111111')
        Ticket.objects.create(text='some text', responsible=resp2, client=cli2)

    def test_get_all_tickets(self):
        response = client.get(reverse('get_post_tickets'))
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
