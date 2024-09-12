from datetime import date
print("\033[0;32m-=-\033[m" * 20)
print("\033[0;33mVerificador de Alistamento Militar\033[m")
print("\033[0;32m-=-\033[m" * 20)
nascimento = int(input("Qual o ano do seu nascimento? "))
idade = (date.today().year) - nascimento
if (idade == 18):
    print("\033[1;32mHora de se alistar\033[m")
elif (idade > 18):
    print("\033[1;31mPassou do tempo\033[m")
else:
    print("\033[1;33mAinda vai se alistar\033[m")
print("---FIM---")