# Criação das cartas e do Baralho
valores = (4, 5, 6, 7, "Q", "J", "K", "A", 2, 3)
naipes = ("Ouros", "Espadas", "Copas", "Paus")

info_das_cartas = []

def criar_cartas():

        for v in valores:

            valor = v

            for n in naipes:

                naipe = n
                if valor == "A":
                     nome = f"Ás de {naipe}"
                
                elif valor == "Q":
                      nome = f"Rainha de {naipe}"  

                elif valor == "J":
                    nome = f"Valete de {naipe}"

                elif valor == "K":
                    nome = f"Rei de {naipe}"

                else:
                    nome = f"{valor} de {naipe} "

                info_das_cartas.append((nome, valor, naipe))


class Carta:
    def __init__(self, nome, valor, naipe):
        self.nome = nome
        self.valor = valor
        self.naipe = naipe


criar_cartas() 

baralho = [Carta(nome, valor, naipe) for nome, valor, naipe in info_das_cartas]

for Carta in baralho:
    print(Carta.nome)
        