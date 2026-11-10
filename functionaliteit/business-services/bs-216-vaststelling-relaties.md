---
description: Procesverloop, invoer en uitvoer van BS 216 Vaststelling Relaties.
---

# BS 216 Vaststelling Relaties

Bouwblok `bs-216-vaststelling-relaties`.

## Invoer en uitvoer

Dit bouwblok benoemt geen invoer- en uitvoervariabelen in het procesmodel.

## Wie roept dit aan

| | |
| --- | --- |
| **Direct aangeroepen door** | `bsb-216-vaststelling-relaties` |
| **Binnen zaakproces** | `ab-afhandelen-aanvraag-dcm`, `ioaw-afhandelen-aanvraag-dcm` |

De volledige keten:

* `bs-216-vaststelling-relaties` ← `bsb-216-vaststelling-relaties` ← `uitvoeren-business-services` ← `ab-afhandelen-aanvraag-dcm`
* `bs-216-vaststelling-relaties` ← `bsb-216-vaststelling-relaties` ← `uitvoeren-business-services` ← `ioaw-afhandelen-aanvraag-dcm`

## Het procesmodel

![Procesmodel: BS 216 Vaststelling Relaties](../../.gitbook/assets/bpmn/bs-216-vaststelling-relaties.svg)

Gegenereerd uit het BPMN-model. Open de afbeelding apart om in te zoomen.

## Het proces

| Soort | Stap |
| --- | --- |
| Gebruikerstaak | Vaststellen Relaties |

## Onderdelen

**Formulieren**

* `bs-216-vaststelling-relaties`
* `bs-216-vaststelling-relaties-samenvatting`

**Formulierstromen**

* `bs-216-vaststelling-relaties`

Dit bouwblok heeft een eigen documentdefinitie.

---

Terug naar [Business services](../business-services.md).
