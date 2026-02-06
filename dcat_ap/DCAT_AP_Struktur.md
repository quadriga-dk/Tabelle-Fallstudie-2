(dcat-dc)=
# Struktur und Elemente von DCAT-AP

Um die Grundlagen des DCAT-AP-Schemas zu verstehen, ist es wichtig, sich zunächst mit den zentralen Konzepten vertraut zu machen, auf denen es basiert. Ein wesentlicher Ursprung liegt in der *Dublin Core Metadata Workshop Series*, die 1995 ins Leben gerufen wurde. Diese Workshops brachten Fachleute aus verschiedenen Bereichen zusammen – darunter Bibliothekar:innen, Forschende im Bereich digitaler Bibliotheken sowie Expert:innen für Inhalte und Textverarbeitung. Ihr gemeinsames Ziel war es, Standards zu entwickeln, um die Auffindbarkeit elektronischer Ressourcen zu verbessern {cite}`Weibel1998RFC2413`.

## Metadatenstandard Dublin Core

<a href="https://www.dublincore.org/specifications/dublin-core/" class="external-link" target="_blank">*Dublin Core*</a> ist heute ein Schlüsselstandard im Umgang mit Metadaten. Da Metadaten die Grundlage für die Organisation und Verknüpfung von Informationen im Web bilden, ermöglicht dieser Standard, Inhalte und Dienste miteinander zu verbinden und sie für Benutzer zugänglicher zu machen. Die *Dublin Core Metadata Initiative (DCMI)* hat dazu beigetragen, ein flexibles Framework zu schaffen, das die Entwicklung von Metadatenformaten erleichtert und interdisziplinäre Entdeckungsmöglichkeiten fördert. Das Ergebnis ist ein Kernstandard, der mittlerweile in 25 Sprachen übersetzt wurde und bis heute eine wichtige Rolle bei der Strukturierung und Auffindbarkeit von Informationen spielt {cite}`WeibelKoch2000DublinCore`.

Der *Dublin-Core-Metadatenstandard* wurde entwickelt, um Interoperabilität im Kontext des Semantic Web und vernetzter Daten (Linked Data) zu ermöglichen. 

Anders gesagt: Dublin Core verwendet spezielle Web-Adressen, sogenannte URIs (Uniform Resource Identifiers) um deutlich zu machen, worauf sich die Metadaten beziehen  – sowohl für die Objekte, die in den Metadaten beschrieben werden, als auch für die Begriffe, die in den genutzten Vokabularen vorkommen. Eine besondere Stärke von Dublin Core ist das sogenannte <a href="https://www.dublincore.org/resources/glossary/application_profile/" class="external-link" target="_blank">Anwendungsprofil</a> (Application Profile, AP). Es beschreibt, wie die grundlegenden Prinzipien und Begriffe von Dublin Core angepasst oder mit spezialisierten Vokabularen kombiniert werden können, um den spezifischen Anforderungen einzelner Projekte oder Anwendungsfälle gerecht zu werden {cite}`DCMI_Metadata_Basics`.

````{margin}
```{admonition} Hinweis
:class: hinweis
Dublin Core ist domänenunabhängig. Es wird nicht nur im bibliothekarischen Umfeld genutzt, sondern auch in Archiven, Museen, im E-Government, bei wissenschaftlichen Dateninfrastrukturen, im Verlagswesen und auch im Bildungsbereich. Diese Vielseitigkeit beruht auf dem bewusst generisch gehaltenen Vokabular. Die Weiterentwicklung des Standards erfolgt durch die <a href="https://www.dublincore.org/about/" target="_blank">Dublin Core Metadata Initiative</a> (DCMI), die Community-Prozesse pflegt und regelmäßig Konferenzen und Arbeitsgruppen organisiert. Der offene, partizipative Charakter dieser Organisation trägt zur Nachhaltigkeit und Aktualität des Standards bei.
```
````

Im Grunde genommen beinhaltet Dublin Core Informationen über 15 breit verwendete Elemente – Urheber:in, Mitwirkende, Herausgeber:in, Titel, Datum, Sprache, Format, Thema, Beschreibung, Identifier, Bezug, Quelle, Typ, Abdeckung und Rechte. Dieses Set wurde zum ersten Mal auf einem Treffen im Jahr 1995 in <a href="https://de.wikipedia.org/wiki/Dublin_(Ohio)" class="external-link" target="_blank">Dublin, Ohio</a> definiert {cite}`DublinCore`. Mainstream-Entwickler haben Vokabulare wie Dublin Core verwendet und nutzen sie weiterhin im Kontext von relationalen Datenbanken und Repositorien, von denen viele auf <a href="https://de.wikipedia.org/wiki/Extensible_Markup_Language" class="external-link" target="_blank">Extensible Markup Language</a> (XML) basieren – einer erweiterbaren Auszeichnungssprache zur Festlegung der Inhalte von Metadatensätzen als strukturierte Dokumente. Darüber hinaus wird die intuitive Bündelung von Beschreibungen in Sets ermöglicht. Dublin-Core-konforme Kategorien können durch die Wiederverwendung bestehender Elemente oder die Definition neuer Begriffe innerhalb einer Anwendung erweitert werden (durch Application Profiles). Beispielsweise kann ein Buch durch die Kategorie „Titel“ beschrieben werden, während ein Autor durch „Name“ und „Geburtsjahr“ charakterisiert wird. Beschreibungen mehrerer Ressourcen, wie „Buch“ oder „Autor“, können in einem Beschreibungsset zusammengefasst werden, das entweder direkt als RDF-Graph gespeichert oder in einem Format codiert wird, das in RDF umgewandelt werden kann.  Ein gut gestaltetes Anwendungsprofil basiert auf verfügbaren RDF-Vokabularen, klar definierten Entitätsmodellen und explizit formulierten funktionalen Anforderungen. Die Konsolidierung des Dublin Core als Standard ist eine graduelle Entwicklung, die sich über einen Zeitraum von 20 Jahren erstreckt hat {cite}`arakaki2018dublin`. 

Zusammenfassend lässt sich sagen, dass der Dublin Core als Schlüssel für die Erstellung von Metadaten und die Unterstützung bei der Gestaltung von Abfragen dient, um diese effektiv auffindbar zu machen. Für diese Abfragen wird eine spezifische Abfragesprache verwendet – ein Thema, mit dem wir uns im [Kapitel 5 - Praxis anwenden: SPARQL](sparql) befassen werden.

````{margin}
```{admonition} Hinweis
:class: hinweis
Ein wesentlicher Vorteil des Dublin Core-Standards ist seine Modularität. Obwohl der Kernstandard nur <a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/" class="external-link" target="_blank">15 Elemente</a> definiert („Simple Dublin Core“), lässt er sich durch zusätzliche Qualifikatoren erweitern (DC Terms) – dies bezeichnet man als „Qualified Dublin Core“. Damit lassen sich präzisere Beschreibungen erzeugen, die dennoch interoperabel bleiben.
```
````

## DCAT und Dublin Core

Mit dem Wissen über Dublin Core betrachten wir nun das <a href="https://www.w3.org/TR/vocab-dcat-3/" class="external-link" target="_blank">Data Catalog Vocabulary</a> (DCAT). DCAT ist ein RDF-Vokabular, das auf dem Dublin-Core-Benennungsschema basiert. Sein Zweck besteht darin, die Interoperabilität zwischen Datenkatalogen im Web zu ermöglichen. DCAT wurde im Kontext von staatlichen Datenkatalogen wie <a href="https://data.gov/" class="external-link" target="_blank">data.gov</a> und <a href="https://www.data.gov.uk/" class="external-link" target="_blank">data.gov.uk</a> entwickelt {cite}`W3C_DCAT_v3`. DCAT wird durch das <a href="https://www.w3.org/" class="external-link" target="_blank">World Wide Web Consortium</a> (W3C) verwaltet. Es ist daher ein vertrauenwürdiges und institutionalisiertes Projekt, das auf politischer Ebene unterstützt und als staatliche Initiative gefördert wird. Dazu gehören spezifische *Anwendungsprofile (AP)*, die in verschiedenen Ländern für Metadateninfrastrukturen entwickelt wurden.  
Dabei steht <a href="https://op.europa.eu/de/web/eu-vocabularies/dcat-ap" class="external-link" target="_blank">*DCAT-AP*</a> für *DCAT-Anwendungsprofil für Datenportale in Europa*. Von der Europäischen Union wird DCAT-AP definiert als "eine Spezifikation, die auf dem Datenkatalog-Vokabular (DCAT) basiert und zur Beschreibung von Datensätzen des öffentlichen Sektors in Europa dient" {cite}`EU_DCAT`. Die Zusammenhänge zwischen Dublin Core, DCAT, DCAT-AP und DCAT-AP.de werden durch die Abb. 3.5 veranschaulicht.


```{figure} /assets/standardisierungsrahmen-dcat-ap-de.png
---
name: Standardisierungsrahmen
alt: Eine grafische Darstellung von DCAT-AP.de und den Zusammenhängen mit Dublin Core und anderen Standards.
---
Darstellung "Standardisierungsrahmen DCAT-AP.de" unter der Lizenz <a href="https://creativecommons.org/publicdomain/zero/1.0/deed.de" class="external-link" target="_blank">CC 0</a> via <a href="https://www.dcat-ap.de/def/dcatde/3.0/spec/" class="external-link" target="_blank">DCAT-AP.de Spezifikation 3.0</a>.
```


In Deutschland nutzen verschiedene staatliche Datenportale wie <a href="https://www.govdata.de/" class="external-link" target="_blank">GovData</a> und die Datenportale der Bundesländer (z. B. das <a href="https://transparenz.hamburg.de/" class="external-link" target="_blank">Transparenzportal Hamburg</a>) DCAT-AP.de zur Standardisierung von Metadaten. Dies ermöglicht eine konsistente Katalogisierung von Daten und vereinfacht die Datenveröffentlichung und -nutzung, sowohl innerhalb der öffentlichen Verwaltung als auch für Bürger:innen.

Durch die Anlehnung an den <a href="https://op.europa.eu/de/web/eu-vocabularies/dcat-ap" class="external-link" target="_blank">europäischen DCAT-AP-Standard</a> ermöglicht DCAT-AP.de eine reibungslose Zusammenarbeit und Datenintegration mit dem Europäischen Datenportal. Deutsche Datensätze, die mit DCAT-AP.de beschrieben sind, lassen sich so problemlos auf das Europäische Datenportal übertragen, was eine einheitliche und grenzübergreifende Datennutzung innerhalb der EU fördert {cite}`FITKO_DCAT_AP`.

```{admonition} Was  Sie mitnehmen sollten
:class: keypoint 
Das DCAT-AP-Schema basiert auf dem Dublin-Core-Metadatenstandard und ermöglicht die Interoperabilität von Datenkatalogen im Web. Durch die Anwendung von DCAT-AP, insbesondere in nationalen Initiativen wie DCAT-AP.de in Deutschland, wird eine effiziente und einheitliche Katalogisierung und Nutzung von offenen Daten gefördert, die grenzübergreifend in der EU genutzt werden können.
```

**Literatur**

```{bibliography}
:filter: docname in docnames
```

