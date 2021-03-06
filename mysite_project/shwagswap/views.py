from django.views import generic
from .models import Shwag, Transaction
from django.shortcuts import render


class ShwagTakeView(generic.ListView):
    template_name = "shwagswap/take.html"
    context_object_name = "sought_out_shwag"

    def get_queryset(self):
        return Shwag.objects.all


class ShwagDealsView(generic.ListView):
    template_name = "shwagswap/transactions.html"
    context_object_name = "transactions"

    def get_queryset(self):
        return Transaction.objects.all


class EmailAuthorView(generic.ListView):
    template_name = "shwagswap/transactions.html"
    context_object_name = "transactions"

    def get_queryset(self):
        return Transaction.objects.all

    def post(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        render(request, self.template_name, {})
