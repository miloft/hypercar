from django.views import View
from django.shortcuts import render, redirect

from tickets.models import Queue


class WelcomeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'tickets/index.html')


class MenuView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'tickets/menu.html')


queue = Queue()


class TicketView(View):

    def get(self, request, service, *args, **kwargs):
        ticket_number = queue.get_ticket_number()
        return render(
            request=request,
            template_name='tickets/ticket.html',
            context={
                'ticket_number': ticket_number,
                'time': queue.get_time(service, ticket_number)
            }
        )


class OperatorView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request=request,
            template_name='tickets/operator_menu.html',
            context=queue.get_counters()
        )

    def post(self, request, *args, **kwargs):
        queue.get_next_ticket()
        return redirect('next/')


class TableView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request=request,
            template_name='tickets/table.html',
            context={
                'next_ticket': queue.next_ticket
            }
        )