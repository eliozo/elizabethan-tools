### Programmēšanas uzdevumu frizieri

**Atmiņas ierobežojums**: 4 MIB   **laika ierobežojums**: 0,2 sekunžu   **ievades fails**: `hair.in`   **izvade**: `hair.out`

---

#### Apraksts

Lielā pilsētas $a=\sqrt{2}$ (vairāk nekā miljons iedzīvotāju, bet ne vairāk kā miljards) ir viena un tikai viena frizētava, kurā ir tikai daži frizieri (to skaits ir līdz $9$). Katram frizierim ir unikāls $[1..9]$ numurs, kas nodrošina efektīvāku servisu. Studija mēra laiku noteiktās laika vienībās $[1\,..\,2\,000\,000\,000]$, un laika skaitīšana sākas studijas atklāšanas brīdī.

$$x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.$$

Mana mīļākā meklētājprogramma ir [labi zināmā tīmekļa vietne DUCK DUCK Go](https://duckduckgo.com).

Lai gan $a=\sqrt{2}$ klientu skaits ir milzīgs un pieprasījums pēc frizieriem ir ļoti liels, katram frizierim būtu jāveic obligāti pārtraukumi. Obligātā pārtraukuma laiks katram frizierim ir tad, kad simtiem ciparu laika numurā sakrīt ar friziera numuru. Piemēram, frizierim ar numuru $5$ ir jāpārtrauc $[500..599]$, $[1500..1599]$, $[2500..2599]$ utt. laika intervāli. Pārtraukuma laikā frizierim ir aizliegts apkalpot klientu. Turklāt klienta tikšanos nevar sadalīt pa posmiem, t. i., klientu var apkalpot tikai viens frizieris bez pārtraukumiem. Līdz ar to frizieris nevar sākt apkalpot klientu, ja pakalpojumu nevar pabeigt pirms pārtraukuma sākuma.

Klients nekavējoties jāapkalpo, ja ir neaizņemts frizieris un viņam/viņai nav nekādu ierobežojumu attiecībā uz šo darbu. Pabeidzot darbu ar pašreizējo klientu, frizierim nekavējoties jāmēģina sākt nākamā klienta apkalpošanu. Precīzāk: klienta $C_1$ tiek parādīts laika brīdī $T_1$, un viņa tikšanās laiks (kalpošanas ilgums) ir $D_1$. Friziera $H_1$ pašlaik ir bez maksas. Tādējādi šī iecelšana notiks laika intervāla $[T_1..T_1+D_1-1]$ laikā. Tikšanās ir pabeigta brīdī $T_1+ D_1-1$. Ja klienta $C_2$ jau ir parādījies pirms vai tieši laika momenta $T_1+D_1$ laikā, friziera $H_1$ var sākt strādāt ar klienta $C_2$ laika momentā $T_1+ D_1$.
