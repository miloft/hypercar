from django.conf.urls.static import static
from django.urls import path

from hypercar import settings
from tickets.views import WelcomeView, MenuView, TicketView, OperatorView, TableView
from django.views.generic.base import RedirectView

urlpatterns = [
    path('welcome/', WelcomeView.as_view(), name='welcome'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('get_ticket/<str:service>', TicketView.as_view(), name='ticket'),

    path('processing/', RedirectView.as_view(url='/processing')),
    path('processing', OperatorView.as_view(), name='operator'),

    path('next/', RedirectView.as_view(url='/next')),
    path('next', TableView.as_view(), name='next_ticket'),

    path('', RedirectView.as_view(url='welcome/'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
