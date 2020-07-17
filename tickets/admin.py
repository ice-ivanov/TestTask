from django.contrib import admin
from .models import Responsible, Client, Ticket


# @admin.register(Position)
# class PositionAdmin(admin.ModelAdmin):
#     list_display = ('name',)


@admin.register(Responsible)
class ResponsibleAdmin(admin.ModelAdmin):
    list_display = ('fio', 'position')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('fio', 'phone')


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('date', 'id', 'responsible', 'client', 'text')
