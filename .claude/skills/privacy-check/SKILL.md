---
name: privacy-check
description: Controleer documentatie op concrete gemeenten, personen, e-mailadressen en andere herleidbare gegevens (BSN, postcode, IBAN, telefoonnummer, secrets). Gebruik dit vóór elke commit of push naar de documentatierepo, bij het verwerken van aangeleverde teksten zoals releasenotes, en wanneer gevraagd wordt om een privacy- of AVG-controle.
---

# Privacycontrole documentatie

Deze documentatie wordt via GitBook gepubliceerd. **Er mogen nooit concrete gemeenten, personen of e-mailadressen in staan.** De teksten beschrijven het systeem generiek: "een gemeente", "de inwoner", "de behandelaar".

## Wanneer uitvoeren

Altijd vóór een commit of push. En in het bijzonder wanneer:

- aangeleverde tekst wordt verwerkt (releasenotes, testverslagen, functionele ontwerpen) — daar zitten de meeste lekken;
- voorbeelddata, JSON-fragmenten of schermafbeeldingen worden toegevoegd;
- een pilot, implementatie of specifieke omgeving wordt beschreven.

## Uitvoeren

```bash
python3 .claude/skills/privacy-check/scripts/check_privacy.py
```

Standaard scant het script alle `.md`- en `.yaml`-bestanden vanaf de repo-root. Paden meegeven kan ook:

```bash
python3 .claude/skills/privacy-check/scripts/check_privacy.py releasenotes/ overzicht/begrippen.md
```

Exitcode `1` betekent bevindingen in de categorie BLOKKEREND. Met `--review` worden ook de twijfelgevallen getoond.

## De categorieën

| Categorie | Ernst | Actie |
| --- | --- | --- |
| E-mailadres | Blokkerend | Verwijderen of vervangen door een rolaanduiding. |
| Gemeentenaam | Blokkerend | Vervangen door "de gemeente". |
| Persoonsnaam | Blokkerend | Vervangen door de rol ("de behandelaar", "de aanvrager"). |
| BSN / burgerservicenummer | Blokkerend | Verwijderen. Nooit een echt of echt-ogend BSN opnemen. |
| IBAN, telefoonnummer, postcode | Blokkerend | Verwijderen of onherkenbaar maken. |
| Ingevulde secret of omgevings-URL | Blokkerend | Vervangen door de placeholder (`${VARIABELE_NAAM}`). |
| Twijfelgeval | Review | Zelf beoordelen; zie hieronder. |

## Bevindingen beoordelen

Het script is streng en levert ruis op. Beoordeel elke melding; onterechte meldingen zet je in de allowlist.

**Bijna altijd onterecht:**

- Lidwoord plus systeemnaam: "de Objects API", "de Documenten API", "de Zaken API".
- Uitvoeringsorganisaties als gegevensbron: UWV, SVB, DUO, RDW, Kadaster, BRP. Dat zijn bronsystemen, geen gemeenten of personen.
- Producten en platformen: Valtimo, GZAC, Open Zaak, Keycloak, Socrates, Suwinet, SmartDocuments, NL Portal, MailHog.
- Plugin-configuratie-UUID's. Dat zijn vaste identifiers uit de broncode, geen persoonsgegevens.

**Vrijwel altijd terecht:**

- Een gemeentenaam in een zin over een pilot, implementatie of referentie-omgeving.
- Een naam met tussenvoegsel die geen systeemnaam is ("van Dijk", "de Vries").
- Een e-mailadres, in welke context dan ook — ook een afzender of contactadres.
- Een ingevulde RSIN, client-secret of omgevings-URL in plaats van een placeholder.

**Ambigu — altijd zelf kijken:** sommige gemeenten zijn ook gewone woorden (Buren, Bergen, Best, Beek, Laren, Epe, Ede, Urk, Goes, Horst, Veere, Weert, Stein, Vught). Het script meldt die als twijfelgeval, niet als blokkerend. Flag alleen als de zin echt over de gemeente gaat.

## Allowlist

Terugkerende onterechte meldingen zet je in `.claude/skills/privacy-check/allowlist.txt` — één term per regel, `#` voor commentaar. Voeg alleen toe wat je daadwerkelijk hebt beoordeeld.

## Bij een bevinding

1. **Herschrijf naar de generieke vorm.** Niet anonimiseren met initialen of "gemeente X" — schrijf de zin om zodat de concrete partij niet nodig is.
2. **Draai het script opnieuw** tot het schoon is.
3. **Meld het aan de gebruiker**, met wat er is aangepast en waarom.

Vindt het script niets, zeg dan expliciet wat er is gecontroleerd — niet alleen "schoon". De gebruiker moet kunnen zien hoe grondig de controle was.

## Beperkingen — benoem deze eerlijk

- De gemeentelijst is een handmatig onderhouden bestand en bevat ook opgeheven gemeenten. Volledigheid is niet gegarandeerd.
- Persoonsnamen worden heuristisch gevonden (tussenvoegsel plus hoofdletter). Een naam zonder tussenvoegsel, zoals "Jansen bepaalt de norm", wordt **niet** gevonden.
- Het script leest geen afbeeldingen. Schermafbeeldingen met echte dossiergegevens moet je zelf beoordelen.

Presenteer een schone uitslag dus nooit als absolute garantie.
