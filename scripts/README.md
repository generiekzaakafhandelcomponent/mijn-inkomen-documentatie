# Scripts

## capture-screenshots.mjs

Maakt de schermafbeeldingen voor de [handleiding](../handleiding/aan-de-slag.md) opnieuw.
Draai dit na elke UI-wijziging — een handleiding met verouderde plaatjes is
misleidender dan geen plaatjes.

### Vereisten

* De lokale omgeving draait: backend op `localhost:8080`, frontend op `localhost:4200`.
* Playwright en een Chrome-installatie.
* Testdossiers in de omgeving (zie `persona-lab`, of gebruik **Creëer Nieuw Dossier**).

### Draaien

```bash
npm install playwright
node scripts/capture-screenshots.mjs
```

De afbeeldingen komen in `shots/`. Verklein ze daarna naar breedte 1600 en
kopieer ze naar `.gitbook/assets/`:

```bash
for f in shots/*.png; do sips -Z 1600 "$f" --out ".gitbook/assets/$(basename $f)"; done
```

### Inloggegevens

Het script logt in met de standaard ontwikkelgebruiker van de lokale
Keycloak (`admin`/`admin`). Dat zijn de gedocumenteerde dev-accounts uit
`gzac-docker-compose`; ze bestaan alleen lokaal.

### Let op

De vastgelegde schermen tonen **dummygegevens**. Controleer bij het
vernieuwen of de omgeving nog steeds testdata bevat en geen productiedata —
afbeeldingen worden niet gedekt door de privacycontrole in
`.claude/skills/privacy-check`.

## generate-business-services.py

Draai eerst `render-bpmn.mjs` als je ook de procesmodellen wilt meenemen.

Genereert een naslagpagina per business service in
`functionaliteit/business-services/`, uit de bouwblokken van de backend.

```bash
python3 scripts/generate-business-services.py [pad-naar-backend]
```

Zonder argument wordt `../mijn-inkomen-gzac-backend-v13` geprobeerd.

Per bouwblok worden gelezen:

* **naam en omschrijving** uit `building-block-definition.json`;
* **invoer en uitvoer** uit de tekstannotaties in het BPMN-model — niet elk
  blok benoemt die, dan meldt de pagina dat;
* **de processtappen** uit het BPMN-model, met het soort stap erbij;
* **formulieren, formulierstromen en beslistabellen** uit de mappen ernaast;
* **wie het bouwblok aanroept**, door alle BPMN-modellen in de configuratie te
  scannen op `callActivity` en de keten omhoog te volgen tot aan het zaakproces.
  Daarbij wordt het proces-id uit het model gebruikt, niet de mapnaam — die
  twee lopen niet altijd gelijk.

Voor de zaakprocessen toont de pagina een leesbare naam in plaats van het
technische id. Die namen staan in `PROCES_NAMEN` boven in het script; vul
die tabel aan als er een zaakproces bij komt, anders valt de pagina terug
op het id.

Het script werkt ook `SUMMARY.md` bij: de pagina's komen genest onder
*Business services* te staan. Dat is nodig, want **GitBook publiceert
alleen wat in SUMMARY.md staat** — een pagina die er niet in staat wordt
als bestandsverwijzing behandeld en de link loopt dood op GitHub.

Draai dit opnieuw na een wijziging in de bouwblokken. De pagina's zijn
volledig gegenereerd — handmatige aanpassingen gaan bij de volgende run
verloren.

## render-bpmn.mjs

Rendert het BPMN-model van elke business service naar SVG in
`.gitbook/assets/bpmn/`.

```bash
npm install bpmn-js playwright
node scripts/render-bpmn.mjs [pad-naar-backend]
```

De modellen worden met **bpmn-js** in een headless browser getekend en als
SVG weggeschreven — schaalbaar, doorzoekbaar en klein. Er wordt een witte
achtergrond onder gezet, anders is het zwarte lijnwerk onleesbaar in het
donkere thema van GitBook.

Draai dit vóór `generate-business-services.py`: die zoekt per bouwblok of
er een SVG klaarstaat en bedt hem dan in. Ontbreekt het diagram, dan slaat
de pagina die sectie gewoon over.
