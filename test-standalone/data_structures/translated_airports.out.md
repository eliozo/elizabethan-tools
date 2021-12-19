### Programmēšanas laboratorija: lidostas

**RAM atmiņa**: 10 MB   **laika**: 10 sekunžu   **ievade**: `lidostas.in`   **izvade**: `lidostas.out`

---

#### Apraksts

Lai piesaistītu jaunus pasažierus, nacionālā aviokompānija organizēja loteriju. Loterijas balva, ko piedāvā, lai ceļotu no jebkuras lidostas uz jebkuru citu – ar pārskaitījumiem, ja pasažieris tos vēlas. Turklāt uzvarētājs saņem arī 1000 eiro. Lai noteiktu ceļojuma ierobežojumus, uzvarētājs varēja izmantot noteiktu lidojumu ne vairāk kā vienu reizi, un katru minūti, ko viņš pavada lidostā, viņam maksā 1 eiro. Kad uzvarētājs zaudē 1000 eiro prēmiju, viņš pats maksā par uzturēšanos lidostās.

Viens lidojums ir savienojums no vienas lidostas uz citu noteiktā stundā un minūtē. Citā laikā lidojumu starp tiem pašiem galapunktiem uzskata par citu lidojumu. Tie paši lidojumi atkārtojas dienu no dienas.

Lai pārvietotos starp diviem lidojumiem, pasažierim lidostā ir jāpavada vismaz 1 minūte. Proti, ja pasažieris ierodas `plkst. 12.34`, tad plkst. `12.35`/viņš var izlidot ar citu reisu. Visi pulksteņa laiki ir rakstīti formātā `HH: MM`, kur `HH` nozīmē stundas `00. 23` (vajadzības gadījumā priekšā ar nulli) un `MM` apzīmē minūtes `00. 59` (vajadzības gadījumā arī iepriekš ar nulli).

Katrai konkrētajai lidostai katrā minūtē nav vairāk par vienu izlidojošu reisu; vienlaicīgi nevar izlidot divi reisi.

Īsākais lidojuma ilgums ir 30 minūtes; garākais ilgums ir 23 stundas un 59 minūtes. Ja ielidošanas laiks ir mazāks par izlidošanas laiku, ielidošana notiek nākamajā dienā. Visi laiki tiek rakstīti vienā laika joslā - [Griničas vidējais laiks](https://en.wikipedia.org/wiki/Greenwich_Mean_Time).

Loterijā uzvarēja meitene vārdā Fortūna. Viņa gribēja sasniegt savu galamērķi, ietaupot bonusa naudu (un arī savu naudu). Tā kā viņa nezināja, kā atrast optimālo maršrutu, Fortune izvēlējās šādu stratēģiju: Ierodoties jebkurā lidostā, viņa pēc iespējas ātrāk izlidoja (un, sasniedzot galamērķi, pārstāja lidot). Šādā veidā viņa cerēja maksāt mazāk naudas par gaidīšanu lidostās.

Uzdevums ir noteikt, vai Fortune var sasniegt savu galamērķi, šādi ceļodama. Risinājumam ir jāizvada pilns maršruts (maršruts ar visiem lidojumiem) vai jāpaziņo, ka tas nav iespējams.

Sākotnējā lidostā ir vismaz viens izejošais reiss, ir zināms, ka Fortune var pamest šo lidostu. Ir zināms, ka visām $n$ lidostām ir unikāli numuri no $1$ līdz $n$. Kopējais lidojumu skaits nepārsniedz 20\ 000 $.



#### Ievade:

Ievades faila pirmajā rindā ir norādīts lidostu skaits. Otrajā līnijā ir izcelsmes un galamērķa lidostas. 3. rindā norādīts ierašanās laiks izcelsmes lidostā. (var atstāt, sākot no ierašanās laika plus 1 minūte). Pēc tam ir līnijas, kas apraksta lidojumus.

```c
Lidostu sākuma beigu laiks no līdz n Flight_1... Flight_n... 0```

* `Lidostas` — lidostu skaits (nepārsniedz USD 20\ 000); katrai lidostai ir unikāls numurs starp $1$ un šo numuru.
* `Sākums` — tās lidostas numurs, kurā sākas maršruts.
* `Beigas` – lidostas numurs, kas ir plānotais galamērķis.
* `Laiks` - ierašanās sākuma lidostā, rakstīta formātā `HH: MM`.
* `No` – izlidošanas lidostas numurs attiecīgajam lidojumam.
* `Līdz` – ielidošanas lidostas numurs attiecīgajam lidojumam.
* `N` – šajā rindā uzskaitīto lidojumu skaits.
* `Flight_i` - izlidošanas un ielidošanas laiks formātā `HH: MM-HH: MM`
* `0` - ievades fails vienmēr tiek pārtraukts ar rindu, kurā ir viens cipars 0

Līnijām ar lidojumiem var būt jebkurš pasūtījums.   Lidojumus starp tām pašām divām lidostām var saņemt vienā vai vairākās ievades līnijās.   Viens un tas pats lidojums nekad netiek uzskaitīts divreiz.

Pieņemsim, ka ievades dati ir pareizi, tie vienmēr izmanto norādīto formātu un atbilst problēmas apraksta ierobežojumiem.


#### Izvade:

Ja ir iespējams sasniegt galamērķi, izvades datnē jānorāda sākumlidosta un ierašanās laiks šajā lidostā. Pēc šī saraksta pilns maršruts, kurā redzams viens reiss katrā līnijā.

```c
Sākuma laiks no - > līdz lidojumam...```

* `Sākums` — lidostas numurs, kurā sākas ceļojums.
* `Laiks` - laiks, kad ceļotājs ierodas sākuma lidostā, formāts ir `HH: MM` (tas pats, kas ievades 3. rindiņa).
* `No` - izlidošanas lidosta pašreizējam lidojumam.
* `Uz` - pašreizējā lidojuma galamērķa lidosta.
* `Lidojums` – izlidošanas un ielidošanas laiks lidojumam formātā `HH: MM-HH: MM`.

Ja ceļojumu nav iespējams veikt, izveidojiet šādu izvades failu:

```c
Neiespējami```

#### 1. piemērs (ir iespējams sasniegt galamērķi):

Ievades datnes saturs `lidostas.in`:

```c
5 1 5 00:00 1 2 1 01:00-03:00 1 2 2 12:00-14:05 15:00-17:00 1 3 2 06:30-08:00 17:20-18:55 2 3 2 13:00-16:00 21:00-00:00 2 4 3 04:00-08:00 05:00-09:00 18:00-22:00 3 1 2 02:45-04:15 23:50-01:20 3 2 1 23:52-02:52 3 5 1 23:51-04:00 4 2 1 18:00-22:00 4 3 1 12:00-13:00 0```

Izvades faila saturs `lidostas.out`:

```c
1 00:00 1 - > 2 01:00-03:00 2 - > 4 04:00-08:00 4 - > 3 12:00-13:00 3 - > 1 23:50-01:20 1 - > 3 06:30-08:00 3 - > 5 23:51-04:00```

#### 2. piemērs (pēc pāriešanas no 1 uz 2 un atpakaļ tiek iestrēgusi 1. lidostā):

Ievades faila saturs `lidostas.in`:

```c
3 1 3 00:00 1 2 1 01:00-02:00 2 1 1 03:00-04:00 2 3 1 12:00-13:00 3 2 1 18:00-19:00 0```

Izvades faila saturs `lidostas.out`:

```c
Neiespējami```

