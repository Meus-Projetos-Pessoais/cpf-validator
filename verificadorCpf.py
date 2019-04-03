class ValidDocuments:
    @staticmethod
    def cpf_isvalid(cpf):
        try:
            str(cpf)
        except:
            return f'o cpf deve ser uma string'

        soma = 0
        contador = 10
        cpfDigt = cpf[-2:]
        cpf = cpf.replace(".","").replace("-","")[:-2]
        numeros_invalid = [
            '111111111','222222222','333333333','444444444',
            '555555555','666666666','777777777','888888888',
            '999999999','000000000']

        if cpf not in numeros_invalid:
            if len(cpf) == 9:
                for i in cpf:
                    soma +=(int(i) * contador)
                    contador -= 1
                if soma % 11 > 2:
                    digit_one = 11 - (soma % 11)
                else:
                    digit_one = 0

                cpf = cpf+str(digit_one)
                contador = 11
                soma = 0

                for i in cpf:
                    soma +=(int(i) * contador)
                    contador -= 1

                if soma % 11 > 2:
                    digit_two = 11 - (soma % 11)
                else:
                    digit_two = 0
                digits = str(digit_one)+str(digit_two)

                if digits == cpfDigt:
                    return f'Documento valido!'
                else:
                    return f'documento invalido'

            else:
                return f'cpf deve possuir 11 digitos'
        else:
            return f'Esses numeros, não são validos'



