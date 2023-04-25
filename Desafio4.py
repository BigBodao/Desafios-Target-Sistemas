#   Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. 
#   O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e o caminhão de
#   Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem na
#   rodovia, qual estará mais próximo a cidade de Ribeirão Preto?

#   IMPORTANTE:
#   a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.
#   b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em 
#   cada um deles e o carro possui tag de pedágio (Sem Parar)
#   c) Explique como chegou no resultado.

#   Resposta: Utilizando uma abordagem em que se calcula o tempo que os veículos levam para se encontrar na rodovia
#   e após isso determinar a posição deles no momento do encontro

# distância entre as cidades em km
distanciaTotal = 100

# velocidade do carro em km/h
velocidadeCarro = 110

# velocidade do caminhão em km/h
velocidadeCaminhao = 80

# tempo em horas até o encontro dos veículos
tempoEncontro = distanciaTotal / (velocidadeCarro + velocidadeCaminhao)

# distância percorrida pelo carro até o encontro em km
distanciaCarro = velocidadeCarro * tempoEncontro

# distância percorrida pelo caminhão até o encontro em km
distanciaCaminhao = velocidadeCaminhao * tempoEncontro

# distância do carro até o ponto de encontro em km
distanciaCarroEncontro = distanciaTotal / 2 - distanciaCarro / 2

# distância do caminhão até o ponto de encontro em km
distanciaCaminhaoEncontro = distanciaTotal / 2 - distanciaCaminhao / 2

if distanciaCarroEncontro < distanciaCaminhaoEncontro:
    print("O carro está mais próximo de Ribeirão Preto")
else:
    print("O caminhão está mais próximo de Ribeirão Preto")
