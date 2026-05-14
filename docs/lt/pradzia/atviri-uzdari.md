# Atviri ir uždari duomenys

Pagrindinis katalogo tikslas — **atviri duomenys**, tačiau ne visi rinkiniai gali būti laisvai prieinami. Vienoje sistemoje (`data.gov.lt`) sugyvena du režimai: laisvai prieinami atviri rinkiniai ir prieigos apribojimais reguliuojami rinkiniai, kuriems prieiga gaunama per sutartį.

## Prieigos teisių lygiai

Kiekvienas duomenų rinkinys turi nustatytas prieigos teises. Lygiai:

| Lygis | Kas tai | Kam matomi metaduomenys | Kas gali naudoti duomenis |
| --- | --- | --- | --- |
| **Atviri** | Be apribojimų; gali naudoti bet kas, įskaitant komercinį naudojimą | Visi | Visi |
| **Apsaugoti** | Prieigai reikalingi papildomi sutikimai ar registracija | Visi | Tik su patvirtinta prieiga |
| **Uždari** | Prieiga tik sutarties pagrindu, paprastai paslaugos teikimo ar tyrimo tikslams | Visi (metaduomenys), bet ne patys duomenys | Tik su aktyvia sutartimi |
| **Konfidencialūs** | Riboto matomumo; turinys ir net metaduomenys gali būti nematomi viešai | Riboti | Tik aiškiai įgaliotiems naudotojams |

Konkretus rinkinio prieigos lygis nurodomas rinkinio formoje (laukas „Prieigos teisės") ir matomas viešajame rinkinio puslapyje.

## Atviri duomenys

Atviri duomenys naudojami **be apribojimų** komercinio ir nekomercinio panaudojimo. Registracijos prieš parsisiunčiant nereikia, taip pat nereikia jokio leidimo. Pagrindinė pareiga — laikytis rinkinio licencijos sąlygų (paprastai tai yra CC BY arba ekvivalentas, kuris reikalauja nurodyti šaltinį).

Pagrindiniai naudojimo būdai:

- Parsisiųsti rinkinio failą (CSV, JSON, ar kitas paskelbtas formatas);
- Pasiekti per rinkinio API;
- Importuoti į savo sistemą per Spinta agentą (jei rinkinys per agentą teikiamas).

## Apriboti duomenys (apsaugoti / uždari / konfidencialūs)

Jei rinkinio prieigos lygis nėra „Atviri", jo duomenims gauti reikia **sutarties** tarp duomenų teikėjo organizacijos ir duomenų gavėjo organizacijos. Trumpas kelias:

1. **Panaudojimo atvejis.** Duomenų gavėjas užregistruoja {doc}`panaudojimo atvejį <../objektai/panaudojimo-atvejis>` portale ir prie jo prisega norimus rinkinius.
2. **Sutarties sukūrimas.** Iš panaudojimo atvejo generuojama {doc}`sutartis <../objektai/sutartis>` (po vieną kiekvienai duomenis teikiančiai organizacijai).
3. **Pasiūlymas ir patvirtinimas.** Duomenų gavėjas pateikia pasiūlymą su teisiniu pagrindu ir tikslu; duomenų teikėjas patvirtina pasiūlymą.
4. **Pasirašymas.** Sutarties PDF dokumentas pasirašomas elektroniniu būdu — pirmiausia duomenų gavėjo, paskui duomenų teikėjo.
5. **Aktyvi sutartis.** Po sėkmingos sinchronizacijos su agentu sutartis tampa „Aktyvi" — atsiranda techninė prieiga prie duomenų.

Detalų žingsnių vadovą rasi: {doc}`Prieigos gavimas <../vartotojo-gidas/prieigos-gavimas>`.

## Vienas portalas, ne du

Tiek atvirų, tiek apribotų duomenų metaduomenys gyvena tame pačiame kataloge `data.gov.lt`. Atskiro „uždaro portalo" nėra — prieigos lygis nustatomas rinkinio lygyje, o sutarčių mechanizmas integruotas į portalą. Naudotojui tai reiškia, kad reikalingo rinkinio paieška visada prasideda toje pačioje vietoje, o prieigos kelias šakojasi tik radus konkretų rinkinį.

## Susiję

- {doc}`Sutartis <../objektai/sutartis>` — sutarties objektas kataloge
- {doc}`Panaudojimo atvejis <../objektai/panaudojimo-atvejis>` — kontekstas, kuriame kuriamos sutartys
- {doc}`Prieigos gavimas <../vartotojo-gidas/prieigos-gavimas>` — pilnas žingsnių vadovas
- {doc}`Pagrindinės sąvokos <savokos>` — terminų sąrašas
