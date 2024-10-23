def get_check_digit(remainder):
    if remainder < 2:
        return 0
    
    return 11 - remainder

def calculate_digits():
    multipliers = list(range(10,1,-1))
    result = 0

    for index in range(9):
        product = int(cpf[index]) * multipliers[index]
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
first_check_digit = calculate_digits()

print('First check digit:',first_check_digit)