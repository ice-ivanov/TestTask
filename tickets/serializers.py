from .models import Responsible, Client, Ticket
from rest_framework import serializers


class ResponsibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsible
        fields = ('id', 'fio', 'position')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'fio', 'phone')


class TicketSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    responsible = ResponsibleSerializer()
    client = ClientSerializer()

    class Meta:
        model = Ticket
        fields = ('id', 'text', 'date', 'responsible', 'client')

    def create(self, validated_data):
        responsible_data = validated_data.pop('responsible')
        # Checking if such Responsible already exists
        if Responsible.objects.filter(fio=responsible_data['fio']):
            validated_data['responsible'] = Responsible.objects.filter(fio=responsible_data['fio']).first()
        else:   # If not, creating a new one
            responsible_serializer = self.fields['responsible']
            responsible = responsible_serializer.create(responsible_data)
            responsible_id = responsible.id
            validated_data['responsible'] = Responsible.objects.filter(id=responsible_id).first()

        client_data = validated_data.pop('client')
        # Checking if such Client already exists
        if Client.objects.filter(fio=client_data['fio'], phone=client_data['phone']):
            validated_data['client'] = Client.objects.filter(fio=client_data['fio'], phone=client_data['phone']).first()
        else:   # If not, creating a new one
            client_serializer = self.fields['client']
            client = client_serializer.create(client_data)
            client_serializer.create(client_data)
            client_id = client.id
            validated_data['client'] = Client.objects.filter(id=client_id).first()

        ticket = Ticket.objects.create(**validated_data)
        return ticket

    def update(self, instance, validated_data):
        # Update the Foo instance
        instance.text = validated_data['text']
        instance.save()
        return instance
