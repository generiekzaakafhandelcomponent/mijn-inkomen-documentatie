---
description: Procesverloop, invoer en uitvoer van BS opvoeren dienst in Socrates.
---

# BS opvoeren dienst in Socrates

Bouwblok `bs-opvoeren-dienst-in-socrates`.

## Invoer en uitvoer

Dit bouwblok benoemt geen invoer- en uitvoervariabelen in het procesmodel.

## Wie roept dit aan

| | |
| --- | --- |
| **Direct aangeroepen door** | `bsb-opvoeren-dienst-in-socrates` |
| **Binnen zaakproces** | `ab-afhandelen-aanvraag-dcm`, `ioaw-afhandelen-aanvraag-dcm` |

De volledige keten:

* `bs-opvoeren-dienst-in-socrates` ← `bsb-opvoeren-dienst-in-socrates` ← `uitvoeren-business-services` ← `ab-afhandelen-aanvraag-dcm`
* `bs-opvoeren-dienst-in-socrates` ← `bsb-opvoeren-dienst-in-socrates` ← `uitvoeren-business-services` ← `ioaw-afhandelen-aanvraag-dcm`

## Het procesmodel

![Procesmodel: BS opvoeren dienst in Socrates](../../.gitbook/assets/bpmn/bs-opvoeren-dienst-in-socrates.svg)

Gegenereerd uit het BPMN-model. Open de afbeelding apart om in te zoomen.

## Het proces

| Soort | Stap |
| --- | --- |
| Keuze | dienst al aangemaakt in socrates |
| Gebruikerstaak | controleren dienst in socrates |
| Systeemstap | Controleren op aangemaakt dienst |
| Systeemstap | Opvoeren dienst in socrates |
| dataStoreReference | socrates |

## Onderdelen

**Formulieren**

* `aanvraag-levensonderhoud.controleren-dienst-in-socrates`

Dit bouwblok heeft een eigen documentdefinitie.

---

Terug naar [Business services](../business-services.md).
