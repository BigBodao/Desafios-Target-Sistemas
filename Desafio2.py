#   Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
#   anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar
#   onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o
#   número informado pertence ou não a sequência.

numero = int(0)
numero = int(input(f"Digite o número que deseja encontrar na sequencia de Fibonacci: \n"))

primeiro = 0
ultimo = 1
cond = False
if numero==0 or numero==1:
    print(f"O número procurado foi:{numero}. E ele se encontra na sequencia de Fibonacci.\n")
    cond=True
print(f"0, 1, ")
while(cond==False):
    atual = primeiro+ultimo
    primeiro = ultimo
    ultimo = atual
    print(f" {atual},")
    if atual == numero:
        print("\n")
        print(f"O número procurado foi:{numero}. E ele se encontra na sequencia de Fibonacci.\n")
        cond=True
    elif atual > numero:
        print("\n")
        print(f"O número procurado foi:{numero}. E ele Não se encontra na sequencia de Fibonacci\n")
        cond=True

    