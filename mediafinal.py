

while True:
    nota1 = float (input ('digite nota 1°: ' ))
    if nota1 <= 10 and nota1 >= 0:
        break
while True:
    nota2 = float (input ('digite nota 2°: ' ))
    if nota2 <= 10 and nota2 >= 0:
        break
while True:
    nota3 = float (input ('digite nota 3°: ' ))
    if nota3 <= 10 and nota3 >= 0:
        break
while True:
    nota4 = float (input ('digite nota 4°: ' ))
    if nota4 <= 10 and nota4 >= 0:
        break

print (nota1,nota2,nota3,nota4)

mediafinal =(nota1 + nota2 + nota3 + nota4) / 4
print('media final: ',mediafinal)

if (mediafinal >= 5):
    print ('Aluno APROVADO!')
elif (mediafinal >=3):
    print('Aluno em RECUPERAÇÃO!')       
else:
    print ('Aluno REPROVADO!')

print('fim do ano letivo, BOAS FERIAS!!!')

    

 