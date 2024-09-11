# Crie um programa que receba a idade de uma pessoa e classifique-a de acordo com as seguintes faixas etárias:
# Criança (0-12 anos)
# Adolescente (13-17 anos)
# Adulto (18-59 anos)
# Idoso (60 anos ou mais)

idd = int(input("insira sua idade: "))
if idd <= 12:
    print ("criança")
else: 
    if idd <= 17:
        print ("adolescente")
    elif idd <= 59:
        print ("adulto")
    else:
            if idd >= 60:
                print("idoso")

