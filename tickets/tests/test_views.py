from django.shortcuts import reverse

from rest_framework.test import APITestCase

from ..models import Ticket, Responsible, Client


class TestTicketApi(APITestCase):
    def setUp(self):
        self.resp = Responsible(fio='resp1', position='pos1')
        self.resp.save()
        self.cli = Client(fio='cli1', phone='+123456')
        self.cli.save()
        self.ticket = Ticket(text="Some text here", responsible=self.resp, client=self.cli)
        self.ticket.save()

    def test_tickets_creation(self):
        response = self.client.post(reverse('tickets'), {
            'text': 'come text here',
            'responsible': {
                'fio': 'resp_test',
                'position': 'position_test'
            },
            'client': {
                'fio': 'client_test',
                'phone': '+123456'
            }
        })
        self.assertEqual(Ticket.objects.count(), 2)
        self.assertEqual(201, response.status_code)

    def test_getting_tickets(self):
        response = self.client.get(reverse('tickets'), format="json")
        self.assertEqual(len(response.data), 1)

    def test_updating_movie(self):
        response = self.client.put(reverse('detail', kwargs={'pk': 1}), {
            'text': 'some new text',
        }, format="json")
        self.assertEqual('some new text', response.data['text'])

    def test_deleting_tickets(self):
        response = self.client.delete(reverse('detail', kwargs={'pk': 1}))
        self.assertEqual(204, response.status_code)
