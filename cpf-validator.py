class ValidCpf:
    def __init__(self):

        self.Error = ""

    def _format_cpf(self, cpf):
        try:
            cpf_formated = cpf.replace(".", "").replace("-", "")

            if len(cpf_formated) == 11:
                return cpf_formated
            else:
                self.Error = 'invalid digit numbers, required 11 digits'

        except Exception as error:
            self.Error = f'error : {error}'

    def _invalid_numbers(self, cpf_formated):
        invalids_numbers = ['11111111111', '22222222222', '33333333333', '44444444444',
                            '55555555555', '66666666666', '77777777777', '88888888888',
                            '99999999999', '00000000000']

        if cpf_formated in invalids_numbers:
            self.Error = 'Invalid numbers'

        return cpf_formated

    def _last_digits(self, cpf):
        cpf = cpf[:-2]
        sum = 0
        counter = 10
        for number in cpf:
            sum += (int(number) * counter)
            counter -= 1
        if sum % 11 >= 2:
            first_digit = 11 - (sum % 11)
        else:
            first_digit = 0

        cpf = cpf + str(first_digit)
        counter = 11
        sum = 0

        for number in cpf:
            sum += (int(number) * counter)
            counter -= 1

        if sum % 11 >= 2:
            second_digit = 11 - (sum % 11)
        else:
            second_digit = 0
        return str(first_digit) + str(second_digit)

    def cpf_isvalid(self, cpf):

        formated_cpf = self._invalid_numbers(self._format_cpf(cpf))
        if self.Error:
            return self.Error


        if cpf[-2:] == self._last_digits(formated_cpf):
            return f"It's  valid!"
        else:
            return f"It's not valid!"



is_valid = ValidCpf()
while True:
    cpf = input()
    print()
    print(is_valid.cpf_isvalid(cpf))