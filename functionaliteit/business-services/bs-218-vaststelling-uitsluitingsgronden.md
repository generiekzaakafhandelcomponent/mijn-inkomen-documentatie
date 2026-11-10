---
description: Procesverloop, invoer en uitvoer van BS 218 vaststelling uitsluitingsgronden.
---

# BS 218 vaststelling uitsluitingsgronden

Bouwblok `bs-218-vaststelling-uitsluitingsgronden`.

## Invoer en uitvoer

**Invoer**

* `BSN`
* `brongegevens`
* `vastgesteldegegevens`
* `aanvraaggegevens`
* `handmatigVaststellen`

**Uitvoer**

* `uitsluitingsgrond (String)`
* `onderbouwing (String)`
* `signalering (Boolean)`
* `toelichting (String)`
* `vanToepassing (Boolean)`
* `brontype = 2 (Professional)`
* `vastleggingsdatum = sysdate`
* `geimplementeerd`
* `handmatig of automatisch vastgesteld`

## Het proces

| Soort | Stap |
| --- | --- |
| Beslistabel | uitsluitingsgronden |
| Keuze | Gegevens kwalitatief voldoende aanwezig? |
| Beslistabel | bepalen gegevens kwalitatief voldoende aanwezig |
| Systeemstap | Zoek naar signalering |
| Keuze | Is er een signalering of handmatig vaststellen gewenst? |
| Gebruikerstaak | ${taakTitel} |

## Onderdelen

**Formulieren**

* `bs-218-vaststellen-uitsluitingsgronden`

**Beslistabellen**

* `bs-218-vaststelling-uitsluitingsgronden`

Dit bouwblok heeft een eigen documentdefinitie.

---

Terug naar [Business services](../business-services.md).
