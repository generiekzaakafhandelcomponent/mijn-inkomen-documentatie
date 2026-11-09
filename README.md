---
description: >-
  Functionele documentatie van Mijn Inkomen: de zaakafhandeling voor aanvragen
  levensonderhoud (Algemene bijstand en IOAW) op basis van GZAC.
---

# Mijn Inkomen

**Mijn Inkomen** ondersteunt de behandeling van aanvragen levensonderhoud door een gemeente. Een inwoner dient een aanvraag in via het klantportaal; Mijn Inkomen maakt daar een zaakdossier van, haalt automatisch gegevens op bij landelijke bronnen, begeleidt de behandelaar door de beoordeling, en legt het besluit vast.

De applicatie ondersteunt twee regelingen:

| Regeling | Zaaktype | Grondslag |
| --- | --- | --- |
| **Algemene bijstand** | `aanvraag-algemene-bijstand-dcm` | Participatiewet |
| **IOAW** | `aanvraag-ioaw-uitkering-dcm` | Wet inkomensvoorziening oudere en gedeeltelijk arbeidsongeschikte werkloze werknemers |

## Wat maakt deze applicatie bijzonder

Mijn Inkomen is geen klassiek, lineair workflowsysteem. De behandeling is opgezet als **Dynamic Case Management (DCM)**: er is geen vast stappenplan dat van begin tot eind wordt doorlopen. In plaats daarvan bestaat de behandeling uit losse, herbruikbare brokjes werk — **business services** — die door een beslistabel worden aan- en uitgezet op basis van wat er in de zaak gebeurt.

Dat betekent in de praktijk:

* **Parallel werken.** Vermogen, inkomen, verblijfstitel en woonsituatie worden tegelijk vastgesteld, niet na elkaar.
* **Terugspringen kan.** Blijkt bij het beslissen dat het inkomen niet klopt? Dan start alleen die vaststelling opnieuw, zonder de rest van het dossier weg te gooien.
* **De zaak stuurt zichzelf.** Zodra alle vaststellingen afgerond zijn, schuift de zaak vanzelf door naar de beslisfase.

{% hint style="info" %}
De regie ligt bij één beslistabel: `besturen-business-services.dmn`. Die vertaalt *"wat is er zojuist gebeurd?"* naar *"wat moet er nu starten, en wat moet er stoppen?"*. Zie [Het aanvraagproces](functionaliteit/aanvraagproces.md).
{% endhint %}

## Waar begin je

{% tabs %}
{% tab title="Ik ben nieuw" %}
Lees eerst [Architectuur](overzicht/architectuur.md) voor het grote plaatje, daarna [Het aanvraagproces](functionaliteit/aanvraagproces.md) om te zien hoe een zaak loopt. De [Begrippenlijst](overzicht/begrippen.md) helpt bij de Nederlandse en GZAC-specifieke termen.
{% endtab %}

{% tab title="Ik ben behandelaar" %}
[Werken in de applicatie](functionaliteit/werken-in-de-applicatie.md) beschrijft de tabbladen, statussen, labels en dashboards. [Informatieverzoeken](functionaliteit/informatieverzoek.md) beschrijft het opvragen van aanvullende stukken bij de inwoner.
{% endtab %}

{% tab title="Ik ga ontwikkelen" %}
[Configuratie](beheer/configuratie.md) legt uit hoe de applicatie volledig vanuit configuratiebestanden wordt opgebouwd, en [Lokaal draaien](beheer/lokaal-draaien.md) hoe je de stack op je eigen machine start.
{% endtab %}
{% endtabs %}

## Technische basis

Mijn Inkomen is een implementatie bovenop **GZAC** (Generiek Zaakafhandelcomponent) en het **Valtimo**-platform. De applicatie zelf bevat vrijwel geen maatwerkcode: alle functionaliteit zit in configuratie — BPMN-procesmodellen, DMN-beslistabellen, JSON-schema's, Form.io-formulieren en pluginconfiguratie.

| | |
| --- | --- |
| Platform | GZAC / Valtimo |
| Taal & runtime | Kotlin, Java 21, Spring Boot |
| Procesengine | Operaton (BPMN 2.0 + DMN) |
| Database | PostgreSQL |
| Authenticatie | Keycloak (OAuth2 / OIDC) |
| Zaakregistratie | Open Zaak (ZGW API's) |

De broncode staat in de repository `mijn-inkomen-gzac-backend`, branch `develop`.
