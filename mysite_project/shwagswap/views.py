from django.views import generic
from .models import Shwag, Transaction
from django.shortcuts import render


class ShwagTakeView(generic.ListView):
    template_name = 'shwagswap/take.html'
    queryset = Shwag.objects.all
    context_object_name = 'sought_out_shwag'


class ShwagDealsView(generic.ListView):
    template_name = 'shwagswap/transactions.html'
    queryset = Transaction.objects.all
    context_object_name = 'transactions'


class EmailAuthorView(generic.ListView):
    template_name = 'shwagswap/transactions.html'
    queryset = Transaction.objects.all
    context_object_name = 'transactions'

    def post(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        render(request, self.template_name, {})
