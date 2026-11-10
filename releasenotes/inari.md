---
description: >-
  De overstap naar GZAC v13, met een herzien informatieverzoek- en briefproces
  en het opruimen van verouderde configuratie.
---

# Release Inari

Inari is vooral een **platformrelease**: Mijn Inkomen ging over van GZAC v12 naar v13. Daarnaast is het proces rond brieven en informatieverzoeken herzien en is een flinke hoeveelheid verouderde configuratie opgeruimd.

{% hint style="warning" %}
Deze notitie is achteraf samengesteld uit de commits van september en oktober 2026. Zie [Overzicht](overzicht.md#hoe-deze-notities-tot-stand-kwamen).
{% endhint %}

## Overstap naar v13

De applicatie is in stappen meegegaan met de Inari-releases van het platform: eerst Inari-2, daarna versie 2.17, en ten slotte de volledige overstap naar V13.

Dat is de grootste wijziging van deze release. De configuratie-indeling veranderde mee: alles wat bij één business service hoort kwam samen in bouwblokken, en de procesengine ging van Camunda naar Operaton. Zie [Configuratie](../beheer/configuratie.md).

{% hint style="info" %}
Bij een platformupgrade van deze omvang raken eigen wijzigingen soms overschreven. Dat gebeurde hier met de Socrates-koppeling: die is na de 2.17-update hersteld.
{% endhint %}

## Brieven en betrokkenen informeren

Het proces *Informeren betrokkenen met brief* is uitgebreid met nieuwe taken, onderbrekingen en statusovergangen. Daarbij zijn twee gegevens toegevoegd die eerder ontbraken: de sleutel van het mailsjabloon en de publieke referentie van de zaak, zodat de juiste brief bij de juiste zaak terechtkomt.

## Informatieverzoek

De informatieverzoekstroom is opgeschoond. Verouderde globale formulieren zijn verwijderd en er is een stap bijgekomen die de zaakdocumenten-plugin aanroept.

## Socrates

Naast het herstel van de koppeling na de platformupgrade is de mogelijkheid toegevoegd om het **opvoeren van de dienst over te slaan**. Dat geeft een uitweg wanneer de uitkeringsadministratie niet bereikbaar is, zodat de behandeling niet volledig vastloopt.

Zie [Werken met een dossier](../handleiding/werken-met-een-dossier.md) voor hoe dat er voor de behandelaar uitziet.

## Opruimen

* Verouderde configuratiebestanden verwijderd.
* Een vervallen rol uit de autorisatie gehaald.
* De externe-klanttaak-plugin bijgewerkt naar 3.0.5, de FreeMarker-plugin naar 8.6.0.

## Beheer en inzicht

Aan het Docker-image is een **OpenTelemetry-agent** toegevoegd. Daarmee kunnen beheerders zien waar tijd en geheugen blijven hangen — iets wat in deze release concreet is gebruikt bij het onderzoeken van een geheugenprobleem.
