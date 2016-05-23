import datetime
from haystack import indexes
from pesquisador.models import Empresa


class EmpresaIndex(indexes.SearchIndex, indexes.Indexable):
	"""docstring for NoteIndex"""
	nome = indexes.CharField(document=True, use_template=True)

	def get_model(self):
		return Empresa

