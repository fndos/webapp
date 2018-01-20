from django.shortcuts import render
import requests as r

# Create your views here.
def index(request):
    template='noticias/noticias.html'
    return render(request,template)

def mostrar10(request):
	template = 'noticias/10mejores.html'
	result = r.get('http://localhost:9000')
	noticias = result.json()
	print (noticias)
	lista=[]
	for k, v in noticias.items():
		lista.append((k,v))
	print(lista)
	return render(request, template, {'noticias': lista })

def mostrar10db(request):
	template = 'noticias/10mejores.html'
	result = r.get('http://localhost:9000/justdb')
	noticias = result.json()
	print (noticias)
	lista=[]
	for k, v in noticias.items():
		lista.append((k,v))
	print(lista)
	return render(request, template, {'noticias': lista })