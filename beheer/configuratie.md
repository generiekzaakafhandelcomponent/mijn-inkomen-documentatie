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
| --- | --- | --: |
| `building-block/` | De bouwblokken: per blok een eigen map met procesmodel, formulieren, process-links en documentdefinitie | 481 |
| `case/` | Zaakdefinities per zaaktype, geversioneerd als `case/<zaaktype>/<versie>/` | 247 |
| `document/` | Gedeelde document- en referentieschema's | 75 |
| `global/` | Formulieren en process-links die over bouwblokken heen worden gebruikt | 9 |
| `pbac/` | Rollen en permissies, één bestand per rol | 12 |
| `pluginconfig/` | Plugininstellingen per omgeving | 7 |
| `objectmanagement/` | Objecttypen in de Objects API | 5 |
| `dashboard/` | Dashboards en widgets | 4 |
| `valuemapping/` | Omzetting portaalverzoek naar dossier | 2 |
| `dropdown/` | Keuzelijsten | 2 |

{% hint style="warning" %}
**Deze indeling is nieuw in v13.** Tot v12 stonden procesmodellen, formulieren en process-links in losse mappen (`bpmn/`, `form/`, `process-link/`, `tabs/`). Nu hoort alles wat bij één bouwblok hoort bij elkaar in één map onder `building-block/`.

Kom je oudere documentatie of voorbeelden tegen die naar `config/bpmn/...` verwijzen, dan gaat dat over v12.
{% endhint %}

## De bouwblokindeling

De zestig mappen onder `building-block/` volgen de business services die ze implementeren:

| Soort bouwblok | Voorbeelden |
| --- | --- |
| Vaststellingen | `bs-211-vaststelling-persoon`, `bs-214-vaststelling-vermogen`, `bs-224-vaststelling-inkomen` |
| Procesondersteunend | `bs-afsluiten-zaak`, `alo-genereer-document`, `alo-genereer-rapportage` |
| Gemeentespecifiek | `alo-gemeente-configuratie` |

Elk blok is daarmee een op zichzelf staand geheel: je kunt één vaststelling aanpassen zonder in gedeelde mappen te hoeven zoeken.

{% hint style="info" %}
In v13 krijgt **elk bouwblok een eigen documentdefinitie**. Naast het zaakdossier `aanvraag-algemene-bijstand-dcm` zie je in de database dus ook documenten als `bs-211-vaststelling-persoon` en `uitvoeren-business-services`. Dat is bedoeld: elk blok beheert zijn eigen gegevens.
{% endhint %}

## Waar een bouwblok uit bestaat

Binnen één map onder `building-block/` staat alles wat bij dat blok hoort:

| Onderdeel | Rol |
| --- | --- |
| Procesmodel | Het BPMN-model van het bouwblok. |
| Formulieren | De Form.io-formulieren voor de taken erin. |
| Process-links | De koppeling tussen processtap en formulier of plugin-actie. |
| Documentdefinitie | Het JSON-schema van de gegevens die het blok beheert. |
| Beslistabellen | De DMN-tabellen die bij dit blok horen. |

Wat over bouwblokken heen wordt gedeeld — bijvoorbeeld generieke formulieren — staat in `global/`.

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

Daarnaast legt `process-document-link` vast welke processen een zaak mogen aanmaken en welke de behandelaar zelf mag starten. Alleen de twee zaakprocessen — *Algemene bijstand aanvraag* (`ab-afhandelen-aanvraag-dcm`) en *IOAW aanvraag* (`ioaw-afhandelen-aanvraag-dcm`) — mogen een zaak initialiseren; de startprocessen voor behandelaarsacties zijn door de gebruiker startbaar.

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
| Valtimo | 13.54.0-1 |
| Procesengine | **Operaton** |
| Java | 21 |
| Taal | Kotlin |

De actuele versies staan altijd in `gradle.properties`.

{% hint style="warning" %}
**v13 draait op Operaton, niet meer op Camunda.** Operaton is de open source voortzetting van Camunda 7. Voor de modellen verandert er weinig — het blijft BPMN 2.0 en DMN — maar in logregels en stacktraces zie je `org.operaton.*` in plaats van `org.camunda.*`.
{% endhint %}

Plugins worden als losse afhankelijkheden meegeleverd: `externe-klanttaak`, `freemarker`, `haal-centraal`, `haal-centraal-authentication`, `object-management`, `smtpmail`, `socrates`, `suwinet`, `suwinet-auth`, `valuemapper`.

Codekwaliteit wordt bewaakt met **ktlint** en **Spotless**. Afhankelijkheden worden automatisch bijgewerkt via **Renovate**.

## Veelvoorkomende wijzigingen

{% tabs %}
{% tab title="Normbedragen indexeren" %}
De bijstandsnormen worden halfjaarlijks aangepast. Voeg een regel toe aan de beslistabel de beslistabel `bs-219-bepalen-basisnormbedrag` in het bouwblok `bs-219-vaststelling-norm` met het nieuwe datumbereik en de twintig bedragen.

Let op dat het datumbereik van de vórige regel aansluit, zodat er geen gat ontstaat.
{% endtab %}

{% tab title="Informatieverzoek-item toevoegen" %}
Geen release nodig. De items staan als object in de Objects API en zijn via het datamenu in de applicatie te onderhouden.
{% endtab %}

{% tab title="Veld op een tabblad" %}
Pas het Form.io-formulier aan in de map van het betreffende bouwblok. Staat het veld nog niet in het schema, voeg het dan ook toe aan de documentdefinitie van dat blok.
{% endtab %}

{% tab title="Gedrag van de regie" %}
Pas de beslistabel `besturen-business-services` aan. Houd rekening met de hit policy **FIRST**: de eerste passende regel wint, dus de volgorde is betekenisvol.

Controleer ook of de afgeleide beslissing *Fase 'vaststellen' afgerond* mee moet veranderen.
{% endtab %}
{% endtabs %}

## Testen

De testopzet test procesverlopen zonder de volledige stack te starten, met de assert- en scenario-bibliotheken van de procesengine.
