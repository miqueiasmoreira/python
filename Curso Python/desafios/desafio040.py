nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2
if (media < 5.0):
    print("\033[1;31mREPROVADO\033[m")
elif(media > 5.0 and media <= 6.9):
    print("\033[1;33mRECUPERAÇÃO\033[m")
else:
    print("\033[1;92mAPROVADO\033[m")