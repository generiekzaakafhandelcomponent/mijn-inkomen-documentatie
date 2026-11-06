---
description: De twee regelingen die Mijn Inkomen ondersteunt, en waarin ze verschillen.
---

# Zaaktypen

Mijn Inkomen ondersteunt twee regelingen voor levensonderhoud. Ze delen vrijwel de volledige inrichting: dezelfde processtructuur, dezelfde tabbladen, dezelfde statussen en labels. Het verschil zit in welke vaststellingen er nodig zijn.

| | Algemene bijstand | IOAW |
| --- | --- | --- |
| Zaaktype | `aanvraag-algemene-bijstand-dcm` | `aanvraag-ioaw-uitkering-dcm` |
| Dossiertype in de regie | `algemene-bijstand` | `ioaw-uitkering` |
| Grondslag | Participatiewet | IOAW |
| Procesvoorvoegsel | `ab-` | `ioaw-` |
| Vermogenstoets | Ja | Nee |
| Inkomenstoets | Ja | Nee |

## Algemene bijstand

Bijstand op grond van de Participatiewet, voor wie onvoldoende inkomen of vermogen heeft om in het levensonderhoud te voorzien. Dit is de uitgebreidste variant: zowel vermogen als inkomen moeten worden vastgesteld voordat er beslist kan worden.

## IOAW

De IOAW is bedoeld voor oudere en gedeeltelijk arbeidsongeschikte werkloze werknemers van wie de WW-uitkering afloopt. Kenmerkend voor deze regeling: **vermogen telt niet mee**. Wie een eigen huis of spaargeld heeft, kan toch recht hebben op IOAW.

Dat vertaalt zich direct naar de inrichting.

## Het verschil in de praktijk

De regie start bij het begin van de vaststellingsfase per regeling een andere set bouwblokken.

{% tabs %}
{% tab title="Algemene bijstand" %}
```
bsb-overwegen-inzetten-handhaving
bsb-overwegen-uitzetten-informatieverzoek
bsb-213-vaststelling-verblijfstitel-aanvrager
bsb-218-vaststelling-uitsluitingsgronden-aanvrager
bsb-442-vaststelling-identiteit-aanvrager
bsb-224-vaststelling-inkomen-aanvrager      ← alleen AB
bsb-214-vaststelling-vermogen               ← alleen AB
bsb-444-vaststelling-voorliggende-voorzieningen
bsb-221-vaststelling-ingangsdatum
```
De bijstandsvorm (BS 212) start hier pas later, zodra het vermogen is vastgesteld.
{% endtab %}

{% tab title="IOAW" %}
```
bsb-overwegen-inzetten-handhaving
bsb-overwegen-uitzetten-informatieverzoek
bsb-213-vaststelling-verblijfstitel-aanvrager
bsb-218-vaststelling-uitsluitingsgronden-aanvrager
bsb-442-vaststelling-identiteit-aanvrager
bsb-444-vaststelling-voorliggende-voorzieningen
bsb-221-vaststelling-ingangsdatum
bsb-212-vaststelling-bijstandsvorm          ← direct mee
```
Geen vermogen, geen inkomen. De bijstandsvorm start meteen, omdat er geen vermogensvaststelling is om op te wachten.
{% endtab %}
{% endtabs %}

Ook de controle *"is de vaststellingsfase afgerond?"* verschilt. Bij IOAW tellen vermogen (BS 214), norm (BS 219) en inkomen (BS 224 en 224b) niet mee — anders zou de zaak nooit doorschuiven naar het besluit.

{% hint style="info" %}
Beide verschillen zijn puur configuratie: twee regels in `besturen-business-services.dmn` voor de startset, en twee regels in de afgeleide beslissing *Fase 'vaststellen' afgerond*. Er is geen aparte code voor IOAW.
{% endhint %}

## Wat identiek is

| Onderdeel | Toelichting |
| --- | --- |
| **Interne statussen** | Beide zaaktypen kennen dezelfde zeven statussen. |
| **Labels** | *Voorschot*, *Te laat*, *Achterstallig*, *Verkorte aanvraagprocedure*. |
| **Tabbladen** | Identieke indeling van het zaakscherm, inclusief de tabbladen *Inkomen* en *Vermogen* — bij IOAW blijven die leeg. |
| **Zaaklijst en zoekvelden** | Dezelfde kolommen en filters. |
| **Dashboards** | Per regeling een eigen paar, met dezelfde widgets. |
| **Informatieverzoeken** | Volledig generiek, identiek voor beide. |
| **Besluittypen** | Dezelfde vier uitkomsten en resultaattypen. |
| **Brieven** | Dezelfde sjablonen, met per regeling een eigen koppelingsbestand. |

## Een derde regeling toevoegen

De opzet is erop gericht dat een extra regeling grotendeels met configuratie kan. In grote lijnen:

1. Een **zaakdossierschema** maken (`config/document/definition/`), met hergebruik van de bestaande referentieschema's.
2. Een **zaakproces** en **initialisatieproces** toevoegen, naar het model van `ab-afhandelen-aanvraag-dcm`.
3. De **startprocessen** voor behandelaarsacties toevoegen met het eigen voorvoegsel.
4. **Regels toevoegen** aan `besturen-business-services.dmn` voor het nieuwe dossiertype en de bijbehorende startset.
5. De afgeleide beslissing *Fase 'vaststellen' afgerond* uitbreiden met een regel voor het nieuwe type.
6. **Statussen, labels, tabbladen, zaaklijst, zoekvelden en dashboards** configureren.
7. Een regel toevoegen aan `alo-bepaal-dossiertype.dmn` die het zaaktype naar het dossiertype vertaalt.
8. De **verzoekplugin** uitbreiden met het nieuwe verzoektype en de bijbehorende mapping.

De business services zelf hoeven niet opnieuw gebouwd te worden: die zijn regelingonafhankelijk.
