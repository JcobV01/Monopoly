import os
import random

class Player:
    def __init__(self, stan_konta, posiadlosci):
        self.stan_konta = stan_konta
        self.posiadlosci = posiadlosci

class Board:
    def __init__(self, id, znacznik, nazwa, cena, kraj, zakupiono, podatek, rola, g1, g2, g3, g4, wlasciciel):
        self.id = id
        self.znacznik = znacznik
        self.nazwa = nazwa
        self.cena = cena
        self.kraj = kraj
        self.zakupiono = zakupiono
        self.podatek = podatek
        self.rola = rola
        self.gracz = [g1, g2, g3, g4]
        self.wlasciciel = wlasciciel


gracz1 = Player(2000000, [])
gracz2 = Player(2000000, [])
gracz3 = Player(2000000, [])
gracz4 = Player(2000000, [])

tabelaGraczy = [gracz1, gracz2, gracz3, gracz4]


pole1 = Board(0, 'a', 'Start', 0, 'None', 0, 0, 'specjalne', 'O', 'X', '%', '&', 0)
pole2 = Board(1, 'ą', 'Grenada', 60000, 'Hiszpania', 0, 3000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole3 = Board(2, 'b', 'Sewila', 60000, 'Hiszpania', 0, 3000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole4 = Board(3, 'c', 'Madryt', 60000, 'Hiszpania', 0, 3000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole5 = Board(4, 'ć', 'Bali', 200000, 'Wyspa', 0, 20000, 'wyspa', ' ', ' ', ' ', ' ', 0)
pole6 = Board(5, 'd', 'Hongkong', 100000, 'Chiny', 0, 5000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole7 = Board(6, 'e', 'Pekin', 100000, 'Chiny', 0, 5000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole8 = Board(7, 'ę', 'Szanghaj', 120000, 'Chiny', 0, 6000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole9 = Board(8, 'f', 'Wiezienie', 0, 'None', 0, 0, 'specjalne', ' ', ' ', ' ', ' ', 0)
pole10 = Board(9, 'g', 'Wenecja', 140000, 'Włochy', 0, 7000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole11 = Board(10, 'h', 'Mediolan', 140000, 'Włochy', 0, 7000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole12 = Board(11, 'i', 'Rzym', 160000, 'Włochy', 0, 16000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole13 = Board(12, 'j', 'Szansa', 0, 'None', 0, 0, 'specjalne', ' ', ' ', ' ', ' ', 0)
pole14 = Board(13, 'k', 'Hamburg', 180000, 'Niemcy', 0, 18000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole15 = Board(14, 'l', 'Cypr', 200000, 'Wyspa', 0, 20000, 'wyspa', ' ', ' ', ' ', ' ', 0)
pole16 = Board(15, 'ł', 'Berlin', 200000, 'Niemcy', 0, 20000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole17 = Board(16, 'm', 'Mistrzostwa', 0, 'None', 0, 0, 'specjalne', ' ', ' ', ' ', ' ', 0)
pole18 = Board(17, 'n', 'Londyn', 220000, 'WielkaBrytania', 0, 22000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole19 = Board(18, 'ń', 'Dubaj', 200000, 'Wyspa', 0, 20000, 'wyspa', ' ', ' ', ' ', ' ', 0)
pole20 = Board(19, 'o', 'Sydnay', 240000, 'WielkaBrytania', 0, 24000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole21 = Board(20, 'ó', 'Szansa', 0, 'None', 0, 0, 'specjalne', ' ', ' ', ' ', ' ', 0)
pole22 = Board(21, 'p', 'Chicago', 260000, 'USA', 0, 26000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole23 = Board(22, 'q', 'LasVegas', 260000, 'USA', 0, 26000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole24 = Board(23, 'r', 'NowyJork', 280000, 'USA', 0, 28000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole25 = Board(24, 's', 'Podroz', 0, 'None', 0, 0, 'specjalne', ' ', ' ', ' ', ' ', 0)
pole26 = Board(25, 't', 'Nicea', 200000, 'Wyspa', 0, 20000, 'wyspa', ' ', ' ', ' ', ' ', 0)
pole27 = Board(26, 'u', 'Lyon', 300000, 'Francja', 0, 30000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole28 = Board(27, 'v', 'Paryz', 320000, 'Francja', 0, 32000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole29 = Board(28, 'w', 'Szansa', 0, 'None', 0, 0, 'specjalne', ' ', ' ', ' ', ' ', 0)
pole30 = Board(29, 'x', 'Krakow', 350000, 'Polska', 0, 35000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole31 = Board(30, 'y', 'Podatek', 0, 'None', 0, 0, 'specjalne', ' ', ' ', ' ', ' ', 0)
pole32 = Board(31, 'z', 'Warszawa', 400000, 'Polska', 0, 40000, 'budynek', ' ', ' ', ' ', ' ', 0)

tablicaPol = [pole1, pole2, pole3, pole4, pole5, pole6, pole7, pole8, pole9, pole10, pole11, pole12, pole13, pole14, pole15, pole16, pole17, pole18, pole19, pole20, pole21, pole22, pole23, pole24, pole25, pole26, pole27, pole28, pole29, pole30, pole31]


rightFilds = [pole10, pole11, pole12, pole13, pole14, pole15, pole16]
leftFilds = [pole32, pole31, pole30, pole29, pole28, pole27, pole26]


currentPlayerPosition = [0, 0, 0, 0]

def setBoard():

    os.system('cls')

    leftLetters = ['z', 'y', 'x', 'w', 'v', 'u', 't']
    rightLetters = ['g', 'h', 'i', 'j', 'k', 'l', 'ł']

    

    print(f"┌{'─'*91}┐")
    print(f"│ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ │")
    print(f"│ │ {pole1.gracz[0]}   {pole1.gracz[1]} │ │ {pole2.gracz[0]}   {pole2.gracz[1]} │ │ {pole3.gracz[0]}   {pole3.gracz[1]} │ │ {pole4.gracz[0]}   {pole4.gracz[1]} │ │ {pole5.gracz[0]}   {pole5.gracz[1]} │ │ {pole6.gracz[0]}   {pole6.gracz[1]} │ │ {pole7.gracz[0]}   {pole7.gracz[1]} │ │ {pole8.gracz[0]}   {pole8.gracz[1]} │ │ {pole9.gracz[0]}   {pole9.gracz[1]} │ │")
    print(f"│ │   a   │ │   ą   │ │   b   │ │   c   │ │   ć   │ │   d   │ │   e   │ │   ę   │ │   f   │ │")
    print(f"│ │ {pole1.gracz[2]}   {pole1.gracz[3]} │ │ {pole2.gracz[2]}   {pole2.gracz[2]} │ │ {pole3.gracz[2]}   {pole3.gracz[3]} │ │ {pole4.gracz[2]}   {pole4.gracz[3]} │ │ {pole5.gracz[2]}   {pole5.gracz[3]} │ │ {pole6.gracz[2]}   {pole6.gracz[3]} │ │ {pole7.gracz[2]}   {pole7.gracz[3]} │ │ {pole8.gracz[2]}   {pole8.gracz[3]} │ │ {pole9.gracz[2]}   {pole9.gracz[3]} │ │")
    print(f"│ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ │")

    for i in range(0, 7):
        print(f"│ ┌───────┐{' '*71}┌───────┐ │")
        print(f"│ │ {leftFilds[i].gracz[0]}   {leftFilds[i].gracz[1]} │{' '*71}│ {rightFilds[i].gracz[0]}   {rightFilds[i].gracz[1]} │ │")
        print(f"│ │   {leftLetters[i]}   │{' '*71}│   {rightLetters[i]}   │ │")
        print(f"│ │ {leftFilds[i].gracz[2]}   {leftFilds[i].gracz[3]} │{' '*71}│ {rightFilds[i].gracz[2]}   {rightFilds[i].gracz[3]} │ │")
        print(f"│ └───────┘{' '*71}└───────┘ │")
    
    print(f"│ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ │")
    print(f"│ │ {pole25.gracz[0]}   {pole25.gracz[1]} │ │ {pole24.gracz[0]}   {pole24.gracz[1]} │ │ {pole23.gracz[0]}   {pole23.gracz[1]} │ │ {pole22.gracz[0]}   {pole22.gracz[1]} │ │ {pole21.gracz[0]}   {pole21.gracz[1]} │ │ {pole20.gracz[0]}   {pole20.gracz[1]} │ │ {pole19.gracz[0]}   {pole19.gracz[1]} │ │ {pole18.gracz[0]}   {pole18.gracz[1]} │ │ {pole17.gracz[0]}   {pole17.gracz[1]} │ │")
    print(f"│ │   s   │ │   r   │ │   q   │ │   p   │ │   ó   │ │   o   │ │   ń   │ │   n   │ │   m   │ │")
    print(f"│ │ {pole25.gracz[2]}   {pole25.gracz[3]} │ │ {pole24.gracz[2]}   {pole24.gracz[3]} │ │ {pole23.gracz[2]}   {pole23.gracz[3]} │ │ {pole22.gracz[2]}   {pole22.gracz[3]} │ │ {pole21.gracz[2]}   {pole21.gracz[3]} │ │ {pole20.gracz[2]}   {pole20.gracz[3]} │ │ {pole19.gracz[2]}   {pole19.gracz[3]} │ │ {pole18.gracz[2]}   {pole18.gracz[3]} │ │ {pole17.gracz[2]}   {pole17.gracz[3]} │ │")
    print(f"│ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘ │")
    print(f"└{'─'*91}┘")

    print(currentPlayerPosition)


currentPlayer = 1
currentPlayerSign = "O"

def switchPlayer():
    global currentPlayer
    global currentPlayerSign

    # match currentPlayer:
    #     case 1:
    #         currentPlayer = 2
    #         currentPlayerSign = "X"
    #     case 2:
    #         currentPlayer = 3
    #         currentPlayerSign = "%"
    #     case 3:
    #         currentPlayer = 4
    #         currentPlayerSign = "&"
    #     case 4:
    #         currentPlayer = 1
    #         currentPlayerSign = "O"

    if currentPlayer == 1:
        currentPlayer = 2
        currentPlayerSign = "X"
    elif currentPlayer == 2:
        currentPlayer = 3
        currentPlayerSign = "%"
    elif currentPlayer == 3:
        currentPlayer = 4
        currentPlayerSign = "&"
    elif currentPlayer == 4:
        currentPlayer = 1
        currentPlayerSign = "O"


def dice():
    return [random.randint(1,6), random.randint(1,6)]
        
wylosowane = 0
wybor = 0

def movePlayer():
    global currentPlayer
    global currentPlayerSign

    tablicaPol[currentPlayerPosition[currentPlayer-1]].gracz[currentPlayer-1] = " "

    currentPlayerPosition[currentPlayer-1] += wylosowane[0]+wylosowane[1]

    if currentPlayerPosition[currentPlayer-1] >= 32:
        currentPlayerPosition[currentPlayer-1] -= 32
        tabelaGraczy[currentPlayer-1].stan_konta += 400000
        tablicaPol[currentPlayerPosition[currentPlayer-1]].gracz[currentPlayer-1] = currentPlayerSign

    else:
        tablicaPol[currentPlayerPosition[currentPlayer-1]].gracz[currentPlayer-1] = currentPlayerSign

def tax():
    if tablicaPol[currentPlayerPosition[currentPlayer-1]].zakupiono == 1:
            tabelaGraczy[currentPlayer-1].stan_konta -= tablicaPol[currentPlayerPosition[currentPlayer-1]].podatek
            tabelaGraczy[tablicaPol[currentPlayerPosition[currentPlayer-1]].wlasciciel-1].stan_konta += tablicaPol[currentPlayerPosition[currentPlayer-1]].podatek #chyba działa, przetestować

            print("Pobrano podatek na rzecz właściciela.")





    
    
def buyField():
    if currentPlayerPosition[currentPlayer-1] != 0 and currentPlayerPosition[currentPlayer-1] != 8 and currentPlayerPosition[currentPlayer-1] != 16 and tablicaPol[currentPlayerPosition[currentPlayer-1]].zakupiono == 0:
        tabelaGraczy[currentPlayer-1].stan_konta -= tablicaPol[currentPlayerPosition[currentPlayer-1]].cena
        tabelaGraczy[currentPlayer-1].posiadlosci.append(tablicaPol[currentPlayerPosition[currentPlayer-1]].nazwa)
        print(f"Kupiono pole {tablicaPol[currentPlayerPosition[currentPlayer-1]].nazwa}")
        tablicaPol[currentPlayerPosition[currentPlayer-1]].zakupiono = 1

        #przypisanie gracza do pola

        tablicaPol[currentPlayerPosition[currentPlayer-1]].wlasciciel = currentPlayer
    else:
        print("Nie można kupić tego pola")




while True:
    setBoard() 
    
    if int(wybor) == 1:
        wybor = 0
        wylosowane = dice()


        movePlayer()
        setBoard() 
        tax()

        print(f"Wylosowane liczby to: {wylosowane[0]} i {wylosowane[1]}")
        
        print(f"Gracz: {currentPlayerSign} | Stan konta: {tabelaGraczy[currentPlayer-1].stan_konta} | Pole: {tablicaPol[currentPlayerPosition[currentPlayer-1]].nazwa} | Cena: {tablicaPol[currentPlayerPosition[currentPlayer-1]].cena} | Rola: {tablicaPol[currentPlayerPosition[currentPlayer-1]].rola}")
        
        print("---------------")
        print(f"Stan konta 1 gracza: {tabelaGraczy[0].stan_konta}")
        print(f"Stan konta 2 gracza: {tabelaGraczy[1].stan_konta}")
        print(f"Stan konta 3 gracza: {tabelaGraczy[2].stan_konta}")
        print(f"Stan konta 4 gracza: {tabelaGraczy[3].stan_konta}")
        print("---------------")
        print(f"Pola 1 gracza: {tabelaGraczy[0].posiadlosci}")
        print(f"Pola 2 gracza: {tabelaGraczy[1].posiadlosci}")
        print(f"Pola 3 gracza: {tabelaGraczy[2].posiadlosci}")
        print(f"Pola 4 gracza: {tabelaGraczy[3].posiadlosci}")
        print("---------------")
        
        
        print("Co chcesz zrobić?")
        print("1 - kup pole")
        print("2 - zakończ rundę")

        
        wybor2 = input("Wybór: ")

        if int(wybor2) == 1:
            buyField()

        switchPlayer()


        
    else:
        print("Niepoprawna opcja")
        
    
    print("Co chcesz zrobić?")
    
    while wybor != "1":
        wybor = input("Wybór: ")

    

