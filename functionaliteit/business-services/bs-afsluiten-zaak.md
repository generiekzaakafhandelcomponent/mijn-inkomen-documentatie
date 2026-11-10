---
description: Procesverloop, invoer en uitvoer van BS Afsluiten zaak.
---

# BS Afsluiten zaak

Bouwblok `bs-afsluiten-zaak`.

## Invoer en uitvoer

Dit bouwblok benoemt geen invoer- en uitvoervariabelen in het procesmodel.

## Het proces

| Soort | Stap |
| --- | --- |
| Systeemstap | Get resultaat type url |
| Systeemstap | Update zaakresultaat |
| dataStoreReference | Zaken API |
| dataStoreReference | Catalogi API |
| Systeemstap | Ophalen zaakstatus type url |
| Systeemstap | Zet zaakstatus |
| dataStoreReference | Catalogi API |
| dataStoreReference | Zaken API |
| Beslistabel | Bepalen resultaatType |
| Systeemstap | Zet interne status |

## Onderdelen

**Beslistabellen**

* `alo-bepalen-resultaattype`

Dit bouwblok heeft een eigen documentdefinitie.

---

Terug naar [Business services](../business-services.md).
