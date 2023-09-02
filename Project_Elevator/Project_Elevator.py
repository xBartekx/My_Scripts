import random

print("1 - I")
# 1 - I

def script_1_I():

    start = random.randint(0, 10)                       #<--- Początek funkcji, gdzie deklaruje zmienne sumujące piętra
                                                        #     i nadaje im stan początkowy według scenariusza 1
    sum_diff = start
    sum_dist = start * 2.8

    for f in range(0,1000):                             #<--- Używam pętli aby przeiterować "n" cykli windy

        finish = random.randint(0, 10)                  #<--- Winda pojedzie w losowe miejsce

        while start == finish:                          #<--- Start jest inny niż koniec
            finish = random.randint(0,10)

        diff = abs(start - finish)                      #<--- Jak liczę różnice pięter oraz odległość
        distance = diff * 2.8

        sum_diff = sum_diff + diff                      #<--- Sumowanie pięter i odległości(odległość zaokrąglam do 2 miejsc po przecinku)
        sum_dist = round(sum_dist + distance, 2)
        start = finish                                  #<--- Start windy zaczyna się tam, gdzie skończył się ostatni cykl/podróż


    print("Droga windy przebyta w km:")                 #<--- Printuje wyniki
    print(round(sum_dist/1000, 2))
    print("Ilość przebytych pięter: ")
    print(sum_diff)


script_1_I()                                            #<--- Wywołuję funkcję

print()
print("2 - I")
# 2 - I

def script_2_I():

    start = random.randint(4, 10)                       #<--- Początek funkcji, gdzie deklaruje zmienne sumujące piętra i nadaje im stan początkowy według scenariusza 2
                                                        #     i nadaje im stan początkowy według scenariusza 2
    sum_diff = 0
    sum_dist = 0
    sum_diff_1 = 0
    sum_dist_1 = 0

    for f in range(0,700):                              #<--- Obliczam za pomocą pętli pierwsze 70% perzejazdów

            finish = 0                                  #<--- Winda zawsze kończy przejazd na parterze

            diff = abs(start - finish)
            distance = (start + diff) * 2.8
            sum_diff = sum_diff + start + diff
            sum_dist = round(sum_dist + distance, 2)
            start = random.randint(4, 10)               #<---Winda zabiera ludzi od 4 piętra wzwyż

    start = 0                                           #<--- Winda zaczyna losowe przejazdy tam gdzie skończyły się przejazdy z ludźmi idącymi do pracy, czyli na piętrze 0

    for f2 in range (0, 300):                           #<--- Obliczam za pomocą drugiej pętli pozostałą liczbę losowych cykli według scenariusza

            finish = random.randint(0, 10)

            while start == finish:
                finish = random.randint(0, 10)

            diff = abs(start - finish)
            distance = diff * 2.8
            sum_diff_1 = sum_diff_1 + diff
            sum_dist_1 = round(sum_dist_1 + distance, 2)
            start = finish

    print("Droga windy przebyta w km:")                 #<--- Printuje sumę wyników z dwóch pętli
    print(round((sum_dist + sum_dist_1)/1000,2))
    print("Ilość przebytych pięter: ")
    print(sum_diff + sum_diff_1)

script_2_I()                                            #<--- Wywołuję funkcję


print()
print("3 - I")
# 3 - I


def script_3_I():

    sum_diff = 0
    sum_dist = 0
    sum_diff_1 = 0
    sum_dist_1 = 0

    for f in range(0,700):                                  #<---- Pierwsze 70 % cykli z 1000 to ludzie wracający z pracy/zakupów

        start = 0                                           #<--- Ludzie w tych 70% zawsze zaczynają z parteru
        finish = random.randint(0, 10)

        while start == finish:
            finish = random.randint(0, 10)

        diff = abs(start - finish) + finish
        distance = (start + diff) * 2.8
        sum_diff = sum_diff + diff
        sum_dist = round(sum_dist + distance, 2)

    start = finish                                           #<--- Kolejne 30 % cykli zaczyna się od miejsca gdzie winda zostawiła ostatniego pasażera z pierwszych 70% wracajacych do domu
    for f2 in range(0,300):                                  #<--- Obliczam za pomocą drugiej pętli pozostałą liczbę losowych cykli według scenariusza

        finish = random.randint(0, 10)

        if start == finish:
            finish = random.randint(0, 10)

        diff = abs(start - finish)
        distance = diff * 2.8
        sum_diff_1 = sum_diff_1 + diff
        sum_dist_1 = round(sum_dist_1 + distance, 2)
        start = finish

    print("Droga windy przebyta w km: ")                    #<--- Printuje sumę wyników z dwóch pętli
    print(round((sum_dist + sum_dist_1)/1000,2))
    print("Ilość przebytych pięter: ")
    print(sum_diff + sum_diff_1)

script_3_I()


print()
print("1 - II")
# 1 - II



def script_1_II():

    start = 0
    sum_diff = start                                                         #<-- Parametry początkowe
    sum_dist = start * 2.8
    return_zero_floor = 0

    for f in range(0,1000):

        finish = random.randint(0, 10)                                       #<--- Start inny od zera
        while start == finish:
            finish = random.randint(0,10)

        diff = abs(start - finish) + abs(finish - 0) + return_zero_floor     #<--- Liczenie pięter
        distance = diff * 2.8                                                #<--- Liczenie dystansu
        sum_diff = sum_diff + diff                                           #<--- Suma ogólna pięter zwiększa się z każdą iteracją
        sum_dist = round(sum_dist + distance, 2)                             #<--- Dystans ogólny zwiększa się z każdą iteracją
        start = 0                                                            #<--- Poglądowo - winda wraca zawsze na 5 piętro po użyciu
        start = random.randint(0, 10)                                        #<--- Losuje gdzie pojedzie winda następnym razem
        while start == 0:
            start = random.randint(0, 10)
        return_zero_floor = abs(0 - start)                                   #<--- Zmienna liczy ile pięter pokonuje winda, kiedy wraca na 5 piętro według algorytmu po każdym użyciu

    sum_dist = round(sum_dist/1000, 2)                                       #<--- Zaokrąglam wynik
    print("Droga windy przebyta w km: ")                                     #<--- Printuje wyniki
    print(sum_dist)
    print("Ilość przebytych pięter: ")
    print(sum_diff)

script_1_II()

print()
print("2 - II")
# 2 - II

def script_2_II():

    start = random.randint(4, 10)                                               #<--- Początek funkcji, gdzie deklaruje zmienne sumujące piętra i nadaje im stan początkowy według scenariusza 2

    return_zero_floor = 0                                                       #     i nadaje im stan początkowy według scenariusza 2
    sum_diff = 0
    sum_dist = 0
    sum_diff_1 = 0
    sum_dist_1 = 0

    for f in range(0,700):                                                      #<--- Obliczam za pomocą pętli pierwsze 70% perzejazdów

            finish = 0                                                          #<--- Winda zawsze zwozi ludzi idących do pracy na parter

            diff = abs(start - finish)
            distance = (start + diff) * 2.8
            sum_diff = sum_diff + start + diff
            sum_dist = round(sum_dist + distance, 2)
            start = random.randint(4, 10)                                       #<---Winda zabiera ludzi od 4 piętra wzwyż

    start = 0                                                                   #<--- Winda zaczyna losowe przejazdy tam gdzie skończyły się przejazdy z ludźmi idącymi do pracy, czyli na piętrze 0

    for f2 in range (0, 300):

        finish = random.randint(0, 10)                                          # <--- Start inny od zera
        while start == finish:
            finish = random.randint(0, 10)

        diff = abs(start - finish) + abs(finish - 0) + return_zero_floor        # <--- Liczenie pięter
        distance = diff * 2.8                                                   # <--- Liczenie dystansu
        sum_diff_1 = sum_diff_1 + diff                                          # <--- Suma ogólna pięter zwiększa się z każdą iteracją
        sum_dist_1 = round(sum_dist_1 + distance, 2)                            # <--- Dystans ogólny zwiększa się z każdą iteracją
        start = 0                                                               # <--- Poglądowo - winda wraca zawsze na 5 piętro po użyciu
        start = random.randint(0, 10)                                           # <--- Losuje gdzie pojedzie winda następnym razem
        while start == 0:
            start = random.randint(0, 10)
        return_zero_floor = abs(0 - start)

    print("Droga windy przebyta w km:")                                         #<--- Printuje sumę wyników z dwóch pętli
    print(round((sum_dist + sum_dist_1)/1000,2))
    print("Ilość przebytych pięter: ")
    print(sum_diff + sum_diff_1)

script_2_II()                                                                   #<--- Wywołuję funkcję


print()
print("3 - II")
# 3 - II


def script_3_II():

    return_zero_floor = 0
    sum_diff = 0
    sum_dist = 0
    sum_diff_1 = 0
    sum_dist_1 = 0

    for f in range(0,700):                                                          #<---- Pierwsze 70 % cykli z 1000 to ludzie wracający z pracy/zakupów

        start = 0                                                                   #<--- Ludzie w tych 70% zawsze zaczynają z parteru
        finish = random.randint(0, 10)

        while start == finish:
            finish = random.randint(0, 10)

        diff = abs(start - finish) + finish
        distance = (start + diff) * 2.8
        sum_diff = sum_diff + diff
        sum_dist = round(sum_dist + distance, 2)

    start = 0                                                                       #<--- Kolejne 30 % cykli zaczyna się od parteru, bo winda w algorytmie II zawsze zaczyna od parteru
    for f2 in range(0,300):                                                         #<--- Obliczam za pomocą drugiej pętli pozostałą liczbę losowych cykli według scenariusza

        finish = random.randint(0, 10)

        if start == finish:
            finish = random.randint(0, 10)

        diff = abs(start - finish) + abs(finish - 0) + return_zero_floor            # <--- Liczenie pięter
        distance = diff * 2.8                                                       # <--- Liczenie dystansu
        sum_diff_1 = sum_diff_1 + diff                                              # <--- Suma ogólna pięter zwiększa się z każdą iteracją
        sum_dist_1 = round(sum_dist_1 + distance, 2)                                # <--- Dystans ogólny zwiększa się z każdą iteracją
        start = 0                                                                   # <--- Poglądowo - winda wraca zawsze na 5 piętro po użyciu
        start = random.randint(0, 10)                                               # <--- Losuje gdzie pojedzie winda następnym razem
        while start == 0:
            start = random.randint(0, 10)
        return_zero_floor = abs(0 - start)

    print("Droga windy przebyta w km: ")                                            #<--- Printuje sumę wyników z dwóch pętli
    print(round((sum_dist + sum_dist_1)/1000,2))
    print("Ilość przebytych pięter: ")
    print(sum_diff + sum_diff_1)

script_3_II()


print()
print("1 - III")
# 1 - III

def script_1_III():

    start = 0
    sum_diff = start                                                         #<-- Parametry początkowe
    sum_dist = start * 2.8
    return_five_floor = 0

    for f in range(0,1000):

        finish = random.randint(0, 10)                                       #<--- Start inny od zera
        while start == finish:
            finish = random.randint(0,10)

        diff = abs(start - finish) + abs(finish - 5) + return_five_floor     #<--- Liczenie pięter
        distance = diff * 2.8                                                #<--- Liczenie dystansu
        sum_diff = sum_diff + diff                                           #<--- Suma ogólna pięter zwiększa się z każdą iteracją
        sum_dist = round(sum_dist + distance, 2)                             #<--- Dystans ogólny zwiększa się z każdą iteracją
        start = 5                                                            #<--- Poglądowo - winda wraca zawsze na 5 piętro po użyciu
        start = random.randint(0, 10)                                        #<--- Losuje gdzie pojedzie winda następnym razem
        while start == 5:
            start = random.randint(0, 10)
        return_five_floor = abs(5 - start)                                   #<--- Zmienna liczy ile pięter pokonuje winda, kiedy wraca na 5 piętro według algorytmu po każdym użyciu

    sum_dist = round(sum_dist/1000, 2)                                       #<--- Zaokrąglam wynik
    print("Droga windy przebyta w km: ")                                     #<--- Printuje wyniki
    print(sum_dist)
    print("Ilość przebytych pięter: ")
    print(sum_diff)

script_1_III()

print()
print("2 -III")
# 2 - III

def script_2_III():

    start = random.randint(4, 10)                                               #<--- Początek funkcji, gdzie deklaruje zmienne sumujące piętra i nadaje im stan początkowy według scenariusza 2

    return_five_floor = 0                                                       #     i nadaje im stan początkowy według scenariusza 2
    sum_diff = 0
    sum_dist = 0
    sum_diff_1 = 0
    sum_dist_1 = 0

    for f in range(0,700):                                                        #<--- Obliczam za pomocą pętli pierwsze 70% perzejazdów

            finish = 0                                                          #<--- Winda zawsze zwozi ludzi idących do pracy na parter

            diff = abs(start - finish)
            distance = (start + diff) * 2.8
            sum_diff = sum_diff + start + diff
            sum_dist = round(sum_dist + distance, 2)
            start = random.randint(4, 10)                                       #<---Winda zabiera ludzi od 4 piętra wzwyż

    start = 0                                                                   #<--- Winda zaczyna losowe przejazdy tam gdzie skończyły się przejazdy z ludźmi idącymi do pracy, czyli na piętrze 0

    for f2 in range (0, 300):

        finish = random.randint(0, 10)                                          # <--- Start inny od zera
        while start == finish:
            finish = random.randint(0, 10)

        diff = abs(start - finish) + abs(finish - 5) + return_five_floor        #<--- Liczenie pięter
        distance = diff * 2.8                                                   #<--- Liczenie dystansu
        sum_diff_1 = sum_diff_1 + diff                                          #<--- Suma ogólna pięter zwiększa się z każdą iteracją
        sum_dist_1 = round(sum_dist_1 + distance, 2)                            #<--- Dystans ogólny zwiększa się z każdą iteracją
        start = 5                                                               #<--- Poglądowo - winda wraca zawsze na 5 piętro po użyciu
        start = random.randint(0, 10)                                           #<--- Losuje gdzie pojedzie winda następnym razem
        while start == 5:
            start = random.randint(0, 10)
        return_five_floor = abs(5 - start)                                      #<--- Zmienna liczy ile pięter pokonuje winda, kiedy wraca na 5 piętro według algorytmu po każdym użyciu

    print("Droga windy przebyta w km:")                                         #<--- Printuje sumę wyników z dwóch pętli
    print(round((sum_dist + sum_dist_1)/1000,2))
    print("Ilość przebytych pięter: ")
    print(sum_diff + sum_diff_1)

script_2_III()

print()
print("3 - III")
# 3 - III

def script_3_III():

    return_five_floor = 0
    sum_diff = 0
    sum_dist = 0
    sum_diff_1 = 0
    sum_dist_1 = 0

    for f in range(0,700):                                                          #<---- Pierwsze 70 % cykli z 1000 to ludzie wracający z pracy/zakupów

        start = 0                                                                   #<--- Ludzie w tych 70% zawsze zaczynają z parteru
        finish = random.randint(0, 10)

        while start == finish:
            finish = random.randint(0, 10)

        diff = abs(start - finish) + finish
        distance = (start + diff) * 2.8
        sum_diff = sum_diff + diff
        sum_dist = round(sum_dist + distance, 2)

    start = 0                                                                       #<--- Kolejne 30 % cykli zaczyna się od parteru, bo winda w algorytmie II zawsze zaczyna od parteru
    for f2 in range(0,300):                                                         #<--- Obliczam za pomocą drugiej pętli pozostałą liczbę losowych cykli według scenariusza

        finish = random.randint(0, 10)

        if start == finish:
            finish = random.randint(0, 10)

        diff = abs(start - finish) + abs(finish - 5) + return_five_floor            #<--- Liczenie pięter
        distance = diff * 2.8                                                       #<--- Liczenie dystansu
        sum_diff_1 = sum_diff_1 + diff                                              #<--- Suma ogólna pięter zwiększa się z każdą iteracją
        sum_dist_1 = round(sum_dist_1 + distance, 2)                                #<--- Dystans ogólny zwiększa się z każdą iteracją
        start = 5                                                                   #<--- Poglądowo - winda wraca zawsze na 5 piętro po użyciu
        start = random.randint(0, 10)                                               #<--- Losuje gdzie pojedzie winda następnym razem
        while start == 5:
            start = random.randint(0, 10)
        return_five_floor = abs(5 - start)                                          #<--- Zmienna liczy ile pięter pokonuje winda, kiedy wraca na 5 piętro według algorytmu po każdym użyciu

    print("Droga windy przebyta w km: ")                                            #<--- Printuje sumę wyników z dwóch pętli
    print(round((sum_dist + sum_dist_1)/1000,2))
    print("Ilość przebytych pięter: ")
    print(sum_diff + sum_diff_1)

script_3_III()
