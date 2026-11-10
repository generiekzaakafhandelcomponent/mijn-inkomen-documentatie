---
description: Procesverloop, invoer en uitvoer van BS vastleggen resultaat inzet handhaving.
---

# BS vastleggen resultaat inzet handhaving

Bouwblok `bs-vastleggen-resultaat-inzet-handhaving`.

## Invoer en uitvoer

Dit bouwblok benoemt geen invoer- en uitvoervariabelen in het procesmodel.

## Wie roept dit aan

| | |
| --- | --- |
| **Direct aangeroepen door** | `bsb-vastleggen-resultaat-inzet-handhaving` |
| **Binnen zaakproces** | `ab-afhandelen-aanvraag-dcm`, `ioaw-afhandelen-aanvraag-dcm` |

De volledige keten:

* `bs-vastleggen-resultaat-inzet-handhaving` ← `bsb-vastleggen-resultaat-inzet-handhaving` ← `uitvoeren-business-services` ← `ab-afhandelen-aanvraag-dcm`
* `bs-vastleggen-resultaat-inzet-handhaving` ← `bsb-vastleggen-resultaat-inzet-handhaving` ← `uitvoeren-business-services` ← `ioaw-afhandelen-aanvraag-dcm`

## Het procesmodel

![Procesmodel: BS vastleggen resultaat inzet handhaving](../../.gitbook/assets/bpmn/bs-vastleggen-resultaat-inzet-handhaving.svg)

Gegenereerd uit het BPMN-model. Open de afbeelding apart om in te zoomen.

## Het proces

| Soort | Stap |
| --- | --- |
| Gebruikerstaak | Vastleggen uitkomst poortonderzoek |

## Onderdelen

**Formulieren**

* `bs.vastleggen-resultaat-inzet-handhaving.verwerken-uitkomst-poortonderzoek`

Dit bouwblok heeft een eigen documentdefinitie.

---

Terug naar [Business services](../business-services.md).
