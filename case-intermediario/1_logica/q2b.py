def aFilaAndou(elem, lista):
    """
    Retira o elemento final da lista e insere um novo elemento no índice 0.
    :param elem: Elemento que será inserido no índice 0.
    :param lista: Lista que será trabalhada
    :return: Lista já com os elementos trocados.
    """
    lista.insert(0, elem)
    lista.pop()
    return lista


def main():
    """
    Este programa funciona da seguinte maneira: Uma lista de espera é criada com um tamanho igual ao máximo instante
    fornecido, tanto no laço dos horários, quanto no instante que será exibido no output. Os primeiros valores da lista
    de espera vão entrando no estacionamento, a medida que os carros vão saindo do estacionamento.
    """
    entrada = str(input()).split(' ')
    k = int(entrada[0])  # Tamanho do estacionamento
    n = int(entrada[1])  # Número de carros que entram no estacionamento.
    estacionamento = [0] * k
    max_espera = 0  # Variável que determina o tamanho da lista de espera.
    agenda = dict()  # Dicionário que relaciona um instante com um carro (keys: instantes; values: carros).

    # Laço que pede os horários de entrada de cada carro.
    for carro in range(1, n + 1):
        e = int(input())  # Horário de entrada do carro (E).
        agenda[e] = carro
        if e > max_espera:
            max_espera = e

    t = int(input())  # Instante que será indicado.

    if t > max_espera:
        max_espera = t

    espera = [0] * max_espera

    # Laço que substitui os zeros na espera de acordo com os horários, (se o horário for 4, será no quarto índice, e
    # assim por diante.
    for k, v in agenda.items():
        espera[k - 1] = v

    # Laço que muda as configurações do estacionamento.
    for i in range(t):
        aFilaAndou(espera[i], estacionamento)

    for i in estacionamento:
        print(i, end=' ')


main()
