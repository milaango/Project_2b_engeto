"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Milan Angelis
email: milanangelis@seznam.cz
"""


def zkontroluj_vstup(volba: str, aktualni_pole: list) -> bool:
    """
    Funkce, která kontroluje podmínky pro volbu políčka v hracím poli:
    - zda je volba celé číslo mezi 1 a 9 včetně,
    - zda již políčko není obsazené.

    :param volba: numerický řetězec reprezentující políčko v hracím poli
    :type volba: str
    :param aktualni_pole: aktuální hrací pole uložené v listu
    :type aktualni_pole: list
    :return: True, pokud jsou splněny všechny podmínky, jinak False
    :rtype: bool

    :Example:
    >>> splneni_podminek = zkontroluj_vstup(
    ...     "4", ["o", "x", " ", " ", " ", " ", " ", " ", " "]
    ... )
    >>> splneni_podminek
    True
    """

    if not volba.isdigit():
        print("Toto není celé číslo.")
        return False
    
    elif int(volba) < 1 or int(volba) > 9:
        print("Číslo musí být větší nebo rovno 1 a menší nebo rovno 9.")
        return False
    
    elif (
        "o" == aktualni_pole[int(volba) - 1] 
        or "x" == aktualni_pole[int(volba) - 1]
    ):
        print("Tato pozice je obsazena.")
        return False
    
    else:
        return True


def tah(hracuv_symbol: str, pozice: str, aktualni_pole: list) -> list:
    """
    Funkce, která zpracovává vstup od hráče (hráčův symbol a pozici)
    a aktuální hrací pole uložené v listu, vrací nové hrací pole v listu
    a ukázku pole po tahu.

    :param hracuv_symbol: řetězec reprezentující daný symbol hráče
    :type hracuv_symbol: str
    :param pozice: numerický řetězec (str), které reprezentuje 
        políčko v hracím poli, kam hráč umisťuje svůj symbol
    :type pozice: str
    :param aktualni_pole: aktuální hrací pole uložené v listu
    :type aktualni_pole: list
    :return: dvojice s novým hracím polem uložené v listu 
        a ukázkou hracího pole pro hráče
    :rtype: list
    """

    pole = aktualni_pole
    pole[int(pozice) - 1] = hracuv_symbol
    nove_hraci_pole = pole

    return [
        nove_hraci_pole,
        f"""
+---+---+---+
| {pole[0]} | {pole[1]} | {pole[2]} |
+---+---+---+
| {pole[3]} | {pole[4]} | {pole[5]} |
+---+---+---+
| {pole[6]} | {pole[7]} | {pole[8]} |
+---+---+---+
""",
    ]


def zkontroluj_tah(hracuv_symbol, pole):
    """
    Funkce, která ověřuje, zdali se hráči aktuálním tahem podařilo umístit
    tři symboly za sebou (ve směru vodorovném, svislém či diagonálním).

    :param hracuv_symbol: řetězec reprezentující daný symbol hráče
    :type hracuv_symbol: str
    :param pole: aktuální hrací pole uložené v listu
    :type pole: list
    :return: True, pokud jsou umístěny tři symboly v jednom
        směru, jinak False
    :rtype: bool

    :Example:
    >>> overeni_viteze = zkontroluj_tah(
    ...     "o", ["x", "x", "o", " ", "o", "o", "x", " ", "o"]
    ... )
    >>> overeni_viteze
    True
    """

    vitezne_kombinace = (
        [0, 4, 8], [2, 4, 6], [0, 1, 2], [3, 4, 5], 
        [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8]
        )
    
    for kombinace in vitezne_kombinace:
            if (
                pole[kombinace[0]] == pole[kombinace[1]] 
                == pole[kombinace[2]] == hracuv_symbol
                ):
                return True

    return False


# Vytisknutí úvodu a prázdného hracího pole:

print(
    f"""
Vítejte ve hře Tic Tac Toe
============================================
PRAVIDLA HRY:
V každém kole hráč umisťuje symbol (o nebo x)
do jednoho čtverečku v hracím poli 
o rozměrech 3x3 čtverečky. 
VÍTĚZEM se stává ten, kdo úspešně umístí
za sebou své tři symboly ve směru:
* vodorovném,
* šikmém,
* či diagonálním.
pozn.: Hráči zadávají čísla od 1 do 9,
která reprezentují jednotlivé čtverečky,
z nichž je pole složeno.
============================================
Nechť hra započne!
--------------------------------------------
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
"""
)


# Počáteční hrací pole uložené do listu a sada kamenů (symbolů) v listu:
hraci_pole = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
poradi_tahu = ["o", "x", "o", "x", "o", "x", "o", "x", "o"]

# For cyklus pro 9 průchodů (počet čtverců k dispozici v hracím poli):
for symbol in range(len(poradi_tahu)):
    print("=" * 44)
    volba_hrace = input(f"Hráči {poradi_tahu[symbol]}, zvol pole: ")
    print("=" * 44)

    # Kontrola formátu vstupu a obsazenosti pole přes uživatelskou funkci 
    # zkontrolujvstup(), pokud je volba neplatná, je hráč vyzván k nápravě:
    
    while not zkontroluj_vstup(volba_hrace, hraci_pole):
        volba_hrace = input("Zvol znovu pole: ")
        print("=" * 44)

    # Samotný tah hráče přes uživatelskou funkci tah(), 
    # kam vkládáme symbol a volbu hráče (číslo) a aktuální hrací pole v listu;
    # získáme aktualizované hrací pole v listu a ukázku současné podoby pole:
    
    hraci_pole, ukazka_pole = tah(
        poradi_tahu[symbol], int(volba_hrace), hraci_pole
        )
    print(ukazka_pole)

    # Kontrola, zdali současný tah hráče vede k jeho vítězství
    # pomocí funkce zkontroluj_tah(), kam vkládáme symbol hráče a aktuální 
    # hrací pole v listu:

    if zkontroluj_tah(poradi_tahu[symbol], hraci_pole):
        print("=" * 44)
        print(f"Gratuluji, hráč {poradi_tahu[symbol]} zvítězil!")
        print("=" * 44)
        break

else:
    # Pokud cyklus proběhl bez přerušení (nikdo nezvítězil), nastává remíza:
    print("=" * 44)
    print("Remíza!")
    print("=" * 44)
