nota1=float(input("DIGITE A PRIMEIRA NOTA: "))
nota2=float(input("DIGITE A SEGUNDA NOTA:  "))
nota3=float(input("DIGITE A TERCEIRA NOTA: "))

total=nota1+nota2+nota3
media=(total)/3

print(total)
print(media)

if total >=60 and media>=20 :
    print("PARABÉNS VOCÊ FOI APROVADO COM A MEDIA", media)
else:
    print("INFLIZMENTE VOCÊ FOI REPROVADO")

