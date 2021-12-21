### Programmēšanas laboratorija: ārvalstnieki

**RAM atmiņa**: 4 MIB   **laiks**: 0,1 sekunde **ievade**: `aliens.in`   **izvade**: `aliens.out`

---

#### Apraksts

2020. gadā cilvēki nosūtīja Marsam autonomu robotu *neatlaidību*. (“*Mars 2020 misija piegādā neatlaidības Rover Sarkanajai planētai kā daļu no NASA Marsa izpētes programmas. Programmas pastāvīgās misijas palīdz mums atbildēt uz galvenajiem jautājumiem par dzīves potenciālu Marsā. Lai gan iepriekšējās misijas ir palīdzējušas mums meklēt apdzīvojamu apstākļu pazīmes senos laikos, neatlaidība būs solis uz priekšu, meklējot pagātnes mikrobu dzīvības pazīmes.*”)

Drīz vien *neatlaidība* pamanīja dažādas dzīvības pazīmes uz Marsa. Viņu attēlos bija zaļi radījumi, kas varēja mainīt savu atrašanās vietu. Mēģinot kādu laiku paslēpties, zaļie radījumi (vēlāk saukti par *citplanētiešiem*) nolēma sazināties ar mūsu civilizāciju. Cilvēki uz Zemes (saukti par *Earthlings*) atklāja, ka nav bīstami, un nolēma uzturēt labas attiecības ar citplanētiešiem un piekļūt viņu tehnoloģijām.

Lai novērstu kultūras atšķirības un izvairītos no pārpratumiem, Earthlings sāka interesēties par citplanētiešu ikdienas dzīvi. Kā viņi atklāja, citplanētiešiem ir bezseksuāla reprodukcija: katram citplanētiešam var būt ne vairāk kā divi bērni. Katrs bērns ir vai nu kreisā, vai labā roka. Turklāt, ja ārvalstniekam ir divi bērni, viens no tiem noteikti ir kreisā roka, bet otrs – labā roka. Reprodukcija var notikt drīz pēc dzimšanas, daudzas paaudzes var dzīvot vienlaicīgi. Tā kā ārvalstniekiem ir ļoti lielas ģimenes, viņu vislabvēlīgākās attiecības ir ar ne vairāk kā 2 radiniekiem.

Earthlings pētīja jautājumu: kā identificēt divus (vai mazāk) mīļākos radiniekus katram svešiniekam. Pirmkārt, mēs izvēlamies kādu svešinieku bez dzīva vecāka. Tad uzzīmējiet ģimenes koku (vecāku un bērnu attiecību koks ar doto svešinieku kā sakni), tad katram svešiniekam šajā ģimenes kokā ir divi mīļākie radinieki tieši viņam priekšā un uzreiz seko viņam *nekārtībā* DFS šķērsām pār šo koku. Kreisās rokas citplanētieši tiek rādīti pa kreisi no viņu vecākiem, pa labi no viņiem.

Jūsu uzdevums ir izveidot efektīvu programmu, kas saņem viena ģimenes koka ģenealoģijas datus, un, saņemot vaicājumu, tai jāatrod divi iecienītākie relatīvie citplanētieši jebkuram konkrētam citplanētiešam.

Ir zināms, ka vienai paplašinātai ģimenei ir ne vairāk kā 10 000 $ārvalstnieku, kas pašlaik ir dzīvi. Katram ārvalstniekam ir unikāls numurs $[1. 10\, 000] $.

Efektīvs risinājums ievadei, kurā ir tikai 100 ārvalstnieku, iegūtu aptuveni 8 punktus. Ja tas apstrādā līdz 1000 ārvalstniekiem, tas iegūst aptuveni 9 punktus.

#### Ievade:

Pirmajā rindā ir norādīts tā ārvalstnieka numurs, kurš ir attiecīgā dzimtas koka *galvenais dzīvais priekštecis*. Visās pārējās ievades faila rindās ir viena no šīm četrām komandām, kas veido ģenealoģijas koku:

1. Norādiet vecāka kreisās rokas bērnu.
2. Norādiet vecāka labās rokas bērnu.
3. Vaicājums par konkrēta svešinieka iecienītākajiem radiniekiem.
4. Pabeidziet savu darbu.

```
Priekštecis... L vecākelements... R vecāku bērns...? Svešinieks... F```

* `Priekštecis` ir ārvalstnieka numurs, kas ir visas dzimtas koka *galvenais dzīvais priekštecis*.
* `L` ir komanda, kas norāda vecākobjekta kreisās rokas bērnu.
* `R` ir komanda, kas norāda vecāka labās rokas bērnu.
* `Vecāks` ir ārvalstnieka numurs, kas iegūs jaunu bērnu (ārvalstnieka identifikators atrodas šajās robežās: $[1. 10\, 000]) $
* `Bērnelements` ir vecākelementa `bērnelements` (identifikators atrodas intervālā $[1.. 10\, 000]) $
* `Ārvalstnieks` ir ārvalstnieka identifikators pieprasījumā atrast iecienītākos radiniekus (identifikators atrodas intervālā $[1 līdz 10\ 000]) $

Ja komandas `L` vai `R` izdodas, ģenealoģijas kokam tiek pievienoti jauni mezgli.

Ievades dati ir derīgi attiecībā uz iepriekš definēto formātu un ierobežojumiem.

#### Izvade:

Atkarībā no ievades faila izvades failā ir izvade katrai vaicājuma komandai un arī katrai komandai, kas beidzas ar kļūmi:

```
Prev Next... error0... error1... error2... error3... error4... error5```

* `Prevs` ir tieši priekšā esošais svešinieks (*nesakārtotā* šķērsvirziena kārtībā) dotajam `svešiniekam`, kad mēs izpildām pavēli`? Svešinieks`. Ja iepriekš nav bijis ārzemnieka, izvadiet `0`.
* `Nākamais` ir nekavējoties sekojošais svešinieks (*nesakārtotā* šķērsvirziena kārtībā) dotajam `svešiniekam`, kad mēs izpildām pavēli`? Svešinieks`. Ja nākamā svešinieka nav, izvadiet `0`.
* `error0` - ārvalstnieks ar identifikācijas numuru `ārvalstnieks` nepastāv ģimenes kokā, kad izpildām komandu`? Svešinieks`.
* `error1` - `vecāki` un`` bērni ir vieni un tie paši.
* `error2` - `vecāks` nepastāv saimes kokā.
* `error3` - `bērns` jau tiek izmantots ģimenes kokā.
* `Err4` - `vecākam` jau ir kreisās rokas bērns ģimenes kokā.
* `ERR5` - `vecākam` jau ir labās rokas vāks dzimtas kokā.

Ja komanda izraisa vairākas kļūdas vienlaikus, izdrukājiet to ar mazāko skaitli.

#### Piemērs:

Ievades failā `aliens.in`:

```
7 L 7 2 R 7 9 L 9 5? 2 R 5 6 L 2 4 L 5 1? 5? 8 L 1 4 F```

Izvades fails `aliens.out`:

```
0 7 1 6 error0 error3```

Ģimenes koks tieši pirms pavēles**? 2**

![ALT teksta](http://home.lu.lv/~garnican/apts/images/aliens_1.jpg " ārvalstnieki 1")

Ģimenes koks tieši pirms pavēles**? 5**

![ALT teksta](http://home.lu.lv/~garnican/apts/images/aliens_2.jpg " ārvalstnieki 2")
