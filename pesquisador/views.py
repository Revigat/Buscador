from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt # import usado para retirar a proteção CSRF do django
from pesquisador.forms import EmpresaForm
from pesquisador.models import *

# Create your views here.

@csrf_exempt
def index(request):

	if request.method == "POST":

		nome_empresa = request.POST['nome'] # recupera o que foi digitado

		aEmpresa = Empresa.objects.filter(nome = nome_empresa) # faz pesquisa no banco
		
		return render_to_response('teste.html',{'aEmpresa' : aEmpresa})

	form = EmpresaForm()
	return render_to_response('pesquisa.html',{'form' : form})





	


