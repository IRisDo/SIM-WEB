from django.shortcuts import render
from .models import Operator, SIM
# Create your views here.
def sim_list(request):
	list_viettel = SIM.objects.filter(operator = Operator.objects.get(Telcos='VIETTEL'))
	list_mobifone = SIM.objects.filter(operator = Operator.objects.get(Telcos='MOBIFONE'))
	list_vinaphone = SIM.objects.filter(operator = Operator.objects.get(Telcos='VINAPHONE'))
	return render(request,'SIM/sim_list.html',{'list_viettel':list_viettel, 'list_vinaphone':list_vinaphone, 'list_mobifone':list_mobifone})