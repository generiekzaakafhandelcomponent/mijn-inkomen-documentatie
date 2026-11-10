---
description: Procesverloop, invoer en uitvoer van BS 223 vastsstellen leef en woonsituatie.
---

# BS 223 vastsstellen leef en woonsituatie

Bouwblok `bs-223-vastsstellen-leef-en-woonsituatie`.

## Invoer en uitvoer

**Invoer**

* `leefEnWoonsituatieVastgesteld`
* `datumVaststellingLeefEnWoonsituatie`
* `woonsituatie (vastgesteld)`
* `toelichtingWoonsituatie`
* `leefsituatie (vastgesteld)`
* `toelichtingLeefsituatie`
* `handmatigVaststellen`
* `aanvrager`
* `verblijfadresAanvrager`
* `verblijfadresAanvragerIsInstelling`
* `partnerAanwezig`
* `partner`
* `verblijfadresPartner`
* `verblijfadresPartnerIsInstelling`
* `woonsituatieVolgensAanvraag`

**Uitvoer**

* `leefEnWoonsituatieVastgesteld`
* `datumVaststellingLeefEnWoonsituatie`
* `woonsituatie`
* `toelichtingWoonsituatie`
* `leefsituatie`
* `toelichtingLeefsituatie`

## Het proces

| Soort | Stap |
| --- | --- |
| Beslistabel | Bepalen gegevens kwalitatief voldoende aanwezig |
| Keuze | gegevens kwalitatief voldoende aanwezig? |
| Beslistabel | Vaststellen woonsituatie |
| Keuze | handmatig woonsituatie vaststellen? |
| Beslistabel | Vaststellen leefsituatie |
| Keuze | handmatig leefsituatie vaststellen? |
| Gebruikerstaak | Vaststellen woonsituatie |
| Gebruikerstaak | Vaststellen leefsituatie |

## Onderdelen

**Formulieren**

* `bs-223-vaststellen-leefsituatie.vaststellen-leefsituatie`
* `bs-223-vaststellen-woonsituatie.vaststellen-woonsituatie`

**Beslistabellen**

* `bs-223-vastsstellen-leef-en-woonsituatie`

Dit bouwblok heeft een eigen documentdefinitie.

---

Terug naar [Business services](../business-services.md).
