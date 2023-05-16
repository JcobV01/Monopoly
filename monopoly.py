import os

class Board:
    def __init__(self, id, znacznik, nazwa, cena, kraj, domki, podatek, rola, g1, g2, g3, g4):
        self.id = id
        self.znacznik = znacznik
        self.nazwa = nazwa
        self.cena = cena
        self.kraj = kraj
        self.domki = domki
        self.podatek = podatek
        self.rola = rola
        self.gracz = [g1, g2, g3, g4]


pole1 = Board(0, 'a', 'Start', 0, 'None', 0, 0, 'specjalne', '', '', '', '')
pole2 = Board(1, 'ą', 'Grenada', 60000, 'Hiszpania', 0, 3000, 'budynek', '', '', '', '')
pole3 = Board(2, 'b', 'Sewila', 60000, 'Hiszpania', 0, 3000, 'budynek', '', '', '', '')
pole4 = Board(3, 'c', 'Madryt', 60000, 'Hiszpania', 0, 3000, 'budynek', '', '', '', '')
pole5 = Board(4, 'ć', 'Bali', 200000, 'Wyspa', 0, 20000, 'wyspa', '', '', '', '')
pole6 = Board(5, 'd', 'Hongkong', 100000, 'Chiny', 0, 5000, 'budynek', '', '', '', '')
pole7 = Board(6, 'e', 'Pekin', 100000, 'Chiny', 0, 5000, 'budynek', '', '', '', '')
pole8 = Board(7, 'ę', 'Szanghaj', 120000, 'Chiny', 0, 6000, 'budynek', '', '', '', '')
pole9 = Board(8, 'f', 'Wiezienie', 0, 'None', 0, 0, 'specjalne', '', '', '', '')
pole10 = Board(9, 'g', 'Wenecja', 140000, 'Włochy', 0, 7000, 'budynek', '', '', '', '')
pole11 = Board(10, 'h', 'Mediolan', 140000, 'Włochy', 0, 7000, 'budynek', '', '', '', '')
pole12 = Board(11, 'i', 'Rzym', 160000, 'Włochy', 0, 16000, 'budynek', '', '', '', '')
pole13 = Board(12, 'j', 'Szansa', 0, 'None', 0, 0, 'specjalne', '', '', '', '')
pole12 = Board(13, 'k', 'Hamburg', 180000, 'Niemcy', 0, 18000, 'budynek', '', '', '', '')
pole13 = Board(14, 'l', 'Cypr', 200000, 'Wyspa', 0, 20000, 'wyspa', '', '', '', '')
pole14 = Board(15, 'ł', 'Berlin', 200000, 'Niemcy', 0, 20000, 'budynek', '', '', '', '')
pole15 = Board(16, 'm', 'Mistrzostwa', 0, 'None', 0, 0, 'specjalne', '', '', '', '')
pole16 = Board(17, 'n', 'Londyn', 220000, 'WielkaBrytania', 0, 22000, 'budynek', '', '', '', '')
pole17 = Board(18, 'ń', 'Dubaj', 200000, 'Wyspa', 0, 20000, 'wyspa', '', '', '', '')
pole18 = Board(19, 'o', 'Sydnay', 240000, 'WielkaBrytania', 0, 24000, 'budynek', '', '', '', '')
pole19 = Board(20, 'ó', 'Szansa', 0, 'None', 0, 0, 'specjalne', '', '', '', '')
pole20 = Board(21, 'p', 'Chicago', 260000, 'USA', 0, 26000, 'budynek', '', '', '', '')
pole21 = Board(22, 'q', 'LasVegas', 260000, 'USA', 0, 26000, 'budynek', '', '', '', '')
pole22 = Board(23, 'r', 'NowyJork', 280000, 'USA', 0, 28000, 'budynek', '', '', '', '')
pole23 = Board(24, 's', 'Podroz', 0, 'None', 0, 0, 'specjalne', '', '', '', '')
pole24 = Board(25, 't', 'Nicea', 200000, 'Wyspa', 0, 20000, 'wyspa', '', '', '', '')
pole25 = Board(26, 'u', 'Lyon', 300000, 'Francja', 0, 30000, 'budynek', '', '', '', '')
pole26 = Board(27, 'v', 'Paryz', 320000, 'Francja', 0, 32000, 'budynek', '', '', '', '')
pole27 = Board(28, 'w', 'Szansa', 0, 'None', 0, 0, 'specjalne', '', '', '', '')
pole28 = Board(29, 'x', 'Krakow', 350000, 'Polska', 0, 35000, 'budynek', '', '', '', '')
pole29 = Board(30, 'y', 'Podatek', 0, 'None', 0, 0, 'specjalne', '', '', '', '')
pole30 = Board(31, 'z', 'Warszawa', 400000, 'Polska', 0, 40000, 'budynek', '', '', '', '')









    



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
