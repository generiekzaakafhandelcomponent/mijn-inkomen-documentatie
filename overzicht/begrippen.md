---
description: De termen die in Mijn Inkomen en in deze documentatie worden gebruikt.
---

# Begrippenlijst

## Regelingen en beleid

| Term | Betekenis |
| --- | --- |
| **ALO** | Aanvraag Levensonderhoud. Verzamelnaam voor beide regelingen; je ziet het terug als voorvoegsel in bestandsnamen en formulieren. |
| **Algemene bijstand** | Uitkering op grond van de Participatiewet voor wie niet genoeg inkomen of vermogen heeft om in het levensonderhoud te voorzien. |
| **IOAW** | Wet inkomensvoorziening oudere en gedeeltelijk arbeidsongeschikte werkloze werknemers. Anders dan bij bijstand telt vermogen hier niet mee. |
| **Bijstandsvorm** | De vorm waarin bijstand wordt verleend, bijvoorbeeld om niet of als lening. |
| **Norm** | Het bedrag waar iemand maandelijks recht op heeft, afhankelijk van leefsituatie en leeftijd. |
| **Kostendelersnorm** | Verlaging van de norm wanneer iemand de woning deelt met andere volwassenen. |
| **Uitsluitingsgronden** | Omstandigheden die recht op uitkering uitsluiten, bijvoorbeeld detentie of verblijf in het buitenland. |
| **Voorliggende voorziening** | Een andere regeling die vóór de bijstand gaat; bestaat die, dan is er geen recht op bijstand. |
| **Verblijfstitel** | De verblijfsstatus van de aanvrager; bepaalt mede of er recht op uitkering bestaat. |
| **Voorschot** | Vooruitbetaling tijdens de behandeling, zodat de inwoner niet zonder inkomen zit terwijl de aanvraag loopt. |
| **Buiten behandeling stellen** | De aanvraag niet inhoudelijk beoordelen omdat de inwoner gevraagde gegevens niet heeft aangeleverd. |
| **Bezwaartermijn** | De periode waarbinnen de inwoner bezwaar kan maken tegen het besluit. De zaak sluit pas daarna. |
| **Poortonderzoek** | Onderzoek aan de voorkant van de aanvraag, wanneer er aanleiding is om de rechtmatigheid extra te toetsen. |

## Zaakafhandeling

| Term | Betekenis |
| --- | --- |
| **Zaak** | De formele registratie van de aanvraag in Open Zaak. |
| **Zaakdossier** | Het JSON-werkdocument binnen Mijn Inkomen waarin alle gegevens van de behandeling staan. |
| **Zaaktype** | Het soort zaak; in Mijn Inkomen `aanvraag-algemene-bijstand-dcm` of `aanvraag-ioaw-uitkering-dcm`. |
| **Interne status** | De voortgangsstatus die de behandelaar in de zaaklijst ziet, los van de formele status in Open Zaak. |
| **Label (case tag)** | Vrij toe te kennen markering op een zaak, bijvoorbeeld *Voorschot* of *Te laat*. |
| **Behandelaar** | De medewerker aan wie de zaak is toegewezen. |
| **Informatieverzoek** | Verzoek aan de inwoner om aanvullende gegevens of documenten, met een deadline. |
| **Portaaltaak** | Een taak die in het klantportaal bij de inwoner verschijnt. |
| **Hersteltermijn** | De termijn die de inwoner krijgt om ontbrekende gegevens aan te leveren. |
| **Besluit** | De uitkomst van de aanvraag: toegekend, afgewezen, ingetrokken of buiten behandeling gesteld. |
| **Resultaattype** | De formele vastlegging van die uitkomst in Open Zaak. |

## Procesarchitectuur

| Term | Betekenis |
| --- | --- |
| **DCM** | Dynamic Case Management. Behandeling als een verzameling losse, door regels aangestuurde brokjes werk in plaats van een vast stappenplan. |
| **Business service (BS)** | Eén afgebakend stuk inhoudelijk werk, bijvoorbeeld *vaststelling vermogen*. Genummerd volgens de landelijke referentie, zoals BS 214. |
| **Business service bouwblok (BSB)** | Het omhulsel om een business service dat status, annulering en terugmelding regelt. Sinds v13 is een bouwblok ook de eenheid van configuratie: één map met procesmodel, formulieren, links en schema. |
| **Fase** | De stand van de behandeling: `vaststellen-belanghebbenden`, `opvoeren-dienst`, `vaststellen`, `beslissen`, `beslist`, `intrekken`, `buiten-behandeling-stellen`, `afsluiten`. |
| **Gebeurtenis** | Een melding dat er iets is gebeurd, bijvoorbeeld `vermogen-vastgesteld`. Hierop reageert de regie. |
| **Vaststelling** | Het door de behandelaar bevestigen of corrigeren van een gegeven, waarmee het de officiële waarde voor de beoordeling wordt. |
| **Brongegevens** | Gegevens die automatisch bij landelijke registraties zijn opgehaald. |

## Techniek

| Term | Betekenis |
| --- | --- |
| **GZAC** | Generiek Zaakafhandelcomponent: het open source zaakafhandelplatform waarop Mijn Inkomen draait. |
| **Valtimo** | Het onderliggende platform van GZAC, geleverd door Ritense. |
| **Operaton** | De procesengine die de BPMN-modellen en DMN-tabellen uitvoert. Open source voortzetting van Camunda 7; tot v12 heette dit Camunda. |
| **BPMN** | Business Process Model and Notation: de modelleertaal voor de processen. |
| **DMN** | Decision Model and Notation: de taal voor de beslistabellen. |
| **ZGW-API's** | De Nederlandse standaard-API's voor zaakgericht werken: Zaken, Catalogi, Documenten en Besluiten. |
| **Open Zaak** | De implementatie van de ZGW-API's die als zaakregistratie wordt gebruikt. |
| **Objects API** | Generieke opslag voor gestructureerde objecten; gebruikt voor verzoeken en portaaltaken. |
| **Suwinet** | Het landelijke netwerk waarmee gemeenten gegevens van UWV, SVB, DUO, RDW en Kadaster opvragen. |
| **Haal Centraal** | Landelijke API's voor onder meer BRP-bewoning en BAG-adresgegevens. |
| **Socrates** | De uitkeringsadministratie waarin de dienst wordt opgevoerd. |
| **Form.io** | De techniek waarmee de formulieren en zaaktabbladen zijn opgebouwd. |
| **SmartDocuments** | De documentgenerator waarmee brieven worden opgemaakt. |
| **Printstraat** | De centrale voorziening waaraan gegenereerde brieven worden aangeboden om afgedrukt en verzonden te worden. |
| **Plugin** | Herbruikbare koppeling naar een extern systeem, configureerbaar per omgeving. |
| **Process link** | De verbinding tussen een processtap en wat daar moet gebeuren: een formulier tonen of een plugin aanroepen. |

## Zaakprocessen

De configuratie gebruikt technische procesnamen. Dit zijn de functionele equivalenten:

| Functionele naam | Proces in de configuratie |
| --- | --- |
| Algemene bijstand aanvraag | `ab-afhandelen-aanvraag-dcm` |
| IOAW aanvraag | `ioaw-afhandelen-aanvraag-dcm` |
| Basisafhandelproces | `basisafhandelproces-afhandelen-aanvraag` |

Het **Basisafhandelproces** is het regelingonafhankelijke afhandelproces dat met v13 is bijgekomen; een deel van de bouwblokken is zowel vanuit de twee regelingen als vanuit dit proces bereikbaar.
