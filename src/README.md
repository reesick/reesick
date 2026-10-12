# src

everything the profile readme is drawn with. edit here, never in `assets/`.

| file | what it does |
|---|---|
| `build.py` | hero, section bands, highlight cards, link pills and footer. blue for light mode, green for dark, plus a phone cut of each |
| `make_readme.py` | writes `../README.md`. project rows, copy and links live here |
| `fonts/` | Instrument Serif and Inter, the site's own files. subset and inlined into each svg, so nothing loads from outside |

```
pip install fonttools brotli
python src/build.py
python src/make_readme.py
```
