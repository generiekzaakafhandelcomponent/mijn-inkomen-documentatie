---
description: >-
  Welke rollen er zijn binnen Mijn Inkomen en wat elke rol precies mag —
  per dossier, tabblad, dashboard en taak.
---

# Rollen en rechten

Mijn Inkomen regelt autorisatie met **PBAC**: per rol is vastgelegd welke actie op welk soort object is toegestaan, afgebakend op dossiertype. Een rol krijgt dus niet "toegang tot de applicatie", maar een precies omschreven set van rechten.

{% hint style="info" %}
Deze kruisjeslijst is afgeleid uit de beoordeelde PBAC-lijst van release **v-inari-2.10** en beschrijft de elf rollen van het inkomensdomein. In dezelfde GZAC-omgeving draaien ook andere domeinen met hun eigen rollen; die vallen buiten deze documentatie.
{% endhint %}

## De rollen

| Rol | Rolsleutel | Aantal rechten |
| --- | --- | --: |
| Behandelaar | `ROLE_IV_BEHANDELAAR` | 83 |
| Senior | `ROLE_IV_SENIOR` | 89 |
| Superuser | `ROLE_IV_SUPERUSER` | 89 |
| Management | `ROLE_IV_MANAGEMENT` | 69 |
| Functioneel beheer | `ROLE_IV_FUNCTIONEEL_BEHEER` | 77 |
| Brede intake | `ROLE_IV_BREDE_INTAKE` | 32 |
| Raadpleger | `ROLE_IV_RAADPLEGER` | 36 |
| Raadpleger plus | `ROLE_IV_RAADPLEGER_PLUS` | 42 |
| Raadpleger doc | `ROLE_IV_RAADPLEGER_DOC` | 42 |
| Raadpleger compleet | `ROLE_IV_RAADPLEGER_COMPLEET` | 44 |
| Raadpleger basis | `ROLE_IV_RAADPLEGER_BASIS` | **0** |

Grofweg drie groepen: **uitvoerend** (Behandelaar, Senior, Superuser) mag dossiers wijzigen en taken afronden; **sturend** (Management, Functioneel beheer) mag toewijzen en meekijken op de dashboards; **raadplegend** (de vier Raadpleger-varianten en Brede intake) mag uitsluitend lezen, elk met een eigen snede van tabbladen en documenten.

{% hint style="warning" %}
**`ROLE_IV_RAADPLEGER_BASIS` heeft geen enkel recht.** Er bestaat geen permissiebestand voor deze rol. Wie hem toegewezen krijgt, ziet niets. Hetzelfde geldt voor de generieke `ROLE_USER`, waarvan de permissielijst leeg is.
{% endhint %}

### Gelijk voor beide regelingen

De rechten voor Algemene bijstand en IOAW zijn **exact identiek** — op geen van de 264 rechten per regeling verschillen ze. De matrices hieronder gelden daarom voor beide zaaktypen.

## Legenda

| | |
| --- | --- |
| **x** | Recht toegekend, expliciet benoemd in de permissieregel. |
| **x¹** | Alleen voor eigen notities (`createdByUserId`). |
| **x²** | Met uitzondering van informatieobjecttype *SUWI rapportage*. |
| *leeg* | Geen recht. |

Alle rechten van deze elf rollen zijn expliciet op dossiertype afgebakend; geen van hen krijgt rechten via een regel zonder afbakening.

## Dossier

Wat een rol met het zaakdossier zelf mag.

| Recht | Behandelaar | Senior | Superuser | Management | Func. beheer | Brede intake | Raadpleger | Raadpl. plus | Raadpl. doc | Raadpl. compl. | Raadpl. basis |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| inzien | x | x | x | x | x | x | x | x | x | x | |
| lijst inzien | x | x | x | x | x | x | x | x | x | x | |
| aanmaken | x | x | x | | x | | | | | | |
| wijzigen | x | x | x | x | x | | | | | | |
| verwijderen | | | | | | | | | | | |
| exporteren | x | x | x | x | x | x | | | | | |
| toeëigenen | x | x | x | | | | | | | | |
| toewijzen | x | x | x | x | x | | | | | | |
| toewijsbaar | x | x | x | | | | | | | | |

{% hint style="info" %}
**Niemand mag een dossier verwijderen.** Dat recht is aan geen enkele rol in het inkomensdomein toegekend — alleen de generieke beheerrol beschikt erover.

Let ook op het verschil tussen **toewijzen** en **toewijsbaar**: de eerste is het recht om een dossier aan iemand toe te kennen, de tweede betekent dat een rol zélf als behandelaar gekozen kan worden. Management en Functioneel beheer mogen wel toewijzen, maar zijn niet toewijsbaar — zij verdelen werk zonder het zelf te krijgen.
{% endhint %}

## Dossiertype

Rechten op de dossierdefinitie, die bepalen of een rol het zaaktype in menu's en lijsten terugziet.

| Recht | Behandelaar | Senior | Superuser | Management | Func. beheer | Brede intake | Raadpleger | Raadpl. plus | Raadpl. doc | Raadpl. compl. | Raadpl. basis |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| inzien | x | x | x | x | x | x | x | x | x | x | |
| lijst inzien | x | x | x | x | x | x | x | x | x | x | |
| aanmaken | x | x | x | | x | | | | | | |
| wijzigen | x | x | x | | x | | | | | | |
| verwijderen | | | | | | | | | | | |

## Tabbladen

Welke tabbladen van het zaakscherm een rol te zien krijgt. Dit is de fijnmazigste afbakening in de lijst.

| Tabblad | Behandelaar | Senior | Superuser | Management | Func. beheer | Brede intake | Raadpleger | Raadpl. plus | Raadpl. doc | Raadpl. compl. | Raadpl. basis |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Samenvatting | x | x | x | x | x | x | x | x | x | x | |
| Signalen | x | x | x | x | x | x | x | x | x | x | |
| Brede intake | | x | x | x | x | x | | | | | |
| Woonsituatie | x | x | x | x | x | x | x | x | x | x | |
| Inkomen | x | x | x | x | x | x | x | x | x | x | |
| Vermogen | x | x | x | x | x | x | x | x | x | x | |
| Suwinet | x | x | x | | | | | x | | x | |
| Bewoning | x | x | x | | | | | x | | x | |
| Poortonderzoek | x | x | x | x | x | | | | | x | |
| Informatieverzoeken | x | x | x | x | x | x | x | x | x | x | |
| Documenten | x | x | x | x | x | x | x | x | x | x | |
| Notities | x | x | x | x | x | | | x | | x | |
| Voortgang | | x | x | | x | | | | | | |
| Audit | x | x | x | x | x | | x | x | x | x | |

{% hint style="warning" %}
**Suwinet en Bewoning zijn bewust schaars toegekend.** Die tabbladen tonen rechtstreeks opgehaalde brongegevens over inkomen, vermogen en wie er op een adres woont. Alleen de uitvoerende rollen en twee raadplegervarianten komen erbij — Management en Functioneel beheer niet.

Dat is doelbinding in de praktijk: wie het dossier niet inhoudelijk beoordeelt, heeft de ruwe brongegevens niet nodig.
{% endhint %}

De Brede intake-rol heeft een opvallend profiel: wél het tabblad *Brede intake*, maar géén toegang tot notities, voortgang en audit. Een Behandelaar heeft juist géén toegang tot *Brede intake* en *Voortgang*.

## Notities

| Recht | Behandelaar | Senior | Superuser | Management | Func. beheer | Brede intake | Raadpleger | Raadpl. plus | Raadpl. doc | Raadpl. compl. | Raadpl. basis |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| inzien | x | x | x | x | x | | x | x | x | x | |
| lijst inzien | x | x | x | x | x | | x | x | x | x | |
| aanmaken | x | x | x | x | x | | | | | | |
| wijzigen | x¹ | x | x | x | x | | | | | | |
| verwijderen | x¹ | x | x | x | x | | | | | | |

Een Behandelaar mag alleen zijn **eigen** notities aanpassen of verwijderen. Senior, Superuser, Management en Functioneel beheer mogen dat bij alle notities.

## Documenten (ZGW-bestanden)

| Recht | Behandelaar | Senior | Superuser | Management | Func. beheer | Brede intake | Raadpleger | Raadpl. plus | Raadpl. doc | Raadpl. compl. | Raadpl. basis |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| inzien | x | x | x | x² | x² | x² | x² | x | x² | x | |
| lijst inzien | x | x | x | x² | x | x | x | x | x | x | |
| aanmaken | x | x | x | x² | x² | | | | x² | | |
| wijzigen | x | x | x | x² | x² | | | | x² | | |
| verwijderen | | x | x | x² | x² | | | | x² | | |

{% hint style="warning" %}
**De uitzondering op SUWI-rapportages is niet uniform toegepast.** Bij Management, Functioneel beheer, Brede intake, Raadpleger en Raadpleger doc geldt hij wél, bij Behandelaar, Senior, Superuser, Raadpleger plus en Raadpleger compleet niet — en bij Management ook op *lijst inzien*, terwijl Functioneel beheer daar juist alles mag zien.

Of dit zo bedoeld is, is een beleidsvraag; de lijst legt alleen vast wat er nu geconfigureerd staat. De moeite waard om bij een volgende review tegen het licht te houden.
{% endhint %}

## Zoekvelden

Alle tien de rollen met rechten mogen de zoekvelden van de zaaklijst gebruiken (`lijst inzien`). Alleen Raadpleger basis niet.

## Dashboards

| Dashboard | Behandelaar | Senior | Superuser | Management | Func. beheer | Brede intake | Raadpleger | Raadpl. plus | Raadpl. doc | Raadpl. compl. | Raadpl. basis |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Algemene Bijstand: Algemeen | x | x | x | x | x | | | | | | |
| Algemene Bijstand: Jouw overzicht | x | x | x | x | x | | | | | | |
| IOAW: Algemeen | x | x | x | x | x | | | | | | |
| IOAW: Jouw overzicht | x | x | x | x | x | | | | | | |

De dashboards zijn voorbehouden aan de vijf rollen die daadwerkelijk werk verzetten of verdelen. Raadplegende rollen krijgen geen stuurinformatie.

## Taken en processen

Deze rechten zijn niet op dossiertype afgebakend, maar op de rol zelf: een rol ziet de taken die aan de eigen rolgroep zijn gekoppeld.

| Rol | Taken inzien | Toeëigenen / toewijzen | Taak afronden | Proces starten |
| --- | :-: | :-: | :-: | :-: |
| Behandelaar | x | x | x | x |
| Senior | x | x | x | x |
| Superuser | x | x | x | x |
| Management | x | | | x |
| Functioneel beheer | x | | | x |
| Raadpleger | x | | | |
| Raadpleger plus | x | | | |
| Raadpleger doc | x | | | |
| Raadpleger compleet | x | | | |
| Brede intake | | | | |
| Raadpleger basis | | | | |

Het recht om een proces te starten is beperkt tot een vaste set: het zaakproces *Algemene bijstand aanvraag* (`ab-afhandelen-aanvraag-dcm`) plus de startprocessen `ab-start-buiten-behandeling-stellen`, `ab-start-intrekken-aanvraag` en `ab-start-behandeling-gehele-aanvraag-opnieuw`.

{% hint style="info" %}
**Alleen de drie uitvoerende rollen kunnen werk afronden.** Management en Functioneel beheer zien taken en mogen processen starten, maar kunnen een taak niet zelf afmaken. Dat houdt besluitvorming bij de behandelaars.
{% endhint %}

## Waar staat de configuratie

De permissies staan in `config/pbac/`, met één bestand per rol (bijvoorbeeld `role-iv-behandelaar-v1.permission.json`) en de rollenlijst in een apart bestand. Elke regel koppelt een resourcetype aan een actie, een rol en een reeks condities.

Zie [Configuratie](../beheer/configuratie.md) voor hoe deze bestanden worden uitgerold, en [Werken in de applicatie](werken-in-de-applicatie.md) voor de tabbladen en dashboards waar deze rechten op slaan.
