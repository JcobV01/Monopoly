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



pole1 = Board("START", 0, "None", 0, 0, "start"," ", " ", " ", " ")

pole2 = Board("Sewila", 12000, "Hiszpania", 0, 34000, "posiadlosc"," ", " ", " ", " ")
pole3 = Board("Madryt", 12000, "Hiszpania", 0, 34000, "posiadlosc"," ", " ", " ", " ")

pole4 = Board("Szansa", 0, "None", 0, 34000, "szansa", " ", " ", " ", " ")

pole5 = Board("Shanghai", 12000, "Chiny", 0, 34000, "posiadlosc"," ", " ", " ", " ")
pole6 = Board("Bali", 12000, "None", 0, 34000, "podatek", " ", " ", " ", " ")

pole7 = Board("Bezludna wyspa", 12000, "specjalne", 0, 34000, "kara"," ", " ", " ", " ")

pole8 = Board("Wenecja", 12000, "Włochy", 0, 34000, "posiadlosc"," ", " ", " ", " ")
pole9 = Board("Mediolan", 12000, "Włochy", 0, 34000, "posiadlosc"," ", " ", " ", " ")

pole9 = Board("Szansa", 0, "None", 0, 34000, "szansa"," ", " ", " ", " ")

pole10 = Board("Hamburg", 0, "Niemcy", 0, 34000, "posiadlosc"," ", " ", " ", " ")
pole11 = Board("Cypr", 0, "None", 0, 34000, "szansa"," ", " ", " ", " ")


polaPoziome = [pole1, pole2, pole3, pole4]


    



def setBoard(g1, g2, g3, g4):

    os.system('cls')

    leftLetters = ['z', 'y', 'x', 'w', 'v', 'u', 't']
    rightLetters = ['g', 'h', 'i', 'j', 'k', 'l', 'ł']

    print(f"┌{'─'*91}┐")
    print(f"│ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ │")
    print(f"│ │ {pole1.gracz[0]}   {pole1.gracz[1]} │ │ {pole2.gracz[0]}   {pole2.gracz[1]} │ │ {pole3.gracz[0]}   {pole3.gracz[1]} │ │ {pole4.gracz[0]}   {pole4.gracz[1]} │ │ {pole5.gracz[0]}   {pole5.gracz[1]} │ │ {pole6.gracz[0]}   {pole6.gracz[1]} │ │ {pole7.gracz[0]}   {pole7.gracz[1]} │ │ {pole7.gracz[0]}   {pole7.gracz[1]} │ │ {pole7.gracz[0]}   {pole7.gracz[1]} │ │")
    print(f"│ │   a   │ │   ą   │ │   b   │ │   c   │ │   ć   │ │   d   │ │   e   │ │   ę   │ │   f   │ │")
    print(f"│ │ {pole1.gracz[2]}   {pole1.gracz[3]} │ │ {pole2.gracz[2]}   {pole2.gracz[2]} │ │ {pole3.gracz[2]}   {pole3.gracz[3]} │ │ {pole4.gracz[2]}   {pole4.gracz[3]} │ │ {pole5.gracz[2]}   {pole5.gracz[3]} │ │ {pole6.gracz[2]}   {pole6.gracz[3]} │ │ {pole7.gracz[2]}   {pole7.gracz[3]} │ │ {pole7.gracz[2]}   {pole7.gracz[3]} │ │ {pole7.gracz[2]}   {pole7.gracz[3]} │ │")
    print(f"│ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ │")

    for i in range(0, 7):
        print(f"│ ┌───────┐{' '*71}┌───────┐ │")
        print(f"│ │ {g1}   {g2} │{' '*71}│ {g1}   {g2} │ │")
        print(f"│ │   {leftLetters[i]}   │{' '*71}│   {rightLetters[i]}   │ │")
        print(f"│ │ {g3}   {g4} │{' '*71}│ {g3}   {g4} │ │")
        print(f"│ └───────┘{' '*71}└───────┘ │")
    
    print(f"│ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ │")
    print(f"│ │ {g1}   {g2} │ │ {g1}   {g2} │ │ {g1}   {g2} │ │ {g1}   {g2} │ │ {g1}   {g2} │ │ {g1}   {g2} │ │ {g1}   {g2} │ │ {g1}   {g2} │ │ {g1}   {g2} │ │")
    print(f"│ │   s   │ │   r   │ │   q   │ │   p   │ │   ó   │ │   o   │ │   ń   │ │   n   │ │   m   │ │")
    print(f"│ │ {g3}   {g4} │ │ {g3}   {g4} │ │ {g3}   {g4} │ │ {g3}   {g4} │ │ {g3}   {g4} │ │ {g3}   {g4} │ │ {g3}   {g4} │ │ {g1}   {g2} │ │ {g1}   {g2} │ │")
    print(f"│ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ │")
    print(f"└{'─'*91}┘")


setBoard(" ", " ", " ", " ")
