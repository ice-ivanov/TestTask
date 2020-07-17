from django.db import models


# class Position(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name


class Responsible(models.Model):
    fio = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.fio


class Client(models.Model):
    fio = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.fio


class Ticket(models.Model):
    responsible = models.ForeignKey(Responsible, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
