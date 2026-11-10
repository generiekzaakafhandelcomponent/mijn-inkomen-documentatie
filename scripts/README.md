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
* **formulieren, formulierstromen en beslistabellen** uit de mappen ernaast.

Draai dit opnieuw na een wijziging in de bouwblokken. De pagina's zijn
volledig gegenereerd — handmatige aanpassingen gaan bij de volgende run
verloren.
