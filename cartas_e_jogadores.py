# Criação das cartas e do Baralho

class Carta:
    def __init__(self, nome, valor, naipe):
        self.nome = nome
        self.valor = valor
        self.naipe = naipe


class Baralho:

    valores = (4, 5, 6, 7, "Q", "J", "K", "A", 2, 3)
    naipes = ("Ouros", "Espadas", "Copas", "Paus")

    def __init__(self):

        self.cartas = []
        self.criar_cartas()

    def criar_cartas(self):

        for v in self.valores:

            valor = v

            for n in self.naipes:

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

                nova_carta = Carta(nome, valor, naipe)
                self.cartas.append(nova_carta)


meu_baralho = Baralho()

#for carta in meu_baralho.cartas:
#    print(carta.nome, carta.valor, carta.naipe)