def encodeMensagem(valorChave, msg):
    m = ''
    for letra in msg:
        m += chr(ord(letra) + valorChave)
    return m


def decodeMensagem(valorChave, msg):
    m = ''
    for letra in msg:
        m += chr(ord(letra) - valorChave)
    return m


print('==================== CIFRA DE CÉSAR ===============')

msg = str(input("Qual a mensagem que será criptografada? \n > "))

valorChave = int(input("Qual o valor da chave? \n > "))

encoded = encodeMensagem(valorChave, msg)

print('Mensagem Criptografada: ', encoded)
print('Mensagem Descriptografada: ',
      decodeMensagem(valorChave, encoded))
