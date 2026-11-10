---
description: Procesverloop, invoer en uitvoer van BS 212 Vaststelling bijstandsvorm.
---

# BS 212 Vaststelling bijstandsvorm

Bouwblok `bs-212-vaststelling-bijstandsvorm`.

## Invoer en uitvoer

**Invoer**

* `IsBijstandsvormVastgesteld`
* `datumBijstandsvormVastgesteld`
* `vastgesteldeBijstandsvorm`
* `vastgesteldeTotaalVermogen`
* `vastgesteldeVermogenscomponenten`
* `vastgesteldeLeefsituatie`

**Uitvoer**

* `IsBijstandsvormVastgesteld`
* `datumBijstandsvormVastgesteld`
* `vastgesteldeBijstandsvorm`
* `automatischVastgesteld`

## Wie roept dit aan

| | |
| --- | --- |
| **Direct aangeroepen door** | `bsb-212-vaststelling-bijstandsvorm` |
| **Binnen zaakproces** | Algemene bijstand aanvraag, IOAW aanvraag |

De volledige keten, met de technische procesnamen:

* `bs-212-vaststelling-bijstandsvorm` ← `bsb-212-vaststelling-bijstandsvorm` ← `uitvoeren-business-services` ← `ab-afhandelen-aanvraag-dcm`
* `bs-212-vaststelling-bijstandsvorm` ← `bsb-212-vaststelling-bijstandsvorm` ← `uitvoeren-business-services` ← `ioaw-afhandelen-aanvraag-dcm`

## Het procesmodel

![Procesmodel: BS 212 Vaststelling bijstandsvorm](../../.gitbook/assets/bpmn/bs-212-vaststelling-bijstandsvorm.svg)

Gegenereerd uit het BPMN-model. Open de afbeelding apart om in te zoomen.

## Het proces

| Soort | Stap |
| --- | --- |
| Systeemstap | bereken beleenbaarVermogen (10 & 18) |
| Beslistabel | Bepalen bijstandsvorm |
| Systeemstap | bereken overwaarde (1, 15 & 17) |

## Onderdelen

**Beslistabellen**

* `bs-212-vaststelling-bijstandsvorm`

Dit bouwblok heeft een eigen documentdefinitie.

---

Terug naar [Business services](../business-services.md).
