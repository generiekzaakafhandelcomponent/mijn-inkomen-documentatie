---
description: Procesverloop, invoer en uitvoer van BS Behandeling aanvraag opnieuw starten.
---

# BS Behandeling aanvraag opnieuw starten

Bouwblok `bs-behandeling-aanvraag-opnieuw-starten`.

## Invoer en uitvoer

Dit bouwblok benoemt geen invoer- en uitvoervariabelen in het procesmodel.

## Het procesmodel

![Procesmodel: BS Behandeling aanvraag opnieuw starten](../../.gitbook/assets/bpmn/bs-behandeling-aanvraag-opnieuw-starten.svg)

Gegenereerd uit het BPMN-model. Open de afbeelding apart om in te zoomen.

## Het proces

| Soort | Stap |
| --- | --- |
| Aanroep | Ophalen besluit → `generic-ophalen-besluit` |
| Keuze | Besluit zonder vervaldatum? |
| Systeemstap | vastleggen vervaldatum en vervalreden besluit |
| dataStoreReference | Open zaak |
| Keuze | Minimaal 1 besluit aanwezig? |
| Aanroep | Update zaakstatus en interne status → `generic-update-zaakstatus-en-interne-status-plugin-v2` |

## Onderdelen

Dit bouwblok heeft een eigen documentdefinitie.

---

Terug naar [Business services](../business-services.md).
