import math

def el_numero_es_primo(numero):
    raiz_del_num=math.sqrt(numero)
    raiz_del_num=int(raiz_del_num)
    contador = 0
    for i in range (1 , raiz_del_num + 1):
        if i == 1 or i==numero:
            continue
        if numero % i == 0:
            contador = contador + 1

    if contador == 1:
        return False
    else:
        return True


def run():
    numero=int(input('Escribe el numero que deseas: '))
    if el_numero_es_primo(numero) ==True:
        print('el numero es primo')
    else:
        print('El numero no es primo')


if __name__ == "__main__":
    run()