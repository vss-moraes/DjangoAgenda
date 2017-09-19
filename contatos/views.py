from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Contato

# Create your views here.
def main_contatos(request):
    if request.method == 'POST':
        novo_nome = request.POST.get("nome")
        novo_telefone = request.POST.get("telefone")
        contato = Contato(nome=novo_nome, telefone=novo_telefone)
        contato.save()

        return HttpResponseRedirect('/contatos/')

    contatos = Contato.objects.all()
    return render(request, 'contatos.html', { 'contatos': contatos})

def deletar(request, contato_id):
    contato = Contato.objects.get(pk=contato_id)
    contato.delete()
    return HttpResponseRedirect('/contatos/')
