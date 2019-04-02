Projeto Iniciado com o intuito de sanar uma dificuldade na busca por validadores de documentos, na primeira parte,
foi implementado o validador de cpf, nas proximas serão rg, e cnpj.
Como usa?
basta baixar e importar a classe ValidDocuments e instanciar um objeto, para que ele possa usar o metodo cpf_isvalid, que recebe como parametro um numero de cpf.

ex1:

import ValidDocuments

documento = ValidDocuments
cpf = '187.872.456-32'
print(documento.cpd_isvalid(cpf))
- Documento invalido!

Os tipos de retornos so 4:
Documento valido -> Quando o cpf passado é valido!

Documento invalido -> Quando o cpf passado possui 11 digitos não repetidos, mas msm assim é invalido!

Cpf deve possuir 11 digitos -> Quando o cpf passado não possui 11 digitos

Esses numeros, não são validos -> Quando o cpf passado representa 11 numeros iguais(Não valido!)

ex2:

import ValidDocuments

documento = ValidDocuments
cpf = '848.079.640-54'
print(documento.cpd_isvalid(cpf))
-Documento Valido!

