msgCriptografada = ''
msgDescriptografada = ''
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def transformarMensagemEmArray(msg):
    # Transformando a mensagem a ser criptografada em uma lista
    arrayMenssagem = []

    # Tratar os espaços vazios
    for i in list(msg):
        if i != ' ':
            arrayMenssagem.append(i)
    return arrayMenssagem


def listToString(s):

    str1 = " "

    return (str1.join(s))


def encodeMensagem(valorChave, msg):
    msgEncoded = []

    msgToArray = transformarMensagemEmArray(msg)
    for letra in msgToArray:
        posicao = (alfabeto.index(letra) + valorChave) % 52
        msgEncoded.append(alfabeto[posicao])
    msgCriptografada = listToString(msgEncoded)
    return msgCriptografada


def decodeMensagem(valorChave, msg):
    msgDecoded = []
    msgToArray = transformarMensagemEmArray(msg)
    for letra in msgToArray:
        posicao = (alfabeto.index(letra) - valorChave) % 52
        msgDecoded.append(alfabeto[posicao])
    msgDescriptografada = listToString(msgDecoded)
    return msgDescriptografada


print('==================== CIFRA DE CÉSAR ===============')

msg = str(input("Qual a mensagem que será criptografada? \n > "))

valorChave = int(input("Qual o valor da chave? \n > "))

print('Mensagem Criptografada: ', encodeMensagem(valorChave, msg))

print('Mensagem descriptografada: ',
      decodeMensagem(valorChave, encodeMensagem(valorChave, msg)))
