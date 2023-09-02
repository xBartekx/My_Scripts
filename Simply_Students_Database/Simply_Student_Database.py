from tabulate import tabulate

def open_file(a):                                                                                                       #<--- Na początku jest napisanych pięć funkcji do wywoływania odpowiednich funkcjonalności
      with open(a, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
            studenci = [line.split(',') for line in lines]
            studenci = [(n, s, str(i), str(g)) for n, s, i, g in studenci]
            print(lines)

def print_database(studenci):
    print(tabulate(studenci, tablefmt="heavy_grid"))                                                                    #<--Formatowanie danych z pliku do tabeli

def add_student(a):
      f = open(a, "a")
      print("Wprowadź dane studenta według następującego schematu: imię, nazwisko,"                                     #<-- Trzeba podać dane nowego studenta dokładnie tak jak w przykładzie
            " nr. albumu, ocena. Przykład: Jan, Nowak, 456, 4.5")
      new_student = str(input())
      f.write(new_student)
      f.close()

def remove_student(a):
      print("Podaj nr. Albumu:")
      remove = str(input())
      with open(a, "r") as f:
            lines = f.readlines()
      with open(a, "w") as f:
            for line in lines:
                  if remove in line:
                        '\b'
                        continue
                  else:
                        f.write(line)

def save_file(a):
      with open(a, "r") as f:
            lines = f.readlines()
      with open(a, "w") as f:
            for line in lines:
                  f.write(line)


options = 'start'                                                                                                       #<--Tutaj jest domyślny argument do odpalenia pętli w programie. Później już użytkownik wprowadza input'a

a = '...\Projekt\Studenci.csv'                                             #<--Tutaj aby było łatwiej zacząć wpowadziłem swoją ścieżkę początkową. Trzeba zmienić na swoją.

while options != "6":                                                                                                   #<--Tutaj zaczyna się program działający w pętli

      with open(a, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
            studenci = [line.split(',') for line in lines]
            studenci = [(n, s, str(i), str(g)) for n, s, i, g in studenci]

      print("Witaj w bazie danych studentów. Co chcesz zrobić?", "1.Dodaj studenta ", "2.Usuń studenta ",
      "3.Wyświetl studentów ", "4.Zapisz do pliku ", "5.Wczytaj z pliku", "6.Zakończ działanie programu ", sep='\n' )

      options = input()

      if options == '1':                                                                                                #<--Tutaj zaczynają się instrukcje warunkowe przypisane do konkretnych opcji z menu
           add_student(a)

      elif options == '2':
            remove_student(a)

      elif options == '3':
            print_database(studenci)

      elif options == '4':
            save_file(a)

      elif options == '5':
            print("Użyć domyślnej bazy danych? tak/nie: ")                                                              #<--Domyślna ścieżka to ta początkowa przypisana do zmiennej 'a'
            choose = input()
            if choose == 'tak':
                  a = a
            else:
                  print("Wpisz pomiędzy apostrofy  ' '  ścieżkę do Twojej bazy danych: ")                               #<--Tutaj można wpisać nową ścieżkę. Tylko nie można się pomylić, bo inaczej program złapie błąd.
                  b = str(input())
                  open_file(a)
                  a = b

      elif options == '6':                                                                                              #<--Program kończy działanie
            exit()

      else:
            pass                                                                                                        #<--Jak się wpisze coś innego to pętla wraca do początku i znów pokazuje wybór w menu



