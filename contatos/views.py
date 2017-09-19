from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Contato

# Create your views here.
def main_contatos(request):
    if request.method == 'POST':
        try:
            novo_nome = request.POST.get("nome")
            novo_telefone = request.POST.get("telefone")
            contato = Contato(nome=novo_nome, telefone=novo_telefone)
            contato.save()
            messages.success(request, "Contato adicionado com sucesso!")
        except:
            messages.warning(request, "Ocorreu um problema ao adicionar o contato.")
        finally:
            return HttpResponseRedirect('/contatos/')

    contatos = Contato.objects.all()
    return render(request, 'contatos.html', { 'contatos': contatos})

def deletar(request, contato_id):
    try:
        contato = Contato.objects.get(pk=contato_id)
        contato.delete()
        messages.success(request, "Contato removido com sucesso!")
    except:
        messages.warning(request, "Não foi possível remover o contato.")
    finally:
        return HttpResponseRedirect('/contatos/')
