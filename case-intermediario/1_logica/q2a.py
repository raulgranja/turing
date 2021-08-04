def repetido(car, lista):
    """
    Analisa se um elemento já estiver dentro de uma lista.
    :param car: O elemento que está entrando na lista, para este programa, é análogo ao carro.
    :param lista: A lista que a função irá trabalhar, para este programa, é análoga ao estacionamento.
    :return: Retorna True se aquele elemento já estiver na lista, e False se ele não estiver.
    """
    if car in lista:
        return True
    else:
        return False


def entraOuSai(car, lista):
    """
    Analisa se um elemento está entrando ou saindo da lista, e se for possível, executa a ação.
    :param car: O elemento que está entrando na lista, para este programa, é análogo ao carro.
    :param lista: A lista que a função irá trabalhar, para este programa, é análoga ao estacionamento.
    :return: Retorna True se a função não encontrar erros de execução, ou seja, se os elementos podem entrar ou sair na
    ordem correta, como se fosse uma pilha; caso contrário retorna False.
    """
    n = abs(car)  # Módulo de car.
    try:
        if car < 0:
            if n == lista[-1]:
                lista.pop()
                # Ou seja, se o carro quer sair do estacionamento e for o topo da pilha (o último a ter entrado),
                # ele sairá.
            else:
                return False

        elif car > 0:
            if not repetido(car, lista):
                lista.append(n)
                # Ou seja, se o carro quer entrar no estacionamento e partindo do pressuposto de que é impossível ter
                # dois carros identicos no estacionamento ao mesmo tempo, ele entrará.
            else:
                return False

        return True

    except IndexError:  # Se houver erros como por exemplo, retirar um carro que ja não está no estacionamento.
        return False


def main():
    entrada = str(input()).split(' ')
    k = int(entrada[0])  # Tamanho do estacionamento
    n = int(entrada[1])  # Instantes que serão monitorados
    estacionamento = list()
    resposta = 'sim'  # A resposta do programa já começa sendo "sim", e verificaremos se ela será falseada.

    # Laço que solicita os n carros.
    for i in range(n):
        carro = int(input())
        if not entraOuSai(carro, estacionamento) or len(estacionamento) > k:
            resposta = 'nao'
            # Ou seja, se a resposta da função entraOuSai for False, ou se o estacionamento não comportar um carro que
            # esteja entrando, a resposta já torna-se "nao" permanentemente.
    print(resposta)


main()
