# Erfragen von Metadaten: Ein Fallbeispiel aus dem Europäischen und Deutschen Metadatenportal  
Um mit Daten arbeiten zu können, müssen diese auffindbar sein. Dieses <a href="https://jupyterbook.org/en/stable/intro.html" class="external-link" target="_blank">JupyterBook</a> vermittelt grundlegende Kenntnisse zur Datenabfrage, indem es relevante Datenportale vorstellt, über die Daten akquiriert werden können und Sie mit Metadaten, Standards und Abfragesprachen vertraut macht. 


```{figure} Datenwissenschaftler_analysiert_Baumverteilungen.png
---
name: Datenwissenschaftler analysiert Baumverteilungen
alt: Eine grafische Darstellung eines Datenwissenschaftlers der die Baumverteilung analysiert.
---
Datenwissenschaftler analysiert Baumverteilungen (KI generiert).
```

## Forschungsfrage - Baumbestand-Analyse: Erfassung und Visualisierung der Baumartenverteilung
Der Baumbestand in deutschen Städten und ländlichen Regionen ist für Klimaanpassung, Umweltforschung und Stadtplanung von zentraler Bedeutung. Eine wichtige Grundlage für diese Arbeiten sind detaillierte Baumkataster, die Informationen zu Baumarten, Standorten und Zustand liefern. Doch wie gut sind diese Daten öffentlich zugänglich?

Dr. Armir Weber, ein Wissenschaftler mit Interesse an städtischen und ländlichen Baumbeständen, möchte ein Dashboard zur Visualisierung der Baumartenvielfalt für die Jahre 2022–2024 entwickeln, das auf offenen Datensätzen basiert. Dazu stellt sich Dr. Weber die folgende Frage:

**- Wie unterscheidet sich das Angebot an offenen Baumkataster-Daten in den deutschen Bundesländern im Zeitraum 2022 – 2024 hinsichtlich Anzahl, Bereitsteller und Veröffentlichungsaktivität?** 

Die Hauptfrage lässt sich also in mehrere Teilfragen untergliedern, die eine detaillierte Analyse der offenen Baumkataster-Daten ermöglichen. Diese Unterfragen fokussieren sich auf verschiedene Aspekte der Datensätze: die Gesamtzahl der Datensätze bundesweit, die Verteilung der Daten auf die einzelnen Bundesländer sowie die Unterschiede in der Zahl der Datenbereitsteller und der Vielfalt der bereitgestellten Formate in den jeweiligen Regionen.

- Wie viele Datensätze gibt es bundesweit im Zeitraum 2022–2024, die das Wort „Baumkataster“ im Titel beinhalten?
- Wie viele Datensätze gibt es pro Bundesland im Zeitraum 2022–2024, die das Wort „Baumkataster“ im Titel beinhalten?
- Wie unterscheiden sich die Bundesländer in ihrer Anzahl an Datenbereitstellern? Wie variiert die Zahl der bereitgestellten Datensätze und Formate je Bundesland?

Diese Fragen sind der Ausgangspunkt für eine tiefere Untersuchung der verfügbaren offenen Daten. Dr. Weber plant, die Datensätze nach Bundesländern und Bereitstellern zu filtern, um ein besseres Verständnis darüber zu gewinnen, welche Regionen besonders viele und vielfältige Baumkataster-Daten zur Verfügung stellen. Recherchiere mit ihm zusammen, wie die Datengrundlage ist. 
Um die Fragen zu beantworten, vermittelt dieses JupyterBook Kenntnisse zu wichtigen Konzepten wie Semantic Web, sowie Metadatenstandards und -qualität. Darüber hinaus erwartet Sie eine Einführung in die Benutzung der Abfragesprache *SPARQL*.  

## Bedeutung dieses Lehrbuchs für die Verwaltungswissenschaft
Die Auffindbarkeit von Daten wird durch Metadaten wesentlich vereinfacht. Ein grundlegendes Verständnis von Metadaten ist daher von entscheidender Relevanz. Dies gilt insbesondere für <a href="https://www.dcat-ap.de/" target="_blank">DCAT-AP</a> als gemeinsamer Metadatenstandard für offene Verwaltungsdaten. Des Weiteren lassen sich durch Abfragesprachen wie SPARQL passgenaue Informationen herausfiltern, was die Suche nach Datensätzen fundamental erleichtern kann.

## Zielgruppe
**Für wen ist dieses JupyterBook gedacht?**

Dieses Selbstlernangebot richtet sich vorwiegend an Verwaltungswissenschaftler:innen und alle Personen, die an digitaler Verwaltung interessiert sind, da die hier vermittelten Inhalte anhand des häufig eingesetzten Datentyps *Tabelle* aufbereitet sind. Zudem orientieren sich die hier entwickelten Lerneinheiten an einem Fallbeispiel, das für diese Disziplin typisch ist.

Die Zielgruppe sind promovierende und promovierte Wissenschaftler:innen, aber auch Lehrende, die das Angebot für die eigene Lehre nachnutzen wollen.

Grundsätzlich steht das JupyterBook aber selbstverständlich allen Interessierten offen.

**Welche Voraussetzungen sind zur Absolvierung der Lerneinheiten erforderlich?**

Dieses JupyterBook erfordert ein allgemeines Verständnis darüber, wie Datensätze strukturiert sind, einschließlich grundlegender Begriffe wie Datensätze oder Variablen. Zudem sollten Anwendende mit Konzepten wie Metadaten und Datendokumentationen vertraut sein.

Für die Kapitel 2. *Semantic Web & Linked Data*, 3. *DCAT-AP Metadatenstandard* sowie 4. *Metadatenqualität* werden darüber hinaus keine Vorkenntnisse benötigt. Sie wurden für ein Einstiegslevel konzipiert und geben einen grundlegenden Einblick in die theoretischen Konzepte.

Für das Kapitel 5. *SPARQL* ist ein Grundinteresse bzw. -verständnis für Abfragengestaltung und Erfragen von Metadaten hilfreich, da Sie dort mit der Abfragesprache SPARQL arbeiten werden. Grundlegende Kenntnisse diesbezüglich sind für dieses Kapitel von Vorteil, aber keine Voraussetzung, da alle Aspekte ausführlich erläutert werden.

Die einzelnen Kapitel sind so gestaltet, dass Sie sie sowohl chronologisch als auch separat voneinander durchgehen können.

## Struktur der Fallstudie
Die zentrale Forschungsfrage, die in dieser Fallstudie untersucht wird, lautet: 

**Welche offenen Daten gibt es, die dazu beitragen, den Bewässerungsbedarf von Bäumen in einer bestimmten Region zu ermitteln?**

Basierend auf den verfügbaren offenen Datenquellen werden Abfragen mithilfe der Abfragesprache SPARQL entwickelt, um relevante Informationen zu extrahieren. Dabei wird die Nachnutzbarkeit der Daten untersucht, ihre Qualität bewertet sowie der Entstehungskontext nachvollzogen. Die Abfragen ermöglichen eine strukturierte Analyse der Daten, um spezifische Antworten zur Bewässerung zu erhalten.

Die Nutzung und erste Schritte mit SPARQL werden in dieser Fallstudie anschaulich erläutert.


**1. Technologien verstehen** 

Um die Forschungsfrage zu beantworten, benötigen wir Daten. Diese können und wollen wir nicht selbst erheben, weshalb wir Daten nachnutzen müssen. Wir greifen in dieser Fallstudie auf Metadaten aus dem europäischen Metadatenportal <a href="https://data.europa.eu/en" target="_blank">data.europa</a> zurück. Daher werden zuerst die grundlegenden Technologien erläutert, die gängige Metadatenschemata ausmachen, nämlich Semantic Web & Linked Data.

**2. Werkzeuge kennenlernen**

Wir machen Sie mit einem der zentralen Werkzeuge für die Operationalisierung von Metadatenrepositorien vertraut: dem DCAT-AP-Standardisierungsschema, das auch die politisch-administrativen Aspekte im Kontext von öffentlicher Verwaltung und Open Data einbezieht. In dieser Fallstudie werden außerdem die Nutzung der Abfragesprache SPARQL und erste praktische Schritte anschaulich erklärt.

**3. Datenqualität messen:** 

Sie lernen, wie Sie Metadaten anhand von Maßnahmen zur Qualitätsmessung überprüfen können, um sicherzustellen, dass diese den Qualitätsanforderungen entsprechen. Dazu stellen wir Ihnen die verschiedenen Qualitätskriterien des Metadata Quality Assessment (MQA) für Metadaten vor.

**4. Praxis anwenden**
Im letzten Schritt der Fallstudie widmen wir uns der praktischen Anwendung und erläutern, wie Metadaten mithilfe der SPARQL-Abfragesprache abgefragt werden können. Dabei vermitteln wir zunächst die grundlegenden Konzepte von SPARQL, einschließlich der Syntax und zentraler Befehle. Im Anschluss führen wir gezielte Abfragen durch, die auf unsere Fragestellung ausgerichtet sind und evaluieren kritisch, in welchem Maß die aktuellen Implementierungen erfolgreich sind oder Optimierungspotenzial aufweisen.


**Struktur der Fallstudie**

Die Gliederung der Fallstudie in Kapitel und Abschnitte können Sie immer in der Menüleiste auf der linken Seite nachvollziehen. Die rechte Menüleiste zeigt Ihnen an, in welchem Abschnitt eines Kapitels Sie sich gerade befinden.
Das JupyterBook lässt sich in zwei Hauptblöcke gliedern:




|       Block              |     Inhalte                                               |    Bearbeitungszeit              |  
|---------------------|----------------------------------------------------|----------------------------------------------------|
| **Block 1**           | Kapitel 2, 3, 4: Grundlagen des Semantic Web, Metadatenstandards und Metadatenqualität | ca. 3 x 15 Min pro Kapitel  |  
| **Block 2**| Kapitel 5: Praktische Anwendung von SPARQL: Abfrage von Daten zur Beantwortung der Forschungsfrage                                                     | 45 Min|
