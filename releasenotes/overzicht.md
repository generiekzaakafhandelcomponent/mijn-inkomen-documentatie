---
description: Alle releases van Mijn Inkomen op een rij, van MVP tot nu.
---

# Overzicht

Mijn Inkomen is stapsgewijs opgebouwd. Elke release voegde functionaliteit toe of verbeterde bestaande onderdelen. De releases zijn vernoemd naar meren, in alfabetische volgorde.

| Release | Periode | Belangrijkste inhoud |
| --- | --- | --- |
| **MVP** | — | Basisproces aanvraagafhandeling met dynamisch casemanagement. |
| **Como** | — | Beoordelingen relaties, norm en woonsituatie; besluitbeheer. |
| **Darbon** | — | Beoordelingen vermogen en inkomen; verbeterde Suwinet-koppeling. |
| **Eder** | t/m april 2026 | Automatische Socrates-koppeling; beoordeling gezamenlijk inkomen. |
| **Finn** | — | Beoordeling voorliggende voorzieningen; autorisatiematrix. |
| **Garda** | april – mei 2026 | Beoordeling bijstandsvorm en uitsluitingsgronden; poortonderzoek. |
| **[Huron](huron.md)** | mei – september 2026 | Beheerde lijsten, documentgeneratie, gemeentespecifieke configuratie. |
| **[Inari](inari.md)** | september – oktober 2026 | Overstap naar GZAC v13; informatieverzoek- en briefproces herzien. |
| **[Junin](junin.md)** | oktober 2026 – heden | Informatieverzoek, eerste Printstraat, platform naar 13.54. |

{% hint style="info" %}
**De releasenamen komen van het platform.** Ritense geeft Valtimo-releases merennamen; Mijn Inkomen hangt zijn opleveringen daaraan op. In de code zie je dat terug als commits met teksten als *"upgraded Valtimo to V13 Inari release"*.
{% endhint %}

## Hoe deze notities tot stand kwamen

| Release | Bron |
| --- | --- |
| MVP t/m Finn | De functionele documentatie van het project. Deze releases vallen buiten de huidige repository-historie. |
| Garda, Huron, Inari | Gereconstrueerd uit de commits in `mijn-inkomen-gzac-backend`. |
| Junin | Aangeleverde releasenotes van het team. |

{% hint style="warning" %}
**Huron en Inari zijn achteraf samengesteld uit de code.** Ze beschrijven wat er technisch is veranderd, niet wat het team als functionele mijlpaal had opgeschreven. Voor een formele verantwoording zijn ze geen vervanging van de releasenotes van het team zelf.

De repository-historie van Mijn Inkomen begint op 13 april 2026; alles daarvóór is de geschiedenis van het GZAC-sjabloon waarop de applicatie is gebouwd.
{% endhint %}
