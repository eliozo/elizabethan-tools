# Pārdomas 6.11.2021

* Uz mark-down faila Tikal filtrs strādā

```
tikal.bat -x -sl EN -tl LV ../test-standalone/data-structures/Airports.md 
python tulkotajs.py ../test-standalone/data-structures/Airports.md.xlf  
tikal.bat -m ../test-standalone/data-structures/Airports.md.xlf -sl EN -tl LV -ie utf-8
pandoc -s -o ../test-standalone/data-structures/Airports_en.docx ../test-standalone/data-structures/Airports_en.md
pandoc -s -o ../test-standalone/data-structures/Airports_lv.docx ../test-standalone/data-structures/Airports_lv.md
```

* Matemātikas formulas un marķējumi varētu būt salūzuši (?)

* XLIFF parādās tagi ar franču valodu (iespējams noklusētā valoda?)

## Todo list

* Saprast, vai mēs varam mark-down filtru konfigurēt un papildināt
* Pielāgot XLIFF extraction arī REVEAL.JS slaidiem
* Pielāgot XLIFF extraction PowerPoint notes sadaļās dzīvojošajam mark-down
* Izmēģināt citas Tikal komandas, izņemot extraction 

# 22.11.2021

* Extract and merge

```
tikal.bat -x file1.md
tikal.bat -m file1.md.xlf
```

