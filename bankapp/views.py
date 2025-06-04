from django.shortcuts import render
from django.http import JsonResponse
from .models import Bank, Branch

def home(request):
    return render(request, 'bankapp/home.html')
def bank_list(request):
    banks = Bank.objects.all()
    data = []
    for bank in banks:
        branches = bank.branches.all()  # Use related_name='branches' if set in models, else use branch_set.all()
        branch_list = []
        for branch in branches:
            branch_list.append({
                'ifsc': branch.ifsc,
                'branch': branch.branch,  # use 'branch', not 'branch_name'
            })
        data.append({
            'name': bank.name,
            'branches': branch_list,
        })
    return JsonResponse(data, safe=False)

def branch_detail(request, ifsc):
    try:
        branch = Branch.objects.get(ifsc=ifsc)
        data = {
            'bank_name': branch.bank.name,
            'branch': branch.branch,  # use 'branch' here too
            'ifsc': branch.ifsc,
            'address': branch.address,
        }
        return JsonResponse(data)
    except Branch.DoesNotExist:
        return JsonResponse({'error': 'Branch not found'}, status=404)
