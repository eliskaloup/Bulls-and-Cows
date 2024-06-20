# Game Bulls and Cows


---------------------------------------------

**Popis projektu**

Program simuluje hru Bulls and Cows. Po vypsání úvodního textu uživatel hádá náhodně vygenerované čtyřciferné číslo. Hru je možné libovolněkrát opakovat. Doplnila jsem možnost počtu pokusů, které si uživatel může sám nastavit a zároveň mu po uhodnutí program napíše, kolik mu zbývá pokusů.

Program funguje následovně:

- Program pozdraví užitele a vypíše úvodní text.
- Program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0).
- Uživatel si vybere požadovaný počet pokusů ve hře (počty životů).
- Hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla, pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky.
  Když taková situace nastane, tak se nepovolený input nebude počítávat jako počet pokusů.
- Program následně vyhodnotí tip uživatele.
- Dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). Vrácené ohodnocení bere ohled na jednotné a množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows).
- Po vypočítání počtu bulls/cows se také zobrazí zbývající počet pokusů ve hře.
- Hra končí výhrou = uhodnutím čísla a nebo po uplynutí zvoleného počtu pokusů.
