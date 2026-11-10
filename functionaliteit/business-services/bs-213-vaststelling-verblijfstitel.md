---
description: Procesverloop, invoer en uitvoer van BS 213 vaststelling verblijfstitel.
---

# BS 213 vaststelling verblijfstitel

Bouwblok `bs-213-vaststelling-verblijfstitel`.

## Invoer en uitvoer

**Invoer**

* `verblijfstitelVastgesteld`
* `datumVerblijfstitelVastgesteld`
* `handmatigVaststellen`
* `nationaliteitVerblijfstatusAanvraag`
* `actiesVerblijfstatus`
* `nationaliteitenBrp`
* `verblijfstitelBrp`

**Uitvoer**

* `verblijfstitelVastgesteld`
* `datumVerblijfstitelVastgesteld`
* `verblijfstitel`
* `rechtOpBijstand`
* `toelichtingConsulent`

## Het proces

| Soort | Stap |
| --- | --- |
| Beslistabel | Bepalen gegevens kwalitatief voldoende aanwezig |
| Keuze | Gegevens kwalitatief voldoende aanwezig? |
| Beslistabel | Bepalen handmatige beoordeling |
| Keuze | Handmatige beoordeling nodig? |
| Beslistabel | Bepalen verblijfstitel rechthebbend |
| Gebruikerstaak | ${taakTitel} |

## Onderdelen

**Formulieren**

* `bs-213-vaststelling-verblijfstitel.vaststellen-verblijfstitel`

**Beslistabellen**

* `bs-213-vaststelling-verblijfstitel`

Dit bouwblok heeft een eigen documentdefinitie.

---

Terug naar [Business services](../business-services.md).
