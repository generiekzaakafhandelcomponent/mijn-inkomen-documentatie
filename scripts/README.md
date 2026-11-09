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
