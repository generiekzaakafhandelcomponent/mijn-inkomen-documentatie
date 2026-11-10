---
description: Procesverloop, invoer en uitvoer van BS 211 ophalen BRP persoonsgegevens tbv vaststellen persoon.
---

# BS 211 ophalen BRP persoonsgegevens tbv vaststellen persoon

Bouwblok `bs-211-ophalen-brp-tbv-vaststellen-persoon`.

## Invoer en uitvoer

Dit bouwblok benoemt geen invoer- en uitvoervariabelen in het procesmodel.

## Wie roept dit aan

| | |
| --- | --- |
| **Direct aangeroepen door** | `bs-211-vaststelling-persoon` |
| **Binnen zaakproces** | Algemene bijstand aanvraag, Basisafhandelproces, IOAW aanvraag |

De volledige keten, met de technische procesnamen:

* `bs-211-ophalen-brp-persoonsgegevens-tbv-vaststellen-persoon` ← `bs-211-vaststelling-persoon` ← `basisafhandelproces-bsb-211-vaststelling-persoon-aanvrager` ← `basisafhandelproces-uitvoeren-business-services` ← `basisafhandelproces-behandelen-zaak` ← `basisafhandelproces-afhandelen-aanvraag`
* `bs-211-ophalen-brp-persoonsgegevens-tbv-vaststellen-persoon` ← `bs-211-vaststelling-persoon` ← `basisafhandelproces-bsb-211-vaststelling-persoon-partner` ← `basisafhandelproces-uitvoeren-business-services` ← `basisafhandelproces-behandelen-zaak` ← `basisafhandelproces-afhandelen-aanvraag`
* `bs-211-ophalen-brp-persoonsgegevens-tbv-vaststellen-persoon` ← `bs-211-vaststelling-persoon` ← `bsb-211-vaststelling-persoon-aanvrager` ← `uitvoeren-business-services` ← `ab-afhandelen-aanvraag-dcm`
* `bs-211-ophalen-brp-persoonsgegevens-tbv-vaststellen-persoon` ← `bs-211-vaststelling-persoon` ← `bsb-211-vaststelling-persoon-aanvrager` ← `uitvoeren-business-services` ← `ioaw-afhandelen-aanvraag-dcm`
* `bs-211-ophalen-brp-persoonsgegevens-tbv-vaststellen-persoon` ← `bs-211-vaststelling-persoon` ← `bsb-211-vaststelling-persoon-partner` ← `uitvoeren-business-services` ← `ab-afhandelen-aanvraag-dcm`
* `bs-211-ophalen-brp-persoonsgegevens-tbv-vaststellen-persoon` ← `bs-211-vaststelling-persoon` ← `bsb-211-vaststelling-persoon-partner` ← `uitvoeren-business-services` ← `ioaw-afhandelen-aanvraag-dcm`

## Het procesmodel

![Procesmodel: BS 211 ophalen BRP persoonsgegevens tbv vaststellen persoon](../../.gitbook/assets/bpmn/bs-211-ophalen-brp-tbv-vaststellen-persoon.svg)

Gegenereerd uit het BPMN-model. Open de afbeelding apart om in te zoomen.

## Het proces

| Soort | Stap |
| --- | --- |
| Aanroep | Ophalen BRP persoons-gegevens → `generic-suwinet-ophalen-brp-brongegevens` |
| Gebruikerstaak | Bepalen vervolgactie |
| Einde | BRP persoons-gegevens niet opgehaald |
| Einde | BRP persoons-gegevens opgehaald |
| Onderbreking | Suwinet BSN niet gevonden |
| Einde | BRP gegevens handmatig ingevuld |

## Onderdelen

**Formulieren**

* `bs-211-vaststelling-persoon.bepalen-vervolgactie`

Dit bouwblok heeft een eigen documentdefinitie.

---

Terug naar [Business services](../business-services.md).
