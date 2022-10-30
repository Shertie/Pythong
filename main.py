# Stworzyć symulację gry w wojnę dla różnej ilości graczy oraz początkowych talii.
# Gra powinna zawierać klasy:
# - karta
# - talia
# - gracz ( ręka )
# W przypadku gdyby zadanie było zbyt złożone na początek, można zrobić wersję gry, która rozegra
# tylko jedną rundę (do skończenia jeden raz rozdanych kart)
# Tworząc program pamiętajcie o zachowaniu zasad programowania obiektowego (w skrócie wszystko
# powinno jak najbardziej odwzorowywać realny przebieg gry)



def ilosc_graczy():
    while True:
        try:
            ilosc_graczy = int(input('ilość graczy wynosi: '))
            if ilosc_graczy < 2:
                print("error, liczba graczny nie może być mniejsza od 2")
            else:
                return ilosc_graczy
        except:
            print("error, wartość nie jest liczbą całkowitą!")



ilosc_graczy=ilosc_graczy()

class Gracz():
    def __init__(self, nickname):
        self.nickname = nickname

gracze = []
for i in range(ilosc_graczy):
    gracz = input("podaj nickname gracza nr "+str(i+1)+": ")
    gracze.append(gracz)




