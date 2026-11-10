---
description: Procesverloop, invoer en uitvoer van BS Overwegen voorschot.
---

# BS Overwegen voorschot

Bouwblok `bs-overwegen-voorschot`.

## Invoer en uitvoer

Dit bouwblok benoemt geen invoer- en uitvoervariabelen in het procesmodel.

## Wie roept dit aan

| | |
| --- | --- |
| **Direct aangeroepen door** | `bsb-overwegen-voorschot` |
| **Binnen zaakproces** | `ab-afhandelen-aanvraag-dcm`, `ioaw-afhandelen-aanvraag-dcm` |

De volledige keten:

* `bs-overwegen-voorschot` ← `bsb-overwegen-voorschot` ← `uitvoeren-business-services` ← `ab-afhandelen-aanvraag-dcm`
* `bs-overwegen-voorschot` ← `bsb-overwegen-voorschot` ← `uitvoeren-business-services` ← `ioaw-afhandelen-aanvraag-dcm`

## Het procesmodel

![Procesmodel: BS Overwegen voorschot](../../.gitbook/assets/bpmn/bs-overwegen-voorschot.svg)

Gegenereerd uit het BPMN-model. Open de afbeelding apart om in te zoomen.

## Het proces

| Soort | Stap |
| --- | --- |
| Gebruikerstaak | Overwegen voorschot |
| Systeemstap | Zet voorschot tag |
| Systeemstap | Verwijder voorschot tag |

## Onderdelen

**Formulieren**

* `bs.overwegen-voorschot.overwegen-voorschot`

Dit bouwblok heeft een eigen documentdefinitie.

---

Terug naar [Business services](../business-services.md).
