def divideString(string):
    """
    Função que divide uma string na metade.
    :param string: String que vai ser dividida.
    :return: Uma tupla com dois elementos, cada um deles sendo uma das metades da string.
    """
    primeira_metade = string[0:len(string)//2]
    segunda_metade = string[len(string)//2:len(string)]
    return primeira_metade, segunda_metade


def inverteString(string):
    """
    Função que inverte uma string.
    :param string: String que vai ser invertida.
    :return: Uma nova string, que é o inverso da inserida.
    """
    nova_string = ''
    for caracter in range(len(string) - 1, -1, -1):
        nova_string += string[caracter]
    return nova_string


def juntaStrings(tupla):
    """
    Concatena duas strings em uma só, a partir de uma tupla com as duas metades.
    :param tupla: Tupla com duas strings.
    :return: Uma nova string, sendo a concatenação das duas strings que estavam na tupla.
    """
    nova_string = tupla(1) + tupla(2)
    return nova_string


def dominioErrado(string):
    """
    Verifica se um email está com o domínio errado (diferente de @usp.br).
    :param string: O email que será verificado.
    :return: Se o domínio estiver errado, retorna True, se estiver correto, retorna False.
    """
    s = string.split('@')
    if s[1] == 'usp.br':
        return False
    else:
        return True


def main():
    n = int(input())  # Quantidade de emails que serão impressos.
    lista_strings = list()  # Lista que guardará as strings já corretamente formatadas.

    # Laço que solicita os emails incorretos.
    for i in range(n):
        string = str(input())
        string_final = ''
        tupla = divideString(string)  # Guarda as duas metades da string inserida em uma tupla.
        for j in range(2):
            string_final += inverteString(tupla[j])  # Concatena as duas metades já invertidas em string_final.
        if dominioErrado(string_final):
            lista_strings.append('ERRO')
        else:
            lista_strings.append(string_final)
        # Se o domínio estiver incorreto, guarda a string ERRO dentro da lista_strings.

    # Laco para printar cada uma das strings que estão dentro da lista.
    for string in lista_strings:
        print(string)


main()
