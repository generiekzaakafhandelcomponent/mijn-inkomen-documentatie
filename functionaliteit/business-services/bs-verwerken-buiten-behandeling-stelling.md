---
description: Procesverloop, invoer en uitvoer van BS Verwerken buiten behandeling stelling.
---

# BS Verwerken buiten behandeling stelling

Bouwblok `bs-verwerken-buiten-behandeling-stelling`.

## Invoer en uitvoer

Dit bouwblok benoemt geen invoer- en uitvoervariabelen in het procesmodel.

## Wie roept dit aan

| | |
| --- | --- |
| **Direct aangeroepen door** | `bsb-verwerken-buiten-behandeling-stelling` |
| **Binnen zaakproces** | `ab-afhandelen-aanvraag-dcm`, `basisafhandelproces-afhandelen-aanvraag`, `ioaw-afhandelen-aanvraag-dcm` |

De volledige keten:

* `bs-verwerken-buiten-behandeling-stelling` ← `bsb-verwerken-buiten-behandeling-stelling` ← `basisafhandelproces-uitvoeren-business-services` ← `basisafhandelproces-behandelen-zaak` ← `basisafhandelproces-afhandelen-aanvraag`
* `bs-verwerken-buiten-behandeling-stelling` ← `bsb-verwerken-buiten-behandeling-stelling` ← `uitvoeren-business-services` ← `ab-afhandelen-aanvraag-dcm`
* `bs-verwerken-buiten-behandeling-stelling` ← `bsb-verwerken-buiten-behandeling-stelling` ← `uitvoeren-business-services` ← `ioaw-afhandelen-aanvraag-dcm`

## Het procesmodel

![Procesmodel: BS Verwerken buiten behandeling stelling](../../.gitbook/assets/bpmn/bs-verwerken-buiten-behandeling-stelling.svg)

Gegenereerd uit het BPMN-model. Open de afbeelding apart om in te zoomen.

## Het proces

| Soort | Stap |
| --- | --- |
| Gebruikerstaak | Vastleggen buiten behandeling stelling |
| Systeemstap | Get besluit document url |
| Aanroep | Vastleggen besluit → `generic-vastleggen-besluit` |
| Keuze | Email aanwezig? |
| Systeemstap | Versturen emailnotificatie |
| Aanroep | Update zaakstatus en interne status → `generic-update-zaakstatus-en-interne-status-plugin-v2` |
| Systeemstap | GenereerEmailTask |

## Onderdelen

**Formulieren**

* `bs.verwerken-buiten-behandeling-stelling-besluit.vastleggen-buiten-behandeling-stelling`

Dit bouwblok heeft een eigen documentdefinitie.

---

Terug naar [Business services](../business-services.md).
