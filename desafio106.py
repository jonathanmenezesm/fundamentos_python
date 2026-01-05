# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
#
# OBS: use cores.
{

}

from time import sleep

def escreva(texto):
    tamanho = len(texto) + 4
    print("~" * tamanho)
    print(f"  {texto}")
    print("~" * tamanho)

def pyhelp(comando):
    help(comando)

def ajudinha():
    while True:
        escreva("Sistema de ajuda PyHELP")
        comando = input("Função ou Biblioteca > ")
        if comando.upper() == "FIM":
            break
        else:
            sleep(1)
            pyhelp(comando)

ajudinha()
