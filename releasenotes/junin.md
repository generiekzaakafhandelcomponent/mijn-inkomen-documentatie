---
description: >-
  De introductie van Informatieverzoek, de eerste versie van de Printstraat, en
  een upgrade van het platform naar Valtimo 12.47.0.
---

# Release Junin

De belangrijkste onderdelen van deze release zijn de introductie van de functionaliteit **Informatieverzoek** en de **eerste versie van de Printstraat**. Daarnaast bevat deze release verbeteringen in de SmartDocuments-integratie, diverse optimalisaties van de gebruikersinterface en een upgrade van het onderliggende Valtimo-platform naar versie 12.47.0.

{% hint style="info" %}
Dit is de **huidige release**. Zie [Overzicht](overzicht.md) voor alle releases op een rij. Zie [Informatieverzoeken](../functionaliteit/informatieverzoek.md) voor de volledige functionele beschrijving van de nieuwe functionaliteit.
{% endhint %}

## In het kort

| Onderdeel | Wat er is gebeurd |
| --- | --- |
| **Informatieverzoek** | Nieuwe functionaliteit voor het opvragen en verwerken van aanvullende informatie en bewijsstukken. |
| **Printstraat** | Eerste versie: brieven worden aangeboden aan de centrale afdruk- en verzendvoorziening. |
| **SmartDocuments** | Verbeteringen in de integratie met de documentgenerator. |
| **Gebruikersinterface** | Nederlandse datumnotatie, minder blokkerende validatie, betere processelectie. |
| **Platform** | Valtimo/GZAC bijgewerkt naar 12.47.0. |

## Nieuwe functionaliteit: Informatieverzoek

Met deze release wordt de functionaliteit **Informatieverzoek** geïntroduceerd. Deze functionaliteit ondersteunt het opvragen en verwerken van aanvullende informatie en bewijsstukken binnen lopende processen.

De volgende onderdelen zijn gerealiseerd:

* Ondersteuning voor het **uploaden van meerdere bestanden** bij hetzelfde bewijsstuk.
* Verbeteringen rondom de **toelichting wanneer een opgevraagd document ontbreekt**.
* Bij het aanmaken van een brief wordt een **overzicht van de opgevraagde documenten** meegenomen.
* Alleen de **tekstvelden die van toepassing zijn** op het informatieverzoek worden getoond.
* Bij het uploaden van bestanden wordt informatie over het **bestandstype en bestandsformaat** weergegeven.
* De **sortering** van informatieverzoeken is omgedraaid.
* De **ja/nee-hersteltermijn** wordt meegenomen in het bericht naar de documentgenerator bij het aanmaken van een informatieverzoek.
* De lijst met **bewijsstukken bij op te vragen items** is geharmoniseerd.

## Eerste versie: Printstraat

Deze release bevat de eerste versie van de **Printstraat**: de centrale voorziening waarmee gegenereerde brieven worden afgedrukt en verzonden.

In het proces *Informeren betrokkenen met brief* wordt het gegenereerde document, samen met het zaaknummer, aangeboden aan de Printstraat. De fysieke verzending verloopt daarmee niet langer handmatig.

## Verbeteringen in de gebruikerservaring

Met Release Junin zijn verschillende verbeteringen doorgevoerd in de gebruikersinterface om het werken met de applicatie eenvoudiger en overzichtelijker te maken. De volgende verbeteringen zijn gerealiseerd:

* De **datumkiezers** zijn aangepast aan de Nederlandse notatie, zodat het selecteren en invoeren van datums beter aansluit op de Nederlandse werkwijze.
* Een **afwijkende periodiciteit bij inkomsten** is niet langer blokkerend, waardoor gebruikers verder kunnen met de verwerking.
* **Verbeterde processelectie** in het tabblad *Voortgang*. Hierdoor kunnen gebruikers sneller en eenvoudiger het juiste proces vinden.

## Upgrade naar 12.47.0

Met Release Junin is het onderliggende Valtimo/GZAC-platform bijgewerkt naar versie **12.47.0**. Deze upgrade bevat een verbetering in de **beveiliging en toegangscontrole van documenten**.

{% hint style="info" %}
**Versienummers verschillen per repository.** Mijn Inkomen wordt op meerdere plekken onderhouden, en die lopen niet gelijk op. Het nummer 12.47.0 hoort bij de repository waarvoor deze releasenotes zijn geschreven; de repository waarop deze documentatie is gebaseerd staat in dezelfde periode op **13.52** en later **13.54.0-1**.

Beide kloppen dus, voor hun eigen lijn. Ga voor de versie van jouw omgeving uit van de `gradle.properties` daarvan; zie [Configuratie](../beheer/configuratie.md#technische-stack).
{% endhint %}
