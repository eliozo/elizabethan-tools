# Pārdomas 6.11.2021

* Uz mark-down faila Tikal filtrs strādā

```
tikal.bat -x -sl EN tl LV file1.md 
python tulkotajs.py ...? 
tikal.bat -m manual.md.xlf -sl EN -tl LV -ie utf-8
pandoc -s -o manual_en.docx file1.md
pandoc -s -o manual_lv.docx manual.out.md
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

