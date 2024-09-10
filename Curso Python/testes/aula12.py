nome = str(input("Qual é seu nome? "))
if (nome == 'Miquéias'):
    print("\033[1;32;44mQue nome bonito\033[m")
elif (nome == 'Maria'):
    print("\033[1;35;45mNome da namorada mais linda do mundo\033[m")
else:
    print("Seu nome é bem normal")
print(f"Tenha um bom dia, \033[1;32;44m{nome}\033[m")