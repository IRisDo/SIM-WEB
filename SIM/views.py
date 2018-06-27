from django.shortcuts import render

# Create your views here.
def sim_list(request):
	return render(request,'SIM/sim_list.html',{})