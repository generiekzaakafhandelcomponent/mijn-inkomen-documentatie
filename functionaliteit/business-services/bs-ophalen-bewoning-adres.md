---
description: Procesverloop, invoer en uitvoer van BS ophalen bewoning adres.
---

# BS ophalen bewoning adres

Bouwblok `bs-ophalen-bewoning-adres`.

## Invoer en uitvoer

**Invoer**

* `verblijfadres`
* `peildatum`
* `objectManagementTitle`

**Uitvoer**

* `bewoningAdres`
* `adresMetVeelBewoners`
* `typeVeelBewonersInstelling`

## Wie roept dit aan

| | |
| --- | --- |
| **Direct aangeroepen door** | `bsb-ophalen-bewoning-adres-aanvrager` |
| **Binnen zaakproces** | `ab-afhandelen-aanvraag-dcm`, `ioaw-afhandelen-aanvraag-dcm` |

De volledige keten:

* `bs-ophalen-bewoning-adres` ← `bsb-ophalen-bewoning-adres-aanvrager` ← `uitvoeren-business-services` ← `ab-afhandelen-aanvraag-dcm`
* `bs-ophalen-bewoning-adres` ← `bsb-ophalen-bewoning-adres-aanvrager` ← `uitvoeren-business-services` ← `ioaw-afhandelen-aanvraag-dcm`

## Het procesmodel

![Procesmodel: BS ophalen bewoning adres](../../.gitbook/assets/bpmn/bs-ophalen-bewoning-adres.svg)

Gegenereerd uit het BPMN-model. Open de afbeelding apart om in te zoomen.

## Het proces

| Soort | Stap |
| --- | --- |
| Aanroep | Controleren adres op veel bewoners → `controleren-adres-veel-bewoners` |
| Aanroep | Ophalen bewoning adres → `ophalen-brp-bewoningen-gegevens` |

## Onderdelen

Dit bouwblok heeft een eigen documentdefinitie.

---

Terug naar [Business services](../business-services.md).
