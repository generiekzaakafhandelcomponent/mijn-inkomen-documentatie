---
description: De applicatie en de omringende stack op je eigen machine starten.
---

# Lokaal draaien

## Wat je nodig hebt

| | |
| --- | --- |
| Java | 21 |
| Docker | Met Docker Compose |
| Keycloak | Draaiend (zie hieronder) |
| Database | PostgreSQL |

## Configuratie klaarzetten

De applicatie leest zijn instellingen uit `.env.properties` in de projectroot. Dat bestand staat niet in versiebeheer — het bevat wachtwoorden en API-sleutels.

Maak het aan op basis van het voorbeeld:

```bash
cp .env.properties.example .env.properties
```

Vul daarna de waarden in voor je eigen omgeving: database, Keycloak, de URL's van Open Zaak en de Objects API, en de objecttype-UUID's.

{% hint style="warning" %}
De objecttype-UUID's moeten overeenkomen met wat er daadwerkelijk in jouw Objecttypes API staat. Zie [De objecttypen](lokaal-draaien.md#de-objecttypen).
{% endhint %}

## De ondersteunende stack starten

Mijn Inkomen heeft nogal wat omringende systemen nodig. Die draaien in Docker. Het `docker-compose.yml` in de projectroot bevat de volledige set:

| Categorie | Containers |
| --- | --- |
| **Zaakregistratie** | Open Zaak 1.20, Open Notificaties 1.13 |
| **Objecten** | Objects API 3.2, Objecttypes API 3.0 |
| **Identiteit** | Keycloak 24 |
| **Portaal** | NL Portal backend en frontend |
| **Bronnen (gesimuleerd)** | Suwinet-simulator, BRP Bewoning-mock, BAG-simulator, **Socrates-simulator** |
| **E-mail** | MailHog |
| **Infrastructuur** | PostgreSQL / PostGIS, Redis, RabbitMQ |

```bash
docker compose up -d
```

{% hint style="info" %}
De Suwinet-, BRP-, BAG- en Socrates-containers zijn **simulatoren**. Ze geven realistische maar verzonnen gegevens terug, zodat je kunt ontwikkelen zonder toegang tot de echte registraties.
{% endhint %}

{% hint style="warning" %}
**Gebruik de simulatorversies die de compose vastpint.** Die zijn afgestemd op de plugins in deze release. Bouw je er zelf een uit de laatste broncode, dan kun je een afwijkend berichtcontract krijgen — met als symptoom een `MALFORMED_JSON`-antwoord terwijl de simulator gewoon draait.
{% endhint %}

De Gradle-build kan de stack ook zelf beheren: het project gebruikt de `docker-compose`-plugin, zodat containers mee opstarten met de applicatie.

## De applicatie starten

```bash
./gradlew bootrun
```

Na het opstarten draait de backend op [http://localhost:8080](http://localhost:8080).

Controleren of hij leeft:

```bash
curl http://localhost:8080/api/ping
```

{% hint style="info" %}
De eerste start duurt langer dan de volgende. Alle configuratie wordt dan uitgerold: zestig bouwblokken met hun procesmodellen, beslistabellen, schema's en formulieren, plus de plugininstellingen.
{% endhint %}

## De objecttypen

Vijf objecttypen moeten in de Objecttypes API staan voordat de applicatie goed werkt:

| Objecttype | Waarvoor |
| --- | --- |
| Verzoek ALO | De aanvraag uit het portaal. |
| Externe Klanttaak | Taken in het portaal. |
| ALO: Informatieverzoek Items | Beheerde lijst met opvraagbare items. |
| Adressen met veel bewoners | Beheerde lijst voor handhavingssignalering. |
| Gemeentespecifieke Configuratie | Instellingen die per gemeente verschillen. |

De map `imports/` bevat fixtures voor de Objects API en de Objecttypes API, plus een Keycloak-realm en database-dumps voor Open Zaak en Open Notificaties. Daarmee start je met een gevulde omgeving.

Neem de UUID's en versienummers van de aangemaakte objecttypen over in `.env.properties`.

## Troubleshooting

{% tabs %}
{% tab title="Configuratie komt niet door" %}
Verhoog het `changesetId` in het gewijzigde bestand. Is dat ID al eerder uitgerold, dan slaat de applicatie de wijziging stilzwijgend over. Zie [Configuratie](configuratie.md#changeset-ids).
{% endtab %}

{% tab title="Brongegevens blijven leeg" %}
Controleer of de simulatorcontainers draaien en of de URL's in `.env.properties` kloppen. Fouten komen in het dossier terecht onder `connectionError`, met foutcode.

De behandeling loopt bewust door als een bron uitvalt — de velden blijven dan alleen leeg.
{% endtab %}

{% tab title="Geen verzoek binnengekomen" %}
Controleer de notificatieketen: staat het abonnement in Open Notificaties, draait RabbitMQ, en wijst de verzoekplugin naar de juiste notificatieconfiguratie?

Controleer ook of de objecttype-UUID in `.env.properties` overeenkomt met het objecttype waarmee het portaal het verzoek aanmaakt.
{% endtab %}

{% tab title="Proces loopt vast" %}
Kijk op het tabblad **Voortgang** waar de zaak staat; daar zie je het procesmodel met de actieve stap gemarkeerd.

Blijft een zaak hangen in `opvoeren-dienst`, dan is het opvoeren in Socrates waarschijnlijk mislukt: kijk naar `socratesError` in het dossier.
{% endtab %}
{% endtabs %}

## E-mail bekijken

Uitgaande mail gaat naar MailHog en wordt niet echt bezorgd. De webinterface van MailHog toont alle verzonden berichten, zodat je ontvangstbevestigingen, informatieverzoeken en besluitnotificaties kunt controleren.

## Valtimo bijwerken

Het script `upgrade.sh` en `prepareEnvVars.sh` ondersteunen het upgraden naar een nieuwe Valtimo-versie. `prepareEnvVars.sh` vraagt om het versienummer en zet de bijbehorende omgevingsvariabelen klaar.

De huidige versie staat in `gradle.properties` onder `valtimoVersion`.

## Meer achtergrond

Voor de ondersteunende containers bestaat een aparte repository met Compose-bestanden en uitleg: [gzac-docker-compose](https://github.com/generiekzaakafhandelcomponent/gzac-docker-compose).
