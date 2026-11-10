---
description: >-
  Beheerde lijsten in de Objects API, documentgeneratie voor brieven, en de
  eerste stap naar gemeentespecifieke configuratie.
---

# Release Huron

Huron is de langstlopende release in deze reeks — ruim vier maanden. De rode draad: onderdelen die eerst vastzaten in de code werden **configureerbaar**, zodat een gemeente ze zelf kan inrichten zonder release.

{% hint style="warning" %}
Deze notitie is achteraf samengesteld uit de commits van mei tot en met september 2026. Zie [Overzicht](overzicht.md#hoe-deze-notities-tot-stand-kwamen).
{% endhint %}

## Beheerde lijsten

Twee lijsten zijn als objecttype in de Objects API gezet, inclusief automatische uitrol en de bijbehorende rechten:

* **ALO: Informatieverzoek Items** — de documenten die bij een informatieverzoek opgevraagd kunnen worden.
* **ALO: Adressen met veel bewoners** — de lijst die het handhavingssignaal voedt.

Daarmee kan een functioneel beheerder ze via het datamenu onderhouden. Zie [Werken in de applicatie](../functionaliteit/werken-in-de-applicatie.md).

## Documentgeneratie

Er is documentgeneratie toegevoegd voor het **informatieverzoek** en de **intrekkingsbrief**. Beide brieven worden sindsdien door het systeem opgemaakt in plaats van buiten de applicatie om.

## Gemeentespecifieke configuratie

De eerste stap naar een installatie die per gemeente verschilt: een eigen configuratieobject, met de bijbehorende formulieren, aangepaste zaaklijsten en schema's.

Hier hoort ook een kleine maar veelzeggende wijziging bij: in de brieftemplates is een specifieke gemeentenaam vervangen door het neutrale *gemeente*, zodat de sjablonen herbruikbaar zijn.

## Koppelingen

| Koppeling | Wat er veranderde |
| --- | --- |
| **Socrates** | Een simulatorcontainer toegevoegd zodat lokaal ontwikkelen kan zonder de echte administratie; pluginversie bijgewerkt. |
| **Suwinet** | Plugin en simulator bijgewerkt. |
| **Notificaties** | Plugininstellingen uit de algemene configuratie gehaald en bij de ZGW-instellingen ondergebracht. |

## Opruimen en vereenvoudigen

* Overbodige *ophalen brongegevens*-processen verwijderd.
* Maatwerkservices vervangen door scripttaken in het procesmodel — minder code, meer configuratie.
* Overbodige process-links en een dubbele permissie weggehaald.

## Beheer

* **Uploadlimieten** voor documenten ingesteld.
* **Logging** afgestemd op de standaardinstellingen van het platform.
* Interceptors toegevoegd die bij het opnieuw proberen van achtergrondtaken de context meenemen, zodat fouten terug te leiden zijn naar de zaak.
* Een **installatiehandleiding** aan de repository toegevoegd.
* De CI/CD-pipeline vernieuwd.

## Autorisatie

De PBAC-configuratie is in meerdere stappen bijgewerkt, waaronder een bugfix op de rechten voor ZGW-documenten en een permissie voor het externe-taakobject. Zie [Rollen en rechten](../functionaliteit/rollen-en-rechten.md).
