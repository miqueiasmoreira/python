from time import sleep
print("\033[1;32m-=-\033[m" * 20)
print("\033[0;31mTeste qual valor é maior ou menor\033[m")
print("\033[1;32m-=-\033[m" * 20)
valor1 = int(input("\033[1;34mValor 1:\033[m "))
valor2 = int(input("\033[1;34mValor 2:\033[m "))
print("\033[0;35mPROCESSANDO...\033[m")
sleep(2)
if (valor1 > valor2):
    print("O \033[1;33mPRIMEIRO\033[m valor é \033[1;33mMAIOR\033[m")
elif (valor2 > valor1):
    print("O \033[1;33mSEGUNDO\033[m valor é \033[1;33mMAIOR\033[m")
else:
    print("Os valores são \033[1;33mIGUAIS\033[m")

