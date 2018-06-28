from django.shortcuts import render, get_object_or_404, redirect
from .models import Operator, SIM, Guest
from .forms import Payment

# Create your views here.
def sim_list(request):
	list_viettel = SIM.objects.filter(operator = Operator.objects.get(Telcos='VIETTEL'))
	list_mobifone = SIM.objects.filter(operator = Operator.objects.get(Telcos='MOBIFONE'))
	list_vinaphone = SIM.objects.filter(operator = Operator.objects.get(Telcos='VINAPHONE'))
	return render(request,'SIM/sim_list.html',{'list_viettel':list_viettel, 'list_vinaphone':list_vinaphone, 'list_mobifone':list_mobifone})

def payment(request,pk):
	num_payment = get_object_or_404(SIM,pk=pk)
	if request.method == "POST":
		payment_form = Payment(request.POST)
		if payment_form.is_valid():
			GUEST = payment_form.save(commit=False)
			GUEST.number_pay = num_payment.number
			GUEST.save()
			return redirect('payment_submit', pk=GUEST.pk)
	else:
		payment_form = Payment()
	return render(request, 'SIM/payment.html',{'payment_form':payment_form})

def payment_submit(request,pk):
	return render(request, 'SIM/payment_submit.html',{})