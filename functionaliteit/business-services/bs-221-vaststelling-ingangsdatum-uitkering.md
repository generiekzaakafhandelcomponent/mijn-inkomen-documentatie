---
description: Procesverloop, invoer en uitvoer van BS 221 Vaststelling Ingangdatum.
---

# BS 221 Vaststelling Ingangdatum

Bouwblok `bs-221-vaststelling-ingangsdatum-uitkering`.

## Invoer en uitvoer

**Invoer**

* `ingangsdatumUitkeringVastgesteld`
* `datumMeldingVastgesteld`
* `datumAanvraagVastgesteld`
* `vastgesteldeIngangsdatumUitkering`
* `vastgesteldeDatumOntstaanRecht`
* `datumVaststellingIngangsdatumUitkering`
* `toelichtingVaststellingIngangsdatumConsulent`
* `handmatigVaststellen`
* `datumMelding`
* `datumAanvraag`
* `verzochteIngangsdatum`
* `redenVerzochteIngangsdatum`
* `redenAanvraag`
* `datumLaatsteSalaris`
* `datumUitkeringGestopt`
* `datumAlimentatieVerlaagd`
* `datumOpleidingStudieAfgerondGestopt`
* `datumRelatieVerbroken`
* `datumEigenBedrijfGestopt`
* `datumWeekgeldCOAGestopt`
* `datumlaatsteDagDetentie`

**Uitvoer**

* `ingangsdatumUitkeringVastgesteld`
* `datumMeldingVastgesteld`
* `datumAanvraagVastgesteld`
* `vastgesteldeIngangsdatumUitkering`
* `vastgesteldeDatumOntstaanRecht`
* `datumVaststellingIngangsdatumUitkering`
* `toelichtingVaststellingIngangsdatumConsulent`

## Het proces

| Soort | Stap |
| --- | --- |
| Beslistabel | Bepalen voorgestelde ingangsdatum |
| Beslistabel | Bepalen handmatige beoordeling |
| Keuze | handmatige beoordeling? |
| Keuze | aanvraagdatum gewijzigd? |
| Gebruikerstaak | Vaststellen Ingangsdatum |
| Systeemstap | Aanpassen zaak properies |
| Beslistabel | Bepalen vastgestelde ingangsdatum |

## Onderdelen

**Formulieren**

* `bs-221-vaststelling-ingangsdatum`

**Beslistabellen**

* `bs-221-vaststelling-ingangsdatum-uitkering`

Dit bouwblok heeft een eigen documentdefinitie.

---

Terug naar [Business services](../business-services.md).
