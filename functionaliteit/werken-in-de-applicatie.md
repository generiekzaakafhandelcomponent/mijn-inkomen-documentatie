---
description: Het zaakscherm, de zaaklijst, statussen, labels en dashboards.
---

# Werken in de applicatie

## Het zaakscherm

Een zaak opent in een scherm met tabbladen. De eerste acht zijn inhoudelijk, de laatste vier ondersteunend.

| Tabblad | Wat je er vindt |
| --- | --- |
| **Samenvatting** | Het dossier in één oogopslag: aanvrager, status, kerngegevens. |
| **Brede Intake** | De intakegegevens: reden van de aanvraag, hulpvraag, bijzonderheden. |
| **Woonsituatie** | Waar en hoe de aanvrager woont, met wie, en het verblijfadres. |
| **Inkomen** | Alle inkomstenbronnen van aanvrager en partner, uit de aanvraag én uit de bronnen. |
| **Vermogen** | Bankrekeningen, bezittingen, schulden en eigen woning. |
| **Suwinet** | De ruwe gegevens zoals opgehaald bij UWV, SVB, DUO, RDW, Kadaster en BRP. |
| **Bewoning** | Wie er volgens de BRP op het adres staan ingeschreven. |
| **Informatieverzoeken** | Alle uitgezette verzoeken met items, deadline, status en ontvangen stukken. |
| **Voortgang** | Het procesverloop: welke stappen zijn doorlopen. |
| **Audit** | Het volledige wijzigingslogboek van het dossier. |
| **Documenten** | Alle documenten bij de zaak. |
| **Notities** | Vrije aantekeningen van de behandelaar. |

{% hint style="info" %}
Op de meeste tabbladen staan ook de **openstaande taken** voor dat onderwerp. Je hoeft dus niet naar een aparte takenlijst: op het tabblad *Vermogen* staan de vermogenstaken, op *Inkomen* de inkomenstaken.
{% endhint %}

De tabbladen *Inkomen* en *Vermogen* bestaan ook bij IOAW, maar blijven daar leeg: die regeling kent geen vermogens- of inkomenstoets.

## De zaaklijst

De zaaklijst toont twaalf kolommen:

| Kolom | Bron | Sorteerbaar |
| --- | --- | --- |
| Aanmaakdatum | Zaak | Ja — standaard aflopend |
| BSN | Dossier | Ja |
| Naam aanvrager | Afgeleid via teksttemplate | Nee |
| Postcode | Afgeleid via teksttemplate | Ja |
| Publieke referentie | Dossier | Ja |
| Zaaknummer | Open Zaak | Ja |
| Behandelaar | Zaak | Ja |
| Status | Interne status | Ja |
| Besluit | Afgeleid via teksttemplate | Nee |
| Uiterlijke einddatum afdoening | Open Zaak | Ja |
| Laatst gewijzigd | Zaak | Ja |
| Labels | Zaak | Nee |

### Zoeken en filteren

| Filter | Werking |
| --- | --- |
| Datumbereik | Zaken aangemaakt tussen twee data. |
| Publieke referentie | Gedeeltelijke match. |
| Zaaknummer | Gedeeltelijke match. |
| BSN | Gedeeltelijke match. |
| Achternaam aanvrager | Gedeeltelijke match. |
| Zaakresultaat | Keuzelijst: Verstrekt, Geweigerd, Buiten behandeling gesteld, Afgebroken. |
| Behandelaar | Gedeeltelijke match. |

Aanmaakdatum, BSN, publieke referentie, zaaknummer, behandelaar en status zijn ook exporteerbaar.

## Interne statussen

De interne status laat zien waar een zaak staat. Hij is losgekoppeld van de formele status in Open Zaak, zodat de behandelaar meer detail ziet dan de buitenwereld.

| Status | Kleur | Standaard in de lijst |
| --- | --- | --- |
| Aanvraag ontvangen | Grijs | Ja |
| In behandeling genomen | Blauw | Ja |
| Informatieverzoek uitgezet | Turquoise | Ja |
| Aanvullende informatie ontvangen | Groen | Ja |
| Geen aanvullende informatie ontvangen | Rood | Ja |
| Beslist | Omlijnd | Nee |
| Afgehandeld | Contrast | Nee |

{% hint style="info" %}
*Beslist* en *Afgehandeld* staan standaard **niet** in de zaaklijst. De lijst toont zo vanzelf het werk dat nog loopt; afgehandelde zaken zijn met een filter op te vragen.
{% endhint %}

## Labels

Labels zijn vrij toe te kennen markeringen, zichtbaar in de zaaklijst.

| Label | Kleur | Wanneer |
| --- | --- | --- |
| **Voorschot** | Rood | Er loopt een voorschot. Automatisch gezet en verwijderd door de voorschotservice. |
| **Te laat** | Rood | De afhandeltermijn is bijna verlopen. Automatisch gezet door de termijnbewaking. |
| **Achterstallig** | Magenta | De afhandeltermijn is verstreken. Automatisch gezet door de termijnbewaking. |
| **Verkorte aanvraagprocedure** | Turquoise | Bij initialisatie vastgesteld dat de verkorte procedure geldt. |

Alle vier worden automatisch gezet; handmatig toekennen kan ook.

## Dashboards

Er zijn vier dashboards: per regeling een algemeen overzicht en een persoonlijk overzicht.

| Dashboard | Scope |
| --- | --- |
| Algemene Bijstand: Algemeen | Alle AB-zaken. |
| Algemene Bijstand: Jouw overzicht | Alleen de zaken van de ingelogde behandelaar. |
| IOAW: Algemeen | Alle IOAW-zaken. |
| IOAW: Jouw overzicht | Alleen de eigen IOAW-zaken. |

Elk dashboard toont dezelfde acht widgets:

| Widget | Signaleert |
| --- | --- |
| Zaken die langer openstaan dan 4 weken | Dossiers die aandacht nodig hebben. |
| Zaken die langer openstaan dan 8 weken | Dossiers die te lang liggen. |
| Alle nieuwe zaken afgelopen 4 weken | Instroom. |
| Zaken afgelopen 4 weken, per status | Waar de werkvoorraad zit. |
| Zaken afgelopen 8 weken, per status | Verloop over langere termijn. |
| Alle besluiten afgelopen 4 weken | Uitstroom. |
| Uitstaande informatieverzoeken | Hoeveel dossiers op de inwoner wachten. |
| Poortonderzoek gestart, niet afgerond | Onderzoeken die blijven liggen. |

De tellers van openstaande zaken kijken naar zaken die niet de status *Afgehandeld* hebben; vanuit elke widget kun je doorklikken naar de onderliggende zaaklijst.

## Zaken toewijzen

Beide zaaktypen staan toe dat er een behandelaar aan de zaak wordt gekoppeld. De behandelaar is zichtbaar in de zaaklijst, filterbaar, en bepaalt wat er in het persoonlijke dashboard verschijnt.

## Beheerde lijsten

Twee lijsten zijn via het datamenu in de applicatie te onderhouden, zonder release:

| Lijst | Gebruikt voor |
| --- | --- |
| **ALO: Informatieverzoek Items** | De items die bij een informatieverzoek kunnen worden opgevraagd. |
| **Adressen met veel bewoners** | Adressen die aanleiding geven tot extra controle. |

Beide zijn opgeslagen als objecttype in de Objects API en hebben een eigen weergave- en bewerkformulier.

## Rechten

De applicatie kent twee rollen: `ROLE_USER` en `ROLE_ADMIN`. De permissies zijn per resourcetype en actie vastgelegd in `config/pbac/all.permission.json` — bijvoorbeeld welke rol zaken mag inzien, aanmaken, wijzigen, claimen of verwijderen. Gebruikers en hun rollen worden beheerd in Keycloak.
