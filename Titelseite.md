---
lang: de-DE
---

(intro)=
# Offene Daten im urbanen Raum: Eine Einführung in die Datenabfrage mit SPARQL und Metadaten

`````{margin}
```{admonition} Fragen oder Feedback 
:class: frage-feedback

<a href="https://github.com/quadriga-dk/Tabelle-Fallstudie-2/issues/new?assignees=&labels=question&projects=&template=frage.yml" class="external-link" target="_blank">
    Stellen Sie eine Frage
</a> <br>
<a href="https://github.com/quadriga-dk/Tabelle-Fallstudie-2/issues/new?assignees=&labels=feedback&projects=&template=feedback.yml" class="external-link" target="_blank">
    Geben Sie uns Feedback
</a>

Mit Ihren Rückmeldungen können wir unser interaktives Lehrbuch gezielt an Ihre Bedürfnisse anpassen.

```
`````

`````{margin}
````{admonition} Zitierhinweis
:class: citation-information
```{literalinclude} /CITATION.bib
:language: bibtex
```
Plomin, J., Walter, P., Schmeling, J. & Dakruni, S. (2025). _Offene Daten im urbanen Raum: Eine Einführung in die Datenabfrage mit SPARQL und Metadaten. QUADRIGA Open Educational Resources: Tabelle 2_ 

````
`````

Dieses <a href="https://jupyterbook.org/en/stable/intro.html" class="external-link" target="_blank">JupyterBook</a> möchte Kenntnisse zur Datenabfrage vermitteln, indem es relevante Datenportale vorstellt, über die Daten akquiriert werden können und Sie mit Metadaten, deren Qualität, Standards und Abfragesprachen vertraut macht.

Der thematische Fokus liegt auf der Arbeit mit Baumkatasterdaten.  
Daten zu Baumverteilungen oder -pflanzungen in Städten gewinnen zunehmend an Bedeutung, da Bäume das Mikroklima wesentlich beeinflussen. Das gestiegene Interesse der Bevölkerung an "ihren" Stadtbäumen zeigen Portale wie <a href="https://www.giessdenkiez.de/map?treeAgeMax=200&lang=de&lat=52.494590307846366&lng=13.388836926491992" class="external-link" target="_blank">Gieß den Kiez</a>, von denen wir uns zu dieser Fallstudie inspirieren lassen haben.


```{figure} /assets/Datenwissenschaftler_analysiert_Baumverteilungen.png
---
name: Datenwissenschaftler analysiert Baumverteilungen
alt: Eine grafische Darstellung eines Datenwissenschaftlers der die Baumverteilung analysiert.
width: 420px
---
Datenwissenschaftler analysiert Baumverteilungen (KI generiert).
```

## Baumbestand-Analyse: Erfassung und Visualisierung der Verteilung der Baumarten

Daten zu Baumbeständen sind wegen des Klimawandels vor allem in Städten aufgrund deren Auswirkung auf das Mikroklima von zentraler Bedeutung. In diesem Zusammenhang stellen Baumkataster eine wichtige Arbeitsgrundlage dar, da sie Informationen zu Baumarten, deren Standort, Alter und Zustand liefern. Doch wie gut sind diese Daten öffentlich zugänglich?

`````{margin}
```{admonition} Hinweis 
:class: hinweis
Die Visualisierung von kommunalen Daten mit Dashboards ist Thema einer weiteren Fallstudie von Quadriga, die thematisch auf diese Fallstudie aufbaut: <a href="https://quadriga-dk.github.io/Tabelle-Fallstudie-3/intro.html" class="external-link" target="_blank">Fallstudie 3</a>.
```
`````

```{admonition} Story
:class: story
Dr. Amir Weber, ein Verwaltungswissenschaftler mit Interesse an kommunalen Daten und Bürgerbeteiligung, möchte ein <a href="https://quadriga-dk.github.io/Tabelle-Fallstudie-3/intro.html" class="external-link" target="_blank">Dashboard</a> zur Visualisierung von Baumbeständen erstellen, das auf offenen Datensätzen basiert. Dazu stellt sich Dr. Weber zunächst die folgende Frage:
```

**Wie lassen sich offene Daten ermitteln, die dazu beitragen können, den Baumbestand in einer bestimmten Region zu ermitteln?**   

Um diese Frage zu beantworten, vermittelt dieses JupyterBook Kenntnisse zu wichtigen Konzepten wie Semantic Web und Linked Data sowie Metadatenstandards und -qualität. Darüber hinaus erwartet Sie eine Einführung in die Benutzung der Abfragesprache SPARQL.  

## Bedeutung dieses Lehrbuchs für die Verwaltungswissenschaft

Die Auffindbarkeit von Daten wird durch Metadaten wesentlich vereinfacht, wenn nicht erst ermöglicht. Ein grundlegendes Verständnis von Metadaten ist daher von entscheidender Relevanz für die Arbeit mit Daten. In Bezug zur Verwaltung(swissenschaft) gilt dies insbesondere für <a href="https://www.dcat-ap.de/" class="external-link" target="_blank">DCAT-AP</a> - den gemeinsamen Metadatenstandard für offene Verwaltungsdaten. Des Weiteren lassen sich durch Abfragesprachen wie SPARQL passgenaue Informationen herausfiltern, was die Suche nach Datensätzen erleichtern kann.

## Zielgruppe

Dieses JupyterBook wurde für Verwaltungswissenschaftler:innen entworfen, da die Daten, die hier via SPARQL abgefragt werden, Daten aus der öffentlichen Verwaltung sind (Baumkatasterdaten).

Diese Daten können selbstverständlich auch in anderen wissenschaftlichen Kontexten oder für Laien von Bedeutung bzw. Interesse sein.


Dieses Lehrbuch steht somit allen Interessierten bzw. Forschenden offen, die wissen möchten, wie man Daten via SPARQL Daten sucht oder generell Interesse an der Funktionsweise von Abfragesprachen haben.


## Struktur der Fallstudie

Basierend auf den verfügbaren offenen Datenquellen werden Abfragen mithilfe der Abfragesprache SPARQL entwickelt, um relevante Informationen zu extrahieren. Dabei wird die Nachnutzbarkeit der Daten untersucht, ihre Qualität bewertet sowie der Entstehungskontext nachvollzogen. Die Abfragen ermöglichen eine strukturierte Analyse der Daten, um spezifische Antworten zum Baumbestand zu erhalten.

Die Nutzung und erste Schritte mit SPARQL werden in dieser Fallstudie anschaulich erläutert.  


```{figure} /assets/case-study-2_steps.png
---
name: steps of casestudy
alt: Skizzenhafte Darstellung der 4 Schritte dieser Fallstudie.
---
Visualisierung der 4 Schritte dieser Fallstudie.
```


**1. Technologien verstehen: Semantic Web & Linked Data** 

Wir greifen in dieser Fallstudie auf Metadaten aus dem europäischen Metadatenportal <a href="https://data.europa.eu/en" class="external-link" target="_blank">data.europa</a> zurück. Daher werden zuerst die grundlegenden Technologien erläutert, die gängige Metadatenschemata ausmachen, nämlich Semantic Web und Linked Data.

**2. Werkzeuge kennenlernen: DCAT-AP Metadatenstandard**

Wir machen Sie mit einem der zentralen Werkzeuge für die Operationalisierung von Metadatenrepositorien vertraut: dem DCAT-AP-Standard, der auch die politisch-administrativen Aspekte im Kontext von öffentlicher Verwaltung und Open Data einbezieht. 

**3. Datenqualität messen: Metadata Quality Assessment** 

Sie lernen, wie Sie Metadaten anhand von Maßnahmen zur Qualitätsmessung überprüfen können, um sicherzustellen, dass diese den Qualitätsanforderungen entsprechen. Dazu stellen wir Ihnen die verschiedenen Qualitätskriterien des Metadata Quality Assessment (MQA) für Metadaten vor.

**4. Praxis anwenden: SPARQL-Abfragen**

Im letzten Schritt der Fallstudie widmen wir uns der praktischen Anwendung und erläutern, wie Metadaten mithilfe der SPARQL-Abfragesprache abgefragt werden können. Dabei vermitteln wir zunächst die grundlegende Funktionsweise von SPARQL, einschließlich der Syntax und zentraler Befehle. Im Anschluss führen wir gezielte Abfragen durch, die auf unsere Fragestellung ausgerichtet sind und evaluieren kritisch, in welchem Maß die aktuellen Implementierungen erfolgreich sind oder Optimierungspotenzial aufweisen.  

---
  

Die Gliederung der Fallstudie in Kapitel und Unterkapitel können Sie immer in der Menüleiste auf der linken Seite nachvollziehen. Die rechte Menüleiste zeigt Ihnen an, in welchem Abschnitt eines Kapitels Sie sich gerade befinden.
Die einzelnen Kapitel sind so gestaltet, dass Sie sie sowohl nacheinander als auch separat voneinander durchgehen können.

Das JupyterBook lässt sich in zwei Hauptblöcke gliedern:


|       Block              |     Inhalte                                               |    Bearbeitungszeit              |  
|---------------------|----------------------------------------------------|----------------------------------------------------|
| **Block 1**           | Kapitel 2, 3, 4: Grundlagen des Semantic Web, Metadatenstandards und Metadatenqualität |  <span style="color:red">*ca. 3 x 20-30 Min pro Kapitel*</span> |  
| **Block 2**| Kapitel 5: Praktische Anwendung von SPARQL: Abfrage von Daten zur Beantwortung der Forschungsfrage                                                     | <span style="color:red">*45 Min*</span> |
