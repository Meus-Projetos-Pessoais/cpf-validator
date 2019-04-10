**_É muito simples usar o cpf-validator, basta importar a classe
`ValidCpf` do arquivo_ `cpf-Validator.py`_, depois instanciar um objeto
com a classe, e chamar o metodo _`cpf_isvalid`_, passando o cpf como paramentro:_**

`from cpf-validator import ValidCpf`
    
    cpf = '243.245.490-10'
    valid = Valid()
    valid.cpf_isvalid(cpf)

saida:

        It's valid!
    
Caso coloque cpf invalido receberá o erro ex:
    
    from cpf-validator import ValidCpf`
    
    cpf = '243.245.490-90'
    valid = Valid()
    valid.cpf_isvalid(cpf)
    
saida :

        It's not valid!
        
Tratativas de erros:
    
    invalid digit numbers, required 11 digits   #Se cpf não tiver 11 digitod
    Invalid numbers # Se for 11 numeros iguais, ex: 11111111111
    It's not valid! #Se atende todos os criterios ateriores, mas não é um cpf valido