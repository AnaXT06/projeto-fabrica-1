nota1 = float(input("Digite uma nota"))
nota2 = float(input("Digite outra nota"))
nota3 = float(input("Digite outra nota"))
nota4 = float(input("Digite ultima nota"))

media = (nota1 + nota2 + nota3 + nota4) /4
print("A media é", media)
if media >=7:
    print("Aprovado")
elif media >=5 and media <=7:
    print("Recuperacao")
else:
    print("Reprovado")
