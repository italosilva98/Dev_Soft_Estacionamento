from django.shortcuts import render, redirect
from .models import Pessoa, Veiculo, MovRotativo, MovMensalista, Mensalista
 
from .forms import PessoaForm, VeiculoForm, RotativoForm, MensalistaForm, MovmensalForm


## CRUD Pessoas ---------------------------------------------------------------------------

def lista_pessoas(req):
    pessoas = Pessoa.objects.all() #pega todos os dados de Pessoa
    form = PessoaForm()
    data = {'pessoas':pessoas, 'form':form}
    return render(req, 'core/lista_pessoas.html', data)


def pessoa_novo(req):
    form = PessoaForm(req.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)

    if request.method =='POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html',{'obj':pessoa})


## CRUD Veiculos ---------------------------------------------------------------------------

def lista_veiculos(req):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    return render(req, 'core/lista_veiculos.html',{'veiculos':veiculos, 'form':form})


def veiculo_novo(req):
    form = VeiculoForm(req.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)


def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)

    if request.method =='POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html',{'obj':veiculo})


## CRUD Mov Rotativos ---------------------------------------------------------------------------

def lista_movrotativos(req):
    movrotativos = MovRotativo.objects.all()
    form = RotativoForm()
    return render(req, 'core/lista_movrotativos.html', {'movrotativos':movrotativos, 'form':form})


def movrot_novo(req):
    form = RotativoForm(req.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')


def movrot_update(request, id):
    data = {}
    rotativo = MovRotativo.objects.get(id=id)
    form = RotativoForm(request.POST or None, instance=rotativo)
    data['rotativo'] = rotativo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/update_movrotativo.html', data)


def movrot_delete(request, id):
    movrot = MovRotativo.objects.get(id=id)

    if request.method =='POST':
        movrot.delete()
        return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/delete_confirm.html',{'obj':movrot})


## CRUD Mensalista ---------------------------------------------------------------------------

def lista_mensalistas(req):
    mensalistas =  Mensalista.objects.all()
    form = MensalistaForm()
    return render(req, 'core/lista_mensalistas.html', {'mensalistas':mensalistas, 'form':form})


def mensal_novo(req):
    form = MensalistaForm(req.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')


def mensal_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/update_mensalista.html', data)


def mensal_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)

    if request.method =='POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html',{'obj':mensalista})


## CRUD Mov Mensalista ---------------------------------------------------------------------------

def lista_movmensalistas(req):
    movmensalistas = MovMensalista.objects.all()
    form = MovmensalForm()
    return render(req, 'core/lista_movmensalistas.html', {'movmensalistas':movmensalistas, 'form':form})


def movmensal_novo(req):
    form = MovmensalForm(req.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalistas')


def movmensal_update(request, id):
    data = {}
    movmensal = MovMensalista.objects.get(id=id)
    form = MovmensalForm(request.POST or None, instance=movmensal)
    data['movmensal'] = movmensal
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/update_movmensal.html', data)


def movmensal_delete(request, id):
    movmensal = MovMensalista.objects.get(id=id)

    if request.method =='POST':
        movmensal.delete()
        return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/delete_confirm.html',{'obj':movmensal})
