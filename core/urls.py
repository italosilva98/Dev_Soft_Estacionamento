from django.urls import path
from .views import (
    lista_pessoas,
    lista_veiculos,
    lista_movrotativos,
    lista_movmensalistas,
    lista_mensalistas,
    pessoa_novo,
    veiculo_novo,
    movrot_novo,
    mensal_novo,
    movmensal_novo,
    pessoa_update,
    veiculo_update,
    movrot_update,
    mensal_update,
    movmensal_update,
    pessoa_delete,
    veiculo_delete,
    movrot_delete,
    mensal_delete,
    movmensal_delete,
)

urlpatterns = [
    path('pessoas/', lista_pessoas, name = 'core_lista_pessoas'),
    path('pessoa-novo/', pessoa_novo, name='core_pessoa_novo'),
    path('pessoa-update/<int:id>/', pessoa_update, name='core_pessoa_update'),
    path('pessoa-delete/<int:id>/', pessoa_delete, name='core_pessoa_delete'),

    path('veiculos/', lista_veiculos, name = 'core_lista_veiculos'),
    path('veiculo-novo/', veiculo_novo, name='core_veiculo_novo'),
    path('veiculo-update/<int:id>/', veiculo_update, name='core_veiculo_update'),
    path('veiculo-delete/<int:id>/', veiculo_delete, name='core_veiculo_delete'),

    path('mov-rot/', lista_movrotativos, name = 'core_lista_movrotativos'),
    path('movrot-novo/', movrot_novo, name = 'core_movrot_novo'),
    path('movrot-update/<int:id>/', movrot_update, name='core_movrot_update'),
    path('movrot-delete/<int:id>/', movrot_delete, name='core_movrot_delete'),

    path('mensalistas', lista_mensalistas, name = 'core_lista_mensalistas'),
    path('mensal-novo', mensal_novo, name = 'core_mensal_novo'),
    path('mensal-update/<int:id>/', mensal_update, name='core_mensal_update'),
    path('mensal-delete/<int:id>/', mensal_delete, name='core_mensal_delete'),

    path('mov-mensal', lista_movmensalistas, name = 'core_lista_movmensalistas'),
    path('movmensal-novo', movmensal_novo, name = 'core_movmensal_novo'),
    path('movmensal-update/<int:id>/', movmensal_update, name='core_movmensal_update'),
    path('movmensal-delete/<int:id>/', movmensal_delete, name='core_movmensal_delete'),
]