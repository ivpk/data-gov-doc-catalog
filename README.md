# data-gov-doc-catalog

Lietuvos atvirų duomenų portalo (https://data.gov.lt) **katalogo dokumentacija**. Dvikalbis (LT/EN) Sphinx projektas, publikuojamas per ReadTheDocs į `docs.data.gov.lt`.

## Struktūra

```
docs/
├── Makefile
├── requirements.in
├── requirements.txt
├── lt/                       # lietuviška versija (pirminė)
│   ├── conf.py
│   ├── index.md
│   ├── pradzia/              # įvadas, atviri/uždari, sąvokos, greitas startas
│   ├── objektai/             # ką katalogas registruoja (organizacija, rinkinys, …)
│   ├── vartotojo-gidas/      # how-to: publikavimas, paėmimas, prieigos gavimas
│   ├── roles/                # rolės ir teisės
│   ├── reference/            # techninė referencija (DSA, DCAT, partnerių API)
│   └── duk.md
└── en/                       # anglų versija (vertimas po LT stabilizavimo)
```

## Lokali peržiūra

```bash
cd docs
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt

# Live preview (LT):
./.venv/bin/sphinx-autobuild -b html lt lt/_build/html
# → http://127.0.0.1:8000
```

## JIRA

- Projektas: **DAS** („Duomenų architektūros skyrius"), https://itpagalba-vssa.atlassian.net/
- Epic: **[DAS-53](https://itpagalba-vssa.atlassian.net/browse/DAS-53)** — „Dokumentacija ir specifikacijos"
- Dokumentacijos darbo susitarimai — `~/dsa-docs/PLAYBOOK.md`

## Branch'ai

- `main` — stabili versija (publikuojama RTD `latest`)
- `docs-draft` — darbinis branch'as visiems dokumentacijos pakeitimams; merge'inamas į `main` kai turinys validuotas
