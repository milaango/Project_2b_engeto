# Tic Tac Toe (Piškvorky)

Druhý projekt v rámci Python Akademie od ENGETO.

## O projektu
Jedná se o jednoduchou konzolovou hru pro dva hráče. Hráči se střídají v zadávání tahů do konzole a jejich cílem je umístit tři své symboly (`o` nebo `x`) do jedné řady (vodorovně, svisle či diagonálně).

## Požadavky na spuštění
Je doporučena verze Pythonu 3.6 nebo vyšší. Projekt nevyžaduje žádné externí knihovny; stačí jej spustit v Terminálu či IDE dle vlastního výběru.

## Průběh hry
Po spuštění projektu jsou hráčům zobrazena pravidla a následně je první hráč (`o`) vyzván k umístění prvního symbolu do hracího pole. Jednotlivá políčka hracího pole jsou reprezentována čísly 1 až 9:

```
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
```
Po zadání čísla je příslušné políčko obsazeno symbolem hráče. Následuje tah druhého hráče (`x`) a postupně se celý proces opakuje, dokud
(a) jeden z hráčů neumístí tři své symboly do řady ve vodorovném, svislém či diagonálním směru, či (b) není celé hrací pole obsazeno symboly. V případě (a) je vítězem ten hráč, který uvedeným způsobem umístil své symboly, v případě (b) nastává remíza.

### Ošetření neplatných tahů:
V případě, že hráč zadá nesprávně políčko, je vypsáno upozornění a hráč je znovu vyzván k volbě. Ověření správnosti se skládá z:
- kontroly, zda je hráčova volba celé číslo v intervalu <1; 9>,
- kontroly, zda je políčko, které hráč vybral, neobsazené.

## Ukázka průběhu
```
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

============================================
Hráči o, zvol pole: 5
============================================

+---+---+---+
|   |   |   |
+---+---+---+
|   | o |   |
+---+---+---+
|   |   |   |
+---+---+---+

============================================
Hráči x, zvol pole: 2
============================================

...

+---+---+---+
| o | x | o |
+---+---+---+
| x | o |   |
+---+---+---+
| o |   | x |
+---+---+---+

============================================
Gratuluji, hráč o zvítězil!
============================================
```