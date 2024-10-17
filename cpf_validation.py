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