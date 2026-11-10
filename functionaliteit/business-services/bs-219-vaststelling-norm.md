---
description: Procesverloop, invoer en uitvoer van BS 219 vaststelling norm.
---

# BS 219 vaststelling norm

Bouwblok `bs-219-vaststelling-norm`.

## Invoer en uitvoer

**Invoer**

* `aantalBelanghebbende`
* `leeftijdJongsteBelanghebbende`
* `leeftijdOudsteBelanghebbende`
* `tenlasteKomendeKinderenAanwezig`
* `leeftijdPersoonAanvrager`
* `leeftijdPersoonPartner`
* `vastgesteldeLeefsituatie`
* `aantalKostendelers`
* `vastgesteldeWoonsitutatie`

**Uitvoer**

* `isNormVastgesteld`
* `datumNormVastgesteld`
* `isAutomatischVastgesteld`
* `vastgesteldeBasisnorm`
* `vastgesteldNormbedrag`
* `vastgesteldeKostendelersnorm`
* `vastgesteldeKostendelersfactor`
* `vastgesteldKostendelersNormbedragIndividueel`
* `vastgesteldKostendelersNormbedragGezamenlijk`

## Het proces

| Soort | Stap |
| --- | --- |
| Keuze | zijn er kostendelers? |
| Beslistabel | bepalen basis-normbedrag |
| Aanroep | Bepalen kostendelers-normbedrag (individueel) → `bs-219-bepalen-individueel-kostendelersnormbedrag` |
| Beslistabel | Bepaal Basisnorm |
| Aanroep | Bepalen kostendelers-normbedrag (individueel) → `bs-219-bepalen-individueel-kostendelersnormbedrag` |
| Aanroep | Bepalen kostendelers-normbedrag (individueel) → `bs-219-bepalen-individueel-kostendelersnormbedrag` |
| Keuze | Aantal belanghebbende |
| Systeemstap | Bepalen kostendelers-normbedrag (gezamelijk) |
| Gebruikerstaak | Vaststellen aantal rechthebbenden |

## Onderdelen

**Formulieren**

* `bs-219-vaststellen-norm.vaststellen-aantal-rechthebbenden`

**Beslistabellen**

* `bs-219-bepalen-basisnormbedrag`
* `bs-219-vaststelling-norm`

Dit bouwblok heeft een eigen documentdefinitie.

---

Terug naar [Business services](../business-services.md).
