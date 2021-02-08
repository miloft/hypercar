from collections import deque

from django.db import models


class Queue:
    def __init__(self):
        self.services = {
            'change_oil': dict(time=2, queue=deque()),
            'inflate_tires': dict(time=5, queue=deque()),
            'diagnostic': dict(time=30, queue=deque())
        }
        self.ticket_number = 0
        self.next_ticket = None
        
    def get_counters(self):
        return {key: len(self.services[key]['queue']) for key in self.services}

    def get_time(self, service, ticket_number):
        time = 0

        for i in self.services:
            time += self.services[i]['time'] * len(self.services[i]['queue'])
            if i == service:
                break

        # update queue
        self.services[service]['queue'].appendleft(ticket_number)

        return time

    def get_ticket_number(self):
        self.ticket_number += 1
        return self.ticket_number

    def get_next_ticket(self):
        self.next_ticket = None
        for i in self.services:
            if len(self.services[i]['queue']):
                self.next_ticket = self.services[i]['queue'].pop()
                break
            else:
                continue
