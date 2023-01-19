from django.shortcuts import render

# Create your views here.


def index(resquest):
    return render(resquest, 'expenses/index.html')


def add_expense(resquest):
    return render(resquest, 'expenses/add_expenses.html')
