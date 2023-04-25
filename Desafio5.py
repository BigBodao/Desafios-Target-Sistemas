#   Escreva um programa que inverta os caracteres de um string.

#   IMPORTANTE:
#   a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente
#   definida no código;
#   b) Evite usar funções prontas, como, por exemplo, reverse;

palavra = input("Digite a palavra para ser invertida: ")
listaPalavra = list(palavra)

for i in range(len(listaPalavra)//2):
    listaPalavra[i], listaPalavra[-i-1] = listaPalavra[-i-1], listaPalavra[i]

inverso = ''.join(listaPalavra)

print(f"A palavra invertida fica: {inverso}")
