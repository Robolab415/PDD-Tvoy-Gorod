from django.shortcuts import render
from django.views import generic

from django.conf import settings
from .models import Ticket


def render_simple_page(request, page_name, title):
    return render(
        request,
        'pages/'+page_name+'.html',
        context={'menu_links': settings.MENU_LINKS, 'title': title }
    )

def index(request):
    return render_simple_page(request, 'index', settings.SITE_NAME)

def error(request):
    return render_simple_page(request, 'index', "Заглушка")

class TicketListView(generic.ListView):
    model = Ticket
    template_name = 'pages/tickets.html'

    def get_context_data(self, **kwargs):
        context = super(TicketListView, self).get_context_data(**kwargs)
        context['menu_links'] = settings.MENU_LINKS
        context['title'] = 'Билеты'
        return context

class TicketDetailView(generic.DetailView):
    model = Ticket
    template_name = 'pages/ticket.html'

    def get_context_data(self, **kwargs):
        context = super(TicketDetailView, self).get_context_data(**kwargs)
        context['menu_links'] = settings.MENU_LINKS
        context['title'] = self.__str__
        return context
