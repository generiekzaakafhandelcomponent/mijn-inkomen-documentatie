---
description: Procesverloop, invoer en uitvoer van BS genereren rapportage.
---

# BS genereren rapportage

Bouwblok `bs-genereren-rapportage`.

## Invoer en uitvoer

Dit bouwblok benoemt geen invoer- en uitvoervariabelen in het procesmodel.

## Het procesmodel

![Procesmodel: BS genereren rapportage](../../.gitbook/assets/bpmn/bs-genereren-rapportage.svg)

Gegenereerd uit het BPMN-model. Open de afbeelding apart om in te zoomen.

## Het proces

| Soort | Stap |
| --- | --- |
| Aanroep | Update zaakstatus en interne status → `generic-update-zaakstatus-en-interne-status-plugin-v2` |
| Aanroep | Genereer rapportage → `alo-genereer-rapportage` |

## Onderdelen

Dit bouwblok heeft een eigen documentdefinitie.

---

Terug naar [Business services](../business-services.md).
