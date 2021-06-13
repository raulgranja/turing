def arroba(caracter):
    """
    Função que verifica se o caracter é um @ ou não.
    :param caracter: O caracter a ser analisado.
    :return: Se o caracter for um @, retorna True, caso contrário, False.
    """
    if caracter == '@':
        return True
    else:
        return False


def compare(a, b):
    """
    Função que compara dois caracteres.
    :param a: Primeiro caracter.
    :param b: Segundo caracter.
    :return: Caso os caracteres sejam iguais, a função retorna uma string contendo exatamente um espaço vazio;
    se os caracteres não forem iguais, ela retorna o caracter representado por b.
    """
    if a == b:
        return ' '
    else:
        return b


def savings(email1, email2):
    """
    Função que compara duas strings e calcula quantos caracteres podem ser desprezados (um caracter desprezado é o
    mesmo que um espaço em branco, já que um email não contém espaços e não gastaria tinta para impressão).
    Essa função leva em conta apenas os caracteres antes do @ para fazer a comparação, e caso haja um espaço seguido
    de um caracter que não seja espaço, ou se o primeiro caracter não for um espaço, o programa desconsidera o
    restante da string.
    :param email1: A primeira string (ou primeiro email).
    :param email2: A segunda string (ou segundo email).
    :return: A quantidade de espaços que foram identificados na string (ou seja, a economia).
    """
    s = ''  # Nova string que será gerada com a análise dos dois emails

    for j in range(len(email1)):  # Para cada caracter do email:
        if arroba(email1[j]):  # Se o caracter for um arroba, o restante é desconsiderado
            break

        else:
            s += compare(email1[j], email2[j])  # Compara e concatena o caracter da segunda string que foi analisado
            letra_past = s[j - 1]
            letra_atual = s[j]
            if (letra_past == ' ' and letra_atual != ' ') or s[0] != ' ':
                break
        # Se o caracter não for um @, compara os dois caracteres, e se a letra passada for um espaço e a letra atual
        # não for um espaço, o programa desconsidera o restante, pois não haverá mais economia. O programa também
        # desconsidera caso o primeiro caracter não é um espaço.

    return s.count(' ')


def main():
    n = int(input())  # Quantidade de emails que serão fornecidos.
    lista_emails = list()  # Lista que guarda os emails que serão fornecidos.
    economia = 0  # Quantos caracteres o programa "economizará".

    # Laço que solicita os N emails:
    for i in range(n):
        email = str(input())
        lista_emails.append(email)
        if i == 0:  # Se for o primeiro email, o programa ja passará para o próximo input.
            continue
        else:
            economia += savings(lista_emails[i - 1], lista_emails[i])
            # Analisa a economia de dois emails consecutivos e soma na variável.

    print(economia)


main()
