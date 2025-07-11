(intro)=
# Erfragen von Metadaten: Ein Fallbeispiel aus dem Europäischen und Deutschen Metadatenportal

Dieses <a href="https://jupyterbook.org/en/stable/intro.html" class="external-link" target="_blank">JupyterBook</a> vermittelt grundlegende Kenntnisse zur Datenabfrage, indem es relevante Datenportale vorstellt, über die Daten akquiriert werden können und Sie mit Metadaten, deren Qualität, Standards und Abfragesprachen vertraut macht.  
Der thematische Fokus liegt auf der Arbeit mit Baumkatasterdaten, da Daten zu Baumverteilungen vor allem im Zuge des Klimawandels zunehmend an Bedeutung gewinnen. Dies zeigen Portale wie <a href="https://www.giessdenkiez.de/map?treeAgeMax=200&lat=52.461091286002215&lng=13.436155588938107&zoom=17.756600613085226&treeId=00008100%3A000bc7ab" class="external-link" target="_blank">Gieß den Kiez</a>, von denen wir uns zu dieser Fallstudie inspirieren lassen haben.


```{figure} Datenwissenschaftler_analysiert_Baumverteilungen.png
---
name: Datenwissenschaftler analysiert Baumverteilungen
alt: Eine grafische Darstellung eines Datenwissenschaftlers der die Baumverteilung analysiert.
---
Datenwissenschaftler analysiert Baumverteilungen (KI generiert).
```

## Baumbestand-Analyse: Erfassung und Visualisierung der Verteilung der Baumarten

Der Baumbestand in Städten und ländlichen Regionen ist für Stadtplanung und Umweltforschung aufgrund deren Auswirkung auf das Mikroklima von zentraler Bedeutung. In diesem Zusammenhang stellen Baumkataster eine wichtige Arbeitsgrundlage dar, da sie Informationen zu Baumarten, deren Standort und Zustand liefern. Doch wie gut sind diese Daten öffentlich zugänglich?

Dr. Amir Weber, ein Experte mit Interesse an städtischen und ländlichen Baumbeständen, möchte ein Dashboard zur Visualisierung der Baumartenvielfalt erstellen, das auf offenen Datensätzen basiert. Dazu stellt sich Dr. Weber zunächst die folgende Frage:

**Wie lassen sich offene Daten ermitteln, die dazu beitragen können, den Baumbestand in einer bestimmten Region zu ermitteln?**   

Um diese Frage zu beantworten, vermittelt dieses JupyterBook Kenntnisse zu wichtigen Konzepten wie Semantic Web und Linked Data sowie Metadatenstandards und -qualität. Darüber hinaus erwartet Sie eine Einführung in die Benutzung der Abfragesprache SPARQL.  

## Bedeutung dieses Lehrbuchs für die Verwaltungswissenschaft

Die Auffindbarkeit von Daten wird durch Metadaten wesentlich vereinfacht, wenn nicht erst ermöglicht. Ein grundlegendes Verständnis von Metadaten ist daher von entscheidender Relevanz für die Arbeit mit Daten. In Bezug zur Verwaltung(swissenschaft) gilt dies insbesondere für <a href="https://www.dcat-ap.de/" class="external-link" target="_blank">DCAT-AP</a> - den gemeinsamen Metadatenstandard für offene Verwaltungsdaten. Des Weiteren lassen sich durch Abfragesprachen wie SPARQL passgenaue Informationen herausfiltern, was die Suche nach Datensätzen erleichtern kann.

## Zielgruppe

Grundsätzlich steht das JupyterBook allen Interessierten offen.

Die explizite Zielgruppe sind jedoch promovierende und promovierte Wissenschaftler:innen sowie Lehrende aus der Verwaltungswissenschaft, da die hier vermittelten Inhalte anhand des häufig untersuchten Datentyps *Tabelle* aufbereitet sind. Zudem orientieren sich die hier entwickelten Lerneinheiten an einem für diese Disziplin typischen Fallbeispiel.


## Struktur der Fallstudie

Die zentrale Forschungsfrage, die in dieser Fallstudie untersucht wird, lautet: 

**Welche offenen Daten gibt es, die dazu beitragen, den Bewässerungsbedarf von Bäumen in einer bestimmten Region zu ermitteln?**

Basierend auf den verfügbaren offenen Datenquellen werden Abfragen mithilfe der Abfragesprache SPARQL entwickelt, um relevante Informationen zu extrahieren. Dabei wird die Nachnutzbarkeit der Daten untersucht, ihre Qualität bewertet sowie der Entstehungskontext nachvollzogen. Die Abfragen ermöglichen eine strukturierte Analyse der Daten, um spezifische Antworten zum Baumbestand zu erhalten.

Die Nutzung und erste Schritte mit SPARQL werden in dieser Fallstudie anschaulich erläutert.  


```{figure} FS-Schritte.png
---
name: steps of casestudy
alt: Skizzenhafte Darstellung der 4 Schritte dieser Fallstudie.
---
Visualisierung der 4 Schritte dieser Fallstudie.
```


**1. Technologien verstehen** 

Wir greifen in dieser Fallstudie auf Metadaten aus dem europäischen Metadatenportal <a href="https://data.europa.eu/en" class="external-link" target="_blank">data.europa</a> zurück. Daher werden zuerst die grundlegenden Technologien erläutert, die gängige Metadatenschemata ausmachen, nämlich Semantic Web & Linked Data.

**2. Werkzeuge kennenlernen**

Wir machen Sie mit einem der zentralen Werkzeuge für die Operationalisierung von Metadatenrepositorien vertraut: dem DCAT-AP-Standard, der auch die politisch-administrativen Aspekte im Kontext von öffentlicher Verwaltung und Open Data einbezieht. In dieser Fallstudie werden außerdem die Nutzung der Abfragesprache SPARQL und erste praktische Schritte anschaulich erklärt.

**3. Datenqualität messen:** 

Sie lernen, wie Sie Metadaten anhand von Maßnahmen zur Qualitätsmessung überprüfen können, um sicherzustellen, dass diese den Qualitätsanforderungen entsprechen. Dazu stellen wir Ihnen die verschiedenen Qualitätskriterien des Metadata Quality Assessment (MQA) für Metadaten vor.

**4. Praxis anwenden**
Im letzten Schritt der Fallstudie widmen wir uns der praktischen Anwendung und erläutern, wie Metadaten mithilfe der SPARQL-Abfragesprache abgefragt werden können. Dabei vermitteln wir zunächst die grundlegenden Konzepte von SPARQL, einschließlich der Syntax und zentraler Befehle. Im Anschluss führen wir gezielte Abfragen durch, die auf unsere Fragestellung ausgerichtet sind und evaluieren kritisch, in welchem Maß die aktuellen Implementierungen erfolgreich sind oder Optimierungspotenzial aufweisen.  

---
  

Die Gliederung der Fallstudie in Kapitel und Abschnitte können Sie immer in der Menüleiste auf der linken Seite nachvollziehen. Die rechte Menüleiste zeigt Ihnen an, in welchem Abschnitt eines Kapitels Sie sich gerade befinden.
Die einzelnen Kapitel sind so gestaltet, dass Sie sie sowohl chronologisch als auch separat voneinander durchgehen können.

Das JupyterBook lässt sich in zwei Hauptblöcke gliedern:


|       Block              |     Inhalte                                               |    Bearbeitungszeit              |  
|---------------------|----------------------------------------------------|----------------------------------------------------|
| **Block 1**           | Kapitel 2, 3, 4: Grundlagen des Semantic Web, Metadatenstandards und Metadatenqualität | ca. 3 x 15 Min pro Kapitel  |  
| **Block 2**| Kapitel 5: Praktische Anwendung von SPARQL: Abfrage von Daten zur Beantwortung der Forschungsfrage                                                     | 45 Min|
