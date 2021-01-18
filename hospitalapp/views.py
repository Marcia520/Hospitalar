from django.shortcuts import render
from django.http import HttpResponse
from .forms import Hospitalform

# Create your views here.
def index(request):
    #return HttpResponse("<h1>Aqui é o index<h1>")
    return render(request, 'hospital/index.html')

def hospital(request):
    #return HttpResponse("<h1>Aqui é a área de hospital<h1>")
	return render(request, 'hospital/hospital.html')


def criar_hospitais (request):
	form = Hospitalform(request.POST)
	if request.method == "POST":
		form = Hospitalform(request.POST,request.FILES)
	if form.is_valid():
		hosp = form.save()
		hosp.save()
		form =Hospitalform()
	return render(request,'hospital/criar_hospitais.html',{'form': form})
	