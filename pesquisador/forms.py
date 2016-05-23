from django import forms
from pesquisador.models import Empresa


class EmpresaForm(forms.ModelForm):			
	class Meta:
		model = Empresa
		fields = ('nome','tipo')


			

			