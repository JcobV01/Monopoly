import os
import random
import sys

#klasa gracz, klasa plansza i ich obiekty

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

gracz1 = Player(700000, [])
gracz2 = Player(700000, [])
gracz3 = Player(700000, [])
gracz4 = Player(700000, [])

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
pole17 = Board(16, 'm', 'Impreza', 0, 'None', 0, 0, 'specjalne', ' ', ' ', ' ', ' ', 0)
pole18 = Board(17, 'n', 'Londyn', 220000, 'WielkaBrytania', 0, 22000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole19 = Board(18, 'ń', 'Dubaj', 200000, 'Wyspa', 0, 20000, 'wyspa', ' ', ' ', ' ', ' ', 0)
pole20 = Board(19, 'o', 'Sydnay', 240000, 'WielkaBrytania', 0, 24000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole21 = Board(20, 'ó', 'Szansa', 0, 'None', 0, 0, 'specjalne', ' ', ' ', ' ', ' ', 0)
pole22 = Board(21, 'p', 'Chicago', 260000, 'USA', 0, 26000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole23 = Board(22, 'q', 'LasVegas', 260000, 'USA', 0, 26000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole24 = Board(23, 'r', 'NowyJork', 280000, 'USA', 0, 28000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole25 = Board(24, 's', 'Pole strzeżone', 0, 'None', 0, 0, 'specjalne', ' ', ' ', ' ', ' ', 0)
pole26 = Board(25, 't', 'Nicea', 200000, 'Wyspa', 0, 20000, 'wyspa', ' ', ' ', ' ', ' ', 0)
pole27 = Board(26, 'u', 'Lyon', 300000, 'Francja', 0, 30000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole28 = Board(27, 'v', 'Paryz', 320000, 'Francja', 0, 32000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole29 = Board(28, 'w', 'Szansa', 0, 'None', 0, 0, 'specjalne', ' ', ' ', ' ', ' ', 0)
pole30 = Board(29, 'x', 'Krakow', 350000, 'Polska', 0, 35000, 'budynek', ' ', ' ', ' ', ' ', 0)
pole31 = Board(30, 'y', 'Podatek', 0, 'None', 0, 0, 'specjalne', ' ', ' ', ' ', ' ', 0)
pole32 = Board(31, 'z', 'Warszawa', 400000, 'Polska', 0, 40000, 'budynek', ' ', ' ', ' ', ' ', 0)

#tablice z obiektami żeby można było się po numerach odwoływać

tablicaPol = [pole1, pole2, pole3, pole4, pole5, pole6, pole7, pole8, pole9, pole10, pole11, pole12, pole13, pole14, pole15, pole16, pole17, pole18, pole19, pole20, pole21, pole22, pole23, pole24, pole25, pole26, pole27, pole28, pole29, pole30, pole31]
tabelaGraczy = [gracz1, gracz2, gracz3, gracz4]

#tabele pomocnicze do rysowania planszy (boczne ściany)

rightFilds = [pole10, pole11, pole12, pole13, pole14, pole15, pole16]
leftFilds = [pole32, pole31, pole30, pole29, pole28, pole27, pole26]

#aktualne pozycje graczy

currentPlayerPosition = [0, 0, 0, 0]

def setBoard():
    #rysowanie planszy
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

#potrzebne zmienne

currentPlayer = 1
currentPlayerSign = "O"
wylosowane = 0
wybor = 0
infoText = ""

def switchPlayer():
    #przełączanie gracza
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
    #losowanie ilości pól na 2 kostki
    return [random.randint(1,6), random.randint(1,6)]
        
def chance():
    #losowanie od 1 do 50000 potrzebne do dodawania pieniędzy na polu szansa
    return random.randint(1, 50000)

def info():
    #funkcja do wyświetlania komunikatów
    if infoText != "":
        print(infoText)

def taxField():
    #podatki
    global infoText
    tabelaGraczy[currentPlayer-1].stan_konta -= tabelaGraczy[currentPlayer-1].stan_konta*0.1
    infoText = "Pobrano podatek"

def getMoney():
    #dodanie graczowi stającemu na polu impreza po 50k od każdego gracza
    global infoText
    for i in tabelaGraczy:
        i.stan_konta -= 50000
    
    tabelaGraczy[currentPlayer-1].stan_konta += 200000
    infoText = "Dostałeś od każdego gracza 50k"

def protectedField():
    #cofnięcie o randomową ilość pól gracza który stanął na polu strzeżonym
    global infoText
    randomNb = random.randint(1, 12)
    currentPlayerPosition[currentPlayer-1] -= randomNb
    infoText = f"Trafiłeś na pole strzeżone - zostałeś cofnięty o {randomNb} pól"

def jail():
    #przeniesienie z więzienia na start
    global infoText
    tablicaPol[currentPlayerPosition[currentPlayer-1]].gracz[currentPlayer-1] = " "
    currentPlayerPosition[currentPlayer-1] = 0
    infoText = "Stanąłeś na polu więzienie - zostałeś deportowany na pole start"

def checkWin():
    a = 0
    for i in tabelaGraczy[currentPlayer-1].posiadlosci:
        #sprawdzanie kurortów
        if i == 'Cypr' or i == 'Nicea' or i == 'Dubaj' or i == 'Bali':
            a += 1

        if a == 4:
            os.system('cls')
            print(f"Wygrał gracz {currentPlayerSign}")
            sys.exit(0)

        #sprawdzanie monopoli

    help = [0, 0, 0, 0, 0, 0, 0, 0]
    monopole = [0, 0, 0, 0, 0, 0, 0, 0]
    o = 0

    for i in tabelaGraczy[currentPlayer-1].posiadlosci:
        if i == 'Grenada' or i == 'Sewila' or i == 'Madryt':
            help[0] += 1
        elif i == 'Hongkong' or i == 'Pekin' or i == 'Szanghaj':
            help[1] += 1
        elif i == 'Wenecja' or i == 'Mediolan' or i == 'Rzym':
            help[2] += 1
        elif i == 'Hamburg' or i == 'Berlin':
            help[3] += 1
        elif i == 'Londyn' or i == 'Sydnay':
            help[4] += 1
        elif i == 'Chicago' or i == 'LasVegas' or i == 'NowyJork':
            help[5] += 1
        elif i == 'Lyon' or i == 'Paryz':
            help[6] += 1
        elif i == 'Krakow' or i == 'Warszawa':
            help[7] += 1 

        if help[0] == 3:
            monopole[0] = 1
        elif help[1] == 3:
            monopole[1] = 1
        elif help[2] == 3:
            monopole[1] = 1
        elif help[3] == 2:
            monopole[1] = 1
        elif help[4] == 2:
            monopole[1] = 1
        elif help[5] == 3:
            monopole[1] = 1
        elif help[6] == 2:
            monopole[1] = 1
        elif help[7] == 2:
            monopole[1] = 1
        
        for j in monopole:
            o += j
            if o == 1:
                os.system('cls')
                print(f"Wygrał gracz {currentPlayerSign}")
                sys.exit(0)

def movePlayer():
    #poruszanie się pionkami i sprawdzanie pól
    global currentPlayer
    global currentPlayerSign
    global infoText

    if tabelaGraczy[currentPlayer-1].stan_konta > -1:

        #zerowanie poprzedniego pola gracza

        tablicaPol[currentPlayerPosition[currentPlayer-1]].gracz[currentPlayer-1] = " "
        currentPlayerPosition[currentPlayer-1] += wylosowane[0]+wylosowane[1]

        #pola specjalne - wywołanie funkcji

        if currentPlayerPosition[currentPlayer-1] == 12 or currentPlayerPosition[currentPlayer-1] == 20 or currentPlayerPosition[currentPlayer-1] == 28:
            tabelaGraczy[currentPlayer-1].stan_konta += chance()
        elif currentPlayerPosition[currentPlayer-1] == 8:
            jail()
        elif currentPlayerPosition[currentPlayer-1] == 16:
            getMoney() 
        elif currentPlayerPosition[currentPlayer-1] == 24:
            protectedField()
        elif currentPlayerPosition[currentPlayer-1] == 30:
            taxField()

        #skok z przez start

        if currentPlayerPosition[currentPlayer-1] > 31:
            currentPlayerPosition[currentPlayer-1] -= 32
            tabelaGraczy[currentPlayer-1].stan_konta += 100000
            tablicaPol[currentPlayerPosition[currentPlayer-1]].gracz[currentPlayer-1] = currentPlayerSign
        else:
            tablicaPol[currentPlayerPosition[currentPlayer-1]].gracz[currentPlayer-1] = currentPlayerSign
    else:
        infoText = "Jesteś bankrutem - nie grasz"
        currentPlayerPosition[currentPlayer-1] = 0

def tax():
    #podatek od stanięcia na polu innego gracza
    if tablicaPol[currentPlayerPosition[currentPlayer-1]].zakupiono == 1:
            tabelaGraczy[currentPlayer-1].stan_konta -= tablicaPol[currentPlayerPosition[currentPlayer-1]].podatek
            tabelaGraczy[tablicaPol[currentPlayerPosition[currentPlayer-1]].wlasciciel-1].stan_konta += tablicaPol[currentPlayerPosition[currentPlayer-1]].podatek

def buyField():
    #kupowanie pola
    if currentPlayerPosition[currentPlayer-1] != 0 and currentPlayerPosition[currentPlayer-1] != 8 and currentPlayerPosition[currentPlayer-1] != 16 and currentPlayerPosition[currentPlayer-1] != 12 and currentPlayerPosition[currentPlayer-1] != 20 and currentPlayerPosition[currentPlayer-1] != 24 and currentPlayerPosition[currentPlayer-1] != 28 and currentPlayerPosition[currentPlayer-1] != 30 and tablicaPol[currentPlayerPosition[currentPlayer-1]].zakupiono == 0 and tabelaGraczy[currentPlayer-1].stan_konta > tablicaPol[currentPlayerPosition[currentPlayer-1]].cena:
        tabelaGraczy[currentPlayer-1].stan_konta -= tablicaPol[currentPlayerPosition[currentPlayer-1]].cena
        tabelaGraczy[currentPlayer-1].posiadlosci.append(tablicaPol[currentPlayerPosition[currentPlayer-1]].nazwa)
        print(f"Kupiono pole {tablicaPol[currentPlayerPosition[currentPlayer-1]].nazwa}")
        tablicaPol[currentPlayerPosition[currentPlayer-1]].zakupiono = 1

        #przypisanie gracza do pola

        tablicaPol[currentPlayerPosition[currentPlayer-1]].wlasciciel = currentPlayer
    else:
        print("Nie można kupić tego pola")

#główna pętla gry, wywoływanie funkcji i wypisywanie informacji

while True:
    setBoard() 
    
    if wybor == '1':
        wybor = 0
        wylosowane = dice()

        movePlayer()
        setBoard() 
        tax()
        

        print(f"Wylosowane liczby to: {wylosowane[0]} i {wylosowane[1]}")

        info()
        infoText = ""
        
        print("---------------")
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
        print("reszta - zakończ rundę")

        
        wybor2 = input("Wybór: ")

        if wybor2 == '1':
            buyField()
            checkWin()

        switchPlayer()
        


    print(" ")  
    print("1 - rzut kostką")
    print("Co chcesz zrobić?")
    
    while wybor != "1":
        
        wybor = input("Wybór: ")

    

