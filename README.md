# Seminārs: Valodu tehnoloģijas un mākslīgais intelekts


## Cilvēka vadīta mācību materiālu automatizēta tulkošana

**Elizabete Ozoliņa, LU Datorikas fakultātes 2.kursa studente**

**Apraksts.**

Šajā projektā ir iekļauti rīki, kuri spēj tulkot Markdown marķējumā rakstītus dokumentus.   
Aplūkojamie piemēri ir datorikas mācību materiāli, piemēram, datu struktūru uzdevumu apraksti,
diskrētās matemātikas lekciju pieraksti.
Dokumenta oriģināls ir Markdown fails angļu valodā un tiek tulkots uz latviešu valodu.
Iegūstamie gala formāti: `.docx`, `.pdf`, `.html`

## Rīka apraksts

Rīks programmēts valodā Python un tiek integrēts ar Tikal (vairāk var uzzināt šeit: `https://okapiframework.org/wiki/index.php/Distributions`),
pandoc un Tildes mašīntulkotāju (vairāk var uzzināt šeit: `https://github.com/tilde-nlp/mt-api-python-demo`)

### Sākotnējā konfigurācija

Lai sāktu konfigurāciju, ir jābūt ieinstalētam Git. 
Projektu pārkopē ar komandu  
`git clone https://github.com/eliozo/elizabethan-tools`
Pirms lietošanas jāuzstāda fails `bin/properties.txt`.  

```txt
[your-config]
client_id = ...................
system_id = ...................
service_url = .................
```

### Rīka darbināšana

Pievienot `bin` direktoriju savam `PATH` mainīgajam.

Atveriet Anaconda konsoli.

Pēc tam palaist šīs komandas. `manual.md` vietā var ielikt jebkuru Markdown failu angļu valodā.
Komandas ir jāizpilda tajā direktorijā, kurā atrodas izvēlētais Markdown fails.


```
tikal.bat -x -sl EN -tl LV manual.md 
tulkot.bat manual.md.xlf  
tikal.bat -m manual.md.xlf -sl EN -tl LV -ie utf-8
rem salabot.bat manual.out.md // Plānots salabot '$ $' -> '$$' un '   ' -> '  \r\n'
pandoc -s -o manual_en.docx manual.md
pandoc -s -o manual_lv.docx manual.out.md
```
### Rīka iespējas 

Rīks pazīst un iztulko Markdown latviešu valodā un saglabā teksta formatējumu.

* Tekstā iekļautās (inline) matemātiskas formulas
* Pilna platuma (block) matemātiskas formulas
* Rindu pārnesumi ar diviem tukšumiem (procesā)


```txt
Tekstā iekļautās formulas piemērs: $y=f(x)$
Pilna platuma formulas piemērs: 

$$x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.$$
```
