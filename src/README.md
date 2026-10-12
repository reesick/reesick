# src

everything the profile readme is drawn with. edit here, never in `assets/`.

| file | what it does |
|---|---|
| `build.py` | the hero, section bands, link pills and footer. blue for light mode, green for dark, plus a phone cut of each |
| `statscard.py` | the numbers card. the workflow runs it daily with live data, offline it reads `seed.json` |
| `make_readme.py` | writes `../README.md`. project rows, copy and links live here |
| `fonts/` | Instrument Serif and Inter, the site's own files. subset and inlined into each svg |

```
pip install fonttools brotli
python src/build.py
python src/statscard.py
python src/make_readme.py
```
