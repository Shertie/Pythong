# Stworzyć symulację gry w wojnę dla różnej ilości graczy oraz początkowych talii.
# Gra powinna zawierać klasy:
# - karta
# - talia
# - gracz (ręka)
# W przypadku gdyby zadanie było zbyt złożone na początek, można zrobić wersję gry, która rozegra
# tylko jedną rundę (do skończenia jeden raz rozdanych kart)
# Tworząc program pamiętajcie o zachowaniu zasad programowania obiektowego (w skrócie wszystko
# powinno jak najbardziej odwzorowywać realny przebieg gry)


# while True:
#     try:
#         ilosc_graczy = int(input('ilość graczy wynosi: '))
#         if ilosc_graczy < 2:
#             print("error, liczba graczny nie może być mniejsza od 2")
#         else:
#             gracze = []
#             for i in range(ilosc_graczy):
#                 nick_gracza = input("podaj nickname gracza nr " + str(i + 1) + ": ")
#                 gracze.append(nick_gracza)
#         break
#     except:
#         print("error, wartość nie jest liczbą całkowitą!")


class Gracz:
    def __init__(self, nickname):
        self.nickname = nickname

class Talia:
    def __init__(self,  ilosc_kart):
        self.ilosc_kart = ilosc_kart

    def tasowanie(self):


class Karta:
    def __init__(self, wartosc):
        self.wartosc = wartosc
    talia = {"AS_KIER":13,"AS_CARO":13,"AS_PIK":13,"AS_TREFL":13,"KROL_KIER":12,"KROL_CARO":12,"KROL_PIK":12,"KROL_TREFL":12, "DAMA_KIER":11,"DAMA_CARO":11,"DAMA_PIK":11,"DAMA_TREFL":11,
             "JOPEK_KIER":10,"JOPEK_CARO":10,"JOPEK_PIK":10,"JOPEK_TREFL":10, "10_KIER":9,"10_CARO":9,"10_PIK":9,"10_TREFL":9,"9_KIER":8,"9_CARO":8,"9_PIK":8,"9_TREFL":8,
             "8_KIER":7,"8_CARO":7,"8_PIK":7,"8_TREFL":7,"7_KIER":6,"7_CARO":6,"7_PIK":6,"7_TREFL":6, "6_KIER":5,"6_CARO":5,"6_PIK":5,"6_TREFL":5, "5_KIER":4,"5_CARO":4,"5_PIK":4,"5_TREFL":4
             , "4_KIER":3,"4_CARO":3,"4_PIK":3,"4_TREFL":3, "3_KIER":2,"3_CARO":2,"3_PIK":2,"3_TREFL":2, "2_KIER":1,"2_CARO":1,"2_PIK":1,"2_TREFL":1}


