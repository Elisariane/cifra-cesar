msgCriptografada = ''
msgDescriptografada = ''
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encodeMensagem(valorChave, msg):
    msgEncoded = []

    for letra in msg:
        if (letra not in alfabeto):
            msgEncoded.append(letra)
        else:
            posicao = (alfabeto.index(letra) + valorChave) % 52
            msgEncoded.append(alfabeto[posicao])
    msgCriptografada = ''.join(msgEncoded)
    return msgCriptografada


def decodeMensagem(valorChave, msg):
    msgDecoded = []
    for letra in msg:
        if (letra not in alfabeto):
            msgDecoded.append(letra)
        else:
            posicao = (alfabeto.index(letra) - valorChave) % 52
            msgDecoded.append(alfabeto[posicao])
    msgDescriptografada = ''.join(msgDecoded)
    return msgDescriptografada


print('==================== CIFRA DE CÉSAR ===============')

msg = str(input("Qual a mensagem que será criptografada? \n > "))

valorChave = int(input("Qual o valor da chave? \n > "))

print('Mensagem Criptografada: ', encodeMensagem(valorChave, msg))

print('Mensagem descriptografada: ',
      decodeMensagem(valorChave, encodeMensagem(valorChave, msg)))
