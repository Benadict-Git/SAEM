from django.shortcuts import render
from .models import Expense

def expenses_dashboard(request):
    expenses = Expense.objects.order_by('-date')
    total_spent = sum(exp.amount for exp in expenses)
    
    context = {
        'expenses': expenses,
        'total_spent': total_spent,
    }
    return render(request, 'finance/dashboard.html', context)
