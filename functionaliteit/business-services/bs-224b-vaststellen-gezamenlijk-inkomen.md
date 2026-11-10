---
description: Procesverloop, invoer en uitvoer van BS 224b vaststellen gezamenlijk inkomen.
---

# BS 224b vaststellen gezamenlijk inkomen

Bouwblok `bs-224b-vaststellen-gezamenlijk-inkomen`.

## Invoer en uitvoer

Dit bouwblok benoemt geen invoer- en uitvoervariabelen in het procesmodel.

## Wie roept dit aan

| | |
| --- | --- |
| **Direct aangeroepen door** | `bsb-224b-vaststelling-gezamelijk-inkomen` |
| **Binnen zaakproces** | Algemene bijstand aanvraag, IOAW aanvraag |

De volledige keten, met de technische procesnamen:

* `bs-224b-vaststellen-gezamenlijk-inkomen` ← `bsb-224b-vaststelling-gezamelijk-inkomen` ← `uitvoeren-business-services` ← `ab-afhandelen-aanvraag-dcm`
* `bs-224b-vaststellen-gezamenlijk-inkomen` ← `bsb-224b-vaststelling-gezamelijk-inkomen` ← `uitvoeren-business-services` ← `ioaw-afhandelen-aanvraag-dcm`

## Het procesmodel

![Procesmodel: BS 224b vaststellen gezamenlijk inkomen](../../.gitbook/assets/bpmn/bs-224b-vaststellen-gezamenlijk-inkomen.svg)

Gegenereerd uit het BPMN-model. Open de afbeelding apart om in te zoomen.

## Het proces

| Soort | Stap |
| --- | --- |
| Systeemstap | Berekenen gezamelijk inkomen |
| Einde | gezamenlijk inkomen vastgesteld |

## Onderdelen

Dit bouwblok heeft een eigen documentdefinitie.

---

Terug naar [Business services](../business-services.md).
