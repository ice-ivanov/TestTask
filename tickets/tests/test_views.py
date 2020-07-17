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

    def test_movie_creation(self):
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

        # assert new movie was added
        self.assertEqual(Ticket.objects.count(), 2)

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)

    # def test_getting_movies(self):
    #     response = self.cli.get(reverse('movies'), format="json")
    #     self.assertEqual(len(response.data), 1)
    #
    # def test_updating_movie(self):
    #     response = self.cli.put(reverse('detail', kwargs={'pk': 1}), {
    #         'name': 'The Space Between Us updated',
    #         'year_of_release': 2017
    #     }, format="json")
    #
    #     # check info returned has the update
    #     self.assertEqual('The Space Between Us updated', response.data['name'])
    #
    # def test_deleting_movie(self):
    #     response = self.cli.delete(reverse('detail', kwargs={'pk': 1}))
    #
    #     self.assertEqual(204, response.status_code)
