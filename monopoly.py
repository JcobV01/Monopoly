import os

class Board:
    def __init__(self, nazwa, cena, kraj, domki, podatek, rola, g1, g2, g3, g4):
        self.nazwa = nazwa
        self.cena = cena
        self.kraj = kraj
        self.domki = domki
        self.podatek = podatek
        self.rola = rola
        self.gracz = [g1, g2, g3, g4]



pole1 = Board("Grenada", 12000, "Hiszpania", 0, 34000, "posiadlosc"," ", " ", " ", " ")
pole2 = Board("Sewila", 12000, "Hiszpania", 0, 34000, "posiadlosc"," ", " ", " ", " ")
pole3 = Board("Madryt", 12000, "Hiszpania", 0, 34000, "posiadlosc"," ", " ", " ", " ")
pole4 = Board("Szansa", 12000, "None", 0, 34000, "szansa", " ", " ", " ", " ")
pole5 = Board("Shanghai", 12000, "Chiny", 0, 34000, "posiadlosc"," ", " ", " ", " ")
pole6 = Board("Podatek", 12000, "None", 0, 34000, "podatek", " ", " ", " ", " ")
pole7 = Board("Hong Kong", 12000, "Chiny", 0, 34000, "posiadlosc"," ", " ", " ", " ")


    



def setBoard(g1, g2, g3, g4):

    os.system('cls')

    leftLetters = ['z', 'y', 'x', 'w', 'u']
    rightLetters = ['h', 'i', 'j', 'k', 'l']

    print(f"┌{'─'*71}┐")
    print(f"│ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ │")
    print(f"│ │ {pole1.gracz[0]}   {pole1.gracz[1]} │ │ {pole2.gracz[0]}   {pole2.gracz[1]} │ │ {pole3.gracz[0]}   {pole3.gracz[1]} │ │ {pole4.gracz[0]}   {pole4.gracz[1]} │ │ {pole5.gracz[0]}   {pole5.gracz[1]} │ │ {pole6.gracz[0]}   {pole6.gracz[1]} │ │ {pole7.gracz[0]}   {pole7.gracz[1]} │ │")
    print(f"│ │   a   │ │   b   │ │   b   │ │   d   │ │   e   │ │   f   │ │   g   │ │")
    print(f"│ │ {pole1.gracz[2]}   {pole1.gracz[3]} │ │ {pole2.gracz[2]}   {pole2.gracz[2]} │ │ {pole3.gracz[2]}   {pole3.gracz[3]} │ │ {pole4.gracz[2]}   {pole4.gracz[3]} │ │ {pole5.gracz[2]}   {pole5.gracz[3]} │ │ {pole6.gracz[2]}   {pole6.gracz[3]} │ │ {pole7.gracz[2]}   {pole7.gracz[3]} │ │")
    print(f"│ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ │")

    for i in range(0, 5):
        print(f"│ ┌───────┐{' '*51}┌───────┐ │")
        print(f"│ │ {g1}   {g2} │{' '*51}│ {g1}   {g2} │ │")
        print(f"│ │   {leftLetters[i]}   │{' '*51}│   {rightLetters[i]}   │ │")
        print(f"│ │ {g3}   {g4} │{' '*51}│ {g3}   {g4} │ │")
        print(f"│ └───────┘{' '*51}└───────┘ │")
    
    print(f"│ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ │")
    print(f"│ │ {g1}   {g2} │ │ {g1}   {g2} │ │ {g1}   {g2} │ │ {g1}   {g2} │ │ {g1}   {g2} │ │ {g1}   {g2} │ │ {g1}   {g2} │ │")
    print(f"│ │   t   │ │   s   │ │   r   │ │   p   │ │   o   │ │   n   │ │   m   │ │")
    print(f"│ │ {g3}   {g4} │ │ {g3}   {g4} │ │ {g3}   {g4} │ │ {g3}   {g4} │ │ {g3}   {g4} │ │ {g3}   {g4} │ │ {g3}   {g4} │ │")
    print(f"│ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ │")
    print(f"└{'─'*71}┘")


setBoard(" ", " ", " ", " ")
