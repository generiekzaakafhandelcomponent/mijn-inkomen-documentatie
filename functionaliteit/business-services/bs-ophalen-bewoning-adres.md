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

## Het proces

| Soort | Stap |
| --- | --- |
| Aanroep | Controleren adres op veel bewoners → `controleren-adres-veel-bewoners` |
| Aanroep | Ophalen bewoning adres → `ophalen-brp-bewoningen-gegevens` |

## Onderdelen

Dit bouwblok heeft een eigen documentdefinitie.

---

Terug naar [Business services](../business-services.md).
