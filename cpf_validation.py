def validate_cpf():
    if cpf == verified_cpf:
        print('Valid CPF')
    else:
        print('Invalid CPF')

    print('Provided CPF:', cpf)
    print('Verifield CPF:', verified_cpf)

def get_check_digit(remainder):
    if remainder < 2:
        return 0
    
    return 11 - remainder

def calculate_digits():
    len_multipliers = len(verified_cpf) + 1
    multipliers = list(range(len_multipliers,1,-1))
    result = 0

    for index in range(len(verified_cpf)):
        product = int(verified_cpf[index]) * multipliers[index]
        result += product    

    _, remainder = divmod(result, 11)

    digit = get_check_digit(remainder)
    return str(digit)

def validate_entry():
    while True:
        cpf = input('CPF: ').replace(".", "").replace('-', '')#Remove dots and dashes
        #only numbers
        if not cpf.isdigit():
            continue
        #Check the numbers of characters
        if len(cpf) != 11:
            continue
        #Avoid all identical digits
        if cpf == cpf[0]*11:
            continue

        return cpf

cpf = validate_entry()

verified_cpf = cpf[0:9]
verified_cpf += calculate_digits()
verified_cpf += calculate_digits()

validate_cpf()