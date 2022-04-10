from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import TransactionForm


# Create your views here.

def home(request):
    return render(request, "broker/home.html")


@login_required()
def tarnsactionslist(request):
    if request.user.is_superuser:
        transactions_list = Transaction.objects.values('national_id', 'branch', 'transaction_value')
        for obj in list(transactions_list):
            obj['transaction_fee'] = obj['transaction_value'] * 0.1
            obj.pop('transaction_value')
        return JsonResponse(list(transactions_list), safe=False)
    else:
        transactions_list = Transaction.objects.filter(branch=request.user.branch).values('national_id', 'branch',
                                                                                          'transaction_value')
        for obj in list(transactions_list):
            obj['transaction_fee'] = obj['transaction_value'] * 0.1
            obj.pop('transaction_value')
        return JsonResponse(list(transactions_list), safe=False)


def create_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/create_transaction")
    else:
        form = TransactionForm()
        return render(request, "broker/create_transaction.html", {'form': form})