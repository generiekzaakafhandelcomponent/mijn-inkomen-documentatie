---
description: Hoe de applicatie vanuit configuratiebestanden wordt opgebouwd.
---

# Configuratie

Mijn Inkomen bevat precies één bestand met code: `Application.kt`, de Spring Boot-startklasse. Alle functionaliteit zit in configuratie die bij het opstarten automatisch wordt uitgerold — *autodeployment*.

{% hint style="success" %}
Dit betekent dat functionele wijzigingen — een stap toevoegen aan een proces, een normbedrag indexeren, een veld op een tabblad zetten — zonder maatwerkcode kunnen. Het betekent óók dat de configuratie de broncode ís en dezelfde zorg verdient: code review, versiebeheer, testen.
{% endhint %}

## De configuratiemappen

Alles staat onder `src/main/resources/config/`.

| Map | Inhoud | Aantal |
| --- | --- | --- |
| `bpmn/` | Procesmodellen | 126 |
| `dmn/` | Beslistabellen | 15 |
| `document/definition/` | Zaakdossierschema's en referentieschema's | 76 |
| `form/` | Form.io-formulieren voor taken en tabbladen | 74 |
| `form-flow/` | Meerstapsformulieren | 3 |
| `case/` | Zaakdefinities, statussen, labels, zaaklijsten | 8 |
| `tabs/` | Indeling van het zaakscherm | 1 |
| `dashboard/` | Dashboards en widgets | 4 |
| `search/` | Zoekvelden per zaaktype | 2 |
| `dropdown/` | Keuzelijsten | 2 |
| `pluginconfig/` | Plugininstellingen | 7 |
| `process-link/` | Koppeling processtap ↔ formulier of plugin | 78 |
| `process-document-link/` | Welke processen een zaak starten of door de gebruiker gestart mogen worden | 1 |
| `objectmanagement/` | Objecttypen in de Objects API | 4 |
| `valuemapping/` | Omzetting portaalverzoek naar dossier | 2 |
| `template/` | FreeMarker-sjablonen voor brieven en afgeleide velden | 18 |
| `pbac/` | Rollen en permissies | 2 |
| `zgw/` | Velden bij documentupload | 1 |
| `documenten-api/` | Instellingen Documenten API | 1 |

## De BPMN-indeling

De procesmodellen zijn in vier groepen verdeeld. Die indeling is wat hergebruik tussen de regelingen mogelijk maakt.

| Map | Rol |
| --- | --- |
| `bpmn/aanvraag-levensonderhoud/algemene-bijstand-dcm/` | Zaakproces en startprocessen voor Algemene bijstand. |
| `bpmn/aanvraag-levensonderhoud/ioaw-dcm/` | Idem voor IOAW. |
| `bpmn/aanvraag-levensonderhoud/shared/` | Gedeeld tussen beide regelingen: brongegevens ophalen, documenten genereren, adrescontrole. |
| `bpmn/business-service/` | De inhoudelijke business services. |
| `bpmn/business-service-bouwblok/` | De omhulsels eromheen. |
| `bpmn/generic/` | Regelingonafhankelijk: informatieverzoeken, Suwinet-bevragingen, status bijwerken, besluiten vastleggen, betrokkenen informeren. |

Zie [Architectuur](../overzicht/architectuur.md#de-procesarchitectuur-drie-lagen).

## Changeset-ID's

Veel configuratiebestanden beginnen met een `changesetId`:

```json
{
  "changesetId": "aanvraag-algemene-bijstand-dcm.v2",
  "internalCaseStatuses": [ … ]
}
```

Dat ID bepaalt of de wijziging bij het opstarten wordt toegepast. Is het ID al eerder uitgerold, dan gebeurt er niets — ook niet als de inhoud is veranderd.

{% hint style="warning" %}
**Wijzig je de inhoud, verhoog dan het changeset-ID.** Vergeet je dat, dan start de applicatie zonder foutmelding op met de óúde configuratie, en ben je lang op zoek naar waarom je wijziging niet werkt.
{% endhint %}

Changeset-ID's kom je tegen bij interne statussen, labels, tabbladen, dashboards, rollen en permissies.

## Process links

Een processtap in BPMN zegt alleen *dát* er iets moet gebeuren. Wát er gebeurt, staat in een **process link**: een koppeling tussen de stap en een formulier, een formulierstroom of een plugin-actie.

| Soort | Betekenis |
| --- | --- |
| Formulier | De gebruikerstaak toont dit Form.io-formulier. |
| Formulierstroom | De taak doorloopt meerdere formulieren achter elkaar. |
| Plugin-actie | De stap roept een plugin aan, bijvoorbeeld het ophalen van Suwinet-gegevens. |

Deze scheiding maakt het mogelijk om een formulier aan te passen zonder het procesmodel aan te raken, en andersom.

Daarnaast legt `process-document-link` vast welke processen een zaak mogen aanmaken en welke de behandelaar zelf mag starten. Alleen `ab-afhandelen-aanvraag-dcm` en `ioaw-afhandelen-aanvraag-dcm` mogen een zaak initialiseren; de startprocessen voor behandelaarsacties zijn door de gebruiker startbaar.

## Omgevingsvariabelen

Alle omgevingsafhankelijke waarden staan als placeholder in de configuratie:

```json
"url": "${AUTODEPLOYMENT_PLUGINCONFIG_ZAKEN-API_URL}"
```

Ze worden bij het opstarten gevuld. Lokaal komen ze uit `.env.properties` in de projectroot; op andere omgevingen uit het secretbeheer van die omgeving.

De variabelen vallen uiteen in groepen:

| Groep | Voorbeeld |
| --- | --- |
| Database | `SPRING_DATASOURCE_URL`, `…_USERNAME`, `…_PASSWORD` |
| Keycloak | `SPRING_SECURITY_OAUTH2_…` |
| RabbitMQ | `SPRING_RABBITMQ_HOST`, `…_PORT` |
| Open Zaak | `AUTODEPLOYMENT_PLUGINCONFIG_ZAKEN-API_URL`, `…_CATALOGI-API_URL`, … |
| Objects API | `AUTODEPLOYMENT_OBJECTMANAGEMENT_…_OBJECTTYPE_UUID` |
| Suwinet | `AUTODEPLOYMENT_PLUGINCONFIG_SUWINET_…` |
| Haal Centraal | `AUTODEPLOYMENT_PLUGINCONFIG_HAALCENTRAAL_…` |
| Socrates | `AUTODEPLOYMENT_PLUGINCONFIG_SOCRATES_URL` |
| SMTP | `AUTODEPLOYMENT_PLUGINCONFIG_SMTP_MAIL_CONFIGURATION_…` |
| Organisatie | `AUTODEPLOYMENT_PLUGINCONFIG_BRONORGANISATIE_RSIN` |

{% hint style="danger" %}
`.env.properties` bevat wachtwoorden en API-sleutels en hoort **niet** in versiebeheer. Gebruik `.env.properties.example` als vertrekpunt.
{% endhint %}

## Technische stack

| | |
| --- | --- |
| Valtimo | 12.47.0 |
| Spring Boot | 3.5.10 |
| Kotlin | 2.1.20 |
| Java | 17 |
| PostgreSQL-driver | 42.7.4 |

De Valtimo-versie is bijgewerkt in [Release Junin](../releasenotes/junin.md). De actuele versies staan altijd in `gradle.properties`.

Plugins worden als losse afhankelijkheden meegeleverd: `externe-klanttaak`, `freemarker`, `haal-centraal`, `haal-centraal-authentication`, `object-management`, `smtpmail`, `socrates`, `suwinet`, `suwinet-auth`, `valuemapper`.

Codekwaliteit wordt bewaakt met **ktlint** en **Spotless**. Afhankelijkheden worden automatisch bijgewerkt via **Renovate**.

## Veelvoorkomende wijzigingen

{% tabs %}
{% tab title="Normbedragen indexeren" %}
De bijstandsnormen worden halfjaarlijks aangepast. Voeg een regel toe aan de beslistabel `config/dmn/alo-dcm/bs-219-bepalen-basisnormbedrag.dmn` met het nieuwe datumbereik en de twintig bedragen.

Let op dat het datumbereik van de vórige regel aansluit, zodat er geen gat ontstaat.
{% endtab %}

{% tab title="Informatieverzoek-item toevoegen" %}
Geen release nodig. De items staan als object in de Objects API en zijn via het datamenu in de applicatie te onderhouden.
{% endtab %}

{% tab title="Veld op een tabblad" %}
Pas het Form.io-formulier in `config/form/` aan dat aan het tabblad gekoppeld is. Staat het veld nog niet in het dossierschema, voeg het dan ook toe aan `config/document/definition/`.
{% endtab %}

{% tab title="Gedrag van de regie" %}
Pas `config/dmn/alo-dcm/besturen-business-services.dmn` aan. Houd rekening met de hit policy **FIRST**: de eerste passende regel wint, dus de volgorde is betekenisvol.

Controleer ook of de afgeleide beslissing *Fase 'vaststellen' afgerond* mee moet veranderen.
{% endtab %}
{% endtabs %}

## Testen

De testopzet gebruikt `camunda-bpm-assert` en `camunda-bpm-assert-scenario`, waarmee procesverlopen getest kunnen worden zonder de volledige stack te starten. Het Camunda-platform wordt gemockt met `camunda-bpm-mockito`.
