from django.shortcuts import redirect, render
from .models import Bank

# Create your views here.
def index(request):
    
    context = {
        "users" : Bank.objects.all(),
        "all_info" : Bank.objects.all()
    }
    
    return render(request, 'start.html', context)

def create_acount(request):
    tmp_bank = Bank()
    tmp_bank.user = request.POST['username']
    tmp_bank.email = request.POST['user_email']
    tmp_bank.phonenum = request.POST['phonenum']
    tmp_bank.balance = request.POST['balance']
    
    tmp_bank.save()
    
    return redirect('/')