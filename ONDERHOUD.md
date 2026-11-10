# Onderhoud van deze documentatie

Hoe deze site in elkaar zit, waar de inhoud vandaan komt, en hoe je hem
opnieuw opbouwt. Dit document is voor wie de documentatie onderhoudt; het
wordt bewust niet via GitBook gepubliceerd.

## Wat dit is

Een GitBook-site die rechtstreeks uit deze repository wordt gesynchroniseerd.
Twee bestanden bepalen de structuur:

| Bestand | Rol |
| --- | --- |
| `.gitbook.yaml` | Wijst GitBook naar de root, de inleiding en de inhoudsopgave. |
| `SUMMARY.md` | De inhoudsopgave én de lijst van te publiceren pagina's. |

> **GitBook publiceert alleen wat in `SUMMARY.md` staat.** Een markdown-bestand
> dat daar ontbreekt wordt niet als pagina herkend; links ernaartoe vallen
> terug op het ruwe bestand op GitHub. Dat is één keer misgegaan met de
> business-servicepagina's. Wil je pagina's wel publiceren maar niet
> prominent in de navigatie, zet ze dan **genest** onder hun ouderpagina —
> twee spaties inspringen.

## Handgeschreven of gegenereerd

Niet alles wordt met de hand onderhouden. Pas gegenereerde pagina's nooit
direct aan: bij de volgende generatie is je wijziging weg.

| Onderdeel | Herkomst |
| --- | --- |
| `overzicht/`, `functionaliteit/*.md`, `gegevens/`, `koppelingen/`, `beheer/`, `handleiding/`, `releasenotes/` | **Handgeschreven.** |
| `functionaliteit/business-services/*.md` | **Gegenereerd** uit de bouwblokken van de backend. |
| `.gitbook/assets/bpmn/*.svg` | **Gegenereerd** uit de BPMN-modellen. |
| `.gitbook/assets/*.png` | **Gegenereerd**: schermafbeeldingen uit een draaiende omgeving. |
| De geneste regels onder *Business services* in `SUMMARY.md` | **Gegenereerd**; de rest van `SUMMARY.md` is handwerk. |

## Waar de inhoud vandaan komt

| Bron | Waarvoor |
| --- | --- |
| `mijn-inkomen-gzac-backend` (branch `develop`) | De configuratie: bouwblokken, BPMN, DMN, schema's, PBAC. De feitelijke basis onder vrijwel alle pagina's. |
| Een draaiende lokale omgeving | De schermafbeeldingen in de handleiding. |
| `mijn-inkomen-playwright` | De E2E-testsuite. Bevat per taak de precieze veld- en knopnamen — de snelste bron als je een scherm moet beschrijven of bereiken. |
| `persona-lab` | Testpersona's en de requests om een dossier aan te maken. |
| Aangeleverde releasenotes | De pagina over de huidige release. |

> Er bestaan **twee repositories met de naam `mijn-inkomen-gzac-backend`**.
> Alleen die in de gemeente-organisatie is actueel; de andere ligt sinds
> april 2026 stil. Controleer bij twijfel `git remote -v` en de datum van de
> laatste commit.

## Opnieuw opbouwen

De volgorde doet ertoe: de paginagenerator zoekt of er al een diagram klaarstaat.

```bash
npm install bpmn-js playwright
node scripts/render-bpmn.mjs                     # 1. BPMN → SVG
python3 scripts/generate-business-services.py    # 2. pagina's + navigatie
node scripts/capture-screenshots.mjs             # 3. schermafbeeldingen
```

Stap 3 vereist een draaiende omgeving; de eerste twee hebben alleen de
backend-checkout nodig. Elk script accepteert het pad naar die checkout als
argument en valt anders terug op `../mijn-inkomen-gzac-backend-v13`.

Details per script staan in [`scripts/README.md`](scripts/README.md).

## Controleren vóór een push

Twee controles, allebei met exitcode 1 bij bevindingen:

```bash
python3 scripts/check-docs.py                               # structuur
python3 .claude/skills/privacy-check/scripts/check_privacy.py   # privacy
```

De structuurcontrole kijkt naar interne links, ankers, afbeeldingen,
GitBook-blokken, codefences en SUMMARY-dekking.

De privacycontrole bewaakt de harde eis dat er **geen concrete gemeenten,
personen of e-mailadressen** in de documentatie staan. Zie
[`.claude/skills/privacy-check/SKILL.md`](.claude/skills/privacy-check/SKILL.md)
voor hoe je bevindingen beoordeelt.

> De privacycontrole **scant geen afbeeldingen**. Schermafbeeldingen met
> dossiergegevens moet je zelf beoordelen. De testpersoon die nu in de
> handleiding staat is als fictief beoordeeld en opgenomen in de allowlist.

## Conventies

**Taal.** Nederlands, en consequent de functionele term boven de technische.
Technische namen mogen erbij staan waar ze helpen bij terugzoeken; in de
begrippenlijst staat de vertaaltabel voor de zaakprocessen.

**GitBook-syntax.** Kaders met een `hint`-blok in vier stijlen — info, success,
warning en danger — en varianten naast elkaar met een `tabs`-blok met
`tab`-elementen erin. Beide moeten netjes afgesloten worden met het
bijbehorende `end`-element; `check-docs.py` bewaakt dat.

**Diagrammen.** Mermaid in een codefence met taal `mermaid`. GitBook rendert
die zelf; er is geen bouwstap voor nodig. BPMN-modellen zijn SVG, met een witte
achtergrond — anders is zwart lijnwerk onleesbaar in het donkere thema.

**Afbeeldingen.** In `.gitbook/assets/`, verkleind naar breedte 1600. Verwijs
er relatief naar.

## Valkuilen

| Symptoom | Oorzaak |
| --- | --- |
| Link opent een markdown-bestand op GitHub | De pagina staat niet in `SUMMARY.md`. |
| Wijziging in de configuratie komt niet door bij het opstarten | Het `changesetId` in het configuratiebestand is niet verhoogd. |
| Documentatie wijkt af van de applicatie | De backend-checkout is verouderd, of wijst naar de verkeerde repository. |
| Pagina mist na een generatie | De bouwblokmap en het proces-id in het model lopen niet gelijk; de generator zoekt op proces-id. |
