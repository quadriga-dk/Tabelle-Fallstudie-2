# Erfragen von Metadaten: Ein Fallbeispiel aus dem Europäischen und Deutschen Metadatenportal  
Um mit Daten arbeiten zu können, müssen diese auffindbar sein. Dieses JupyterBook vermittelt grundlegende Kenntnisse zur Datenabfrage, indem es relevante Datenportale vorstellt, über die Daten akquiriert werden können und Sie mit Metadaten, Standards und Abfragesprachen vertraut macht. 

## Forschungsfrage - Baumbestand-Analyse: Erfassung und Visualisierung der Baumartenverteilung
Der Baumbestand in deutschen Städten und ländlichen Regionen ist für Klimaanpassung, Umweltforschung und Stadtplanung von zentraler Bedeutung. Eine wichtige Grundlage für diese Arbeiten sind detaillierte Baumkataster, die Informationen zu Baumarten, Standorten und Zustand liefern. Doch wie gut sind diese Daten für die Jahre 2022–2024 zugänglich?

Dr. Armir Weber, ein Wissenschaftler mit Interesse an städtischen und ländlichen Baumbeständen, möchte ein Dashboard zur Visualisierung der Baumartenvielfalt entwickeln, das auf offenen, öffentlichen Datensätzen basiert. Dazu stellt sich Dr. Weber die folgende Frage:

**- Wie unterscheidet sich das Angebot an offenen Baumkataster-Daten in den deutschen Bundesländern im Zeitraum 2022 – 2024 hinsichtlich Anzahl, Bereitsteller und Veröffentlichungsaktivität?** 

Die Hauptfrage lässt sich also in mehrere Teilfragen untergliedern, die eine detaillierte Analyse der offenen Baumkataster-Daten ermöglichen. Diese Unterfragen fokussieren sich auf verschiedene Aspekte der Datensätze: die Gesamtzahl der Datensätze bundesweit, die Verteilung der Daten auf die einzelnen Bundesländer sowie die Unterschiede in der Zahl der Datenbereitsteller und der Vielfalt der bereitgestellten Formate in den jeweiligen Regionen.

- Wie viele Datensätze gibt es bundesweit im Zeitraum 2022–2024, die das Wort „Baumkataster“ im Titel beinhalten?
- Wie viele Datensätze gibt es pro Bundesland, die das Wort „Baumkataster“ im Titel beinhalten?
- Wie unterscheiden sich die Bundesländer in ihrer Anzahl an Datenbereitstellern? Wie variiert die Zahl der bereitgestellten Datensätze und Formate je Bundesland?

Diese Fragen sind der Ausgangspunkt für eine tiefere Untersuchung der verfügbaren offenen Daten. Dr. Weber plant, die Datensätze nach Bundesländern und Bereitstellern zu filtern, um ein besseres Verständnis darüber zu gewinnen, welche Regionen besonders viele und vielfältige Baumkataster-Daten zur Verfügung stellen. 
Um die Fragen zu beantworten, vermittelt dieses JupyterBook Kenntnisse zu wichtigen Konzepten wie Semantic Web, sowie Metadatenstandards und -qualität. Darüber hinaus erwartet Sie eine Einführung in die Benutzung der Abfragesprache *SPARQL*.  

## Bedeutung des JupyterBooks für die Verwaltungswissenschaft
Die Auffindbarkeit von Daten wird durch Metadaten wesentlich vereinfacht. Ein grundlegendes Verständnis von Metadaten ist daher von entscheidender Relevanz. Dies gilt insbesondere für <a href="https://www.dcat-ap.de/" target="_blank">DCAT-AP</a> als gemeinsamer Metadatenstandard für offene Verwaltungsdaten. Des Weiteren lassen sich durch Abfragesprachen wie SPARQL passgenaue Informationen herausfiltern, was die Suche nach Datensätzen fundamental erleichtern kann.


## Lernziele bzw. zu erwerbende Kompetenzen
Sie müssen dieses JupyterBook nicht am Stück durchgehen, sondern können es auch Kapitel für Kapitel absolvieren. Dabei werden Sie folgende Lernziele erreichen:

```{admonition} Grundlegende Konzepte und Datenidentifikation
:class: lernziele
- Die Lernenden sind vertraut mit semantischen Technologien und Linked Data.
- Die Lernenden verstehen, dass Open Data Portale auf semantischen Technologien basieren und kennen die Linked Data Grundprinzipien, die hier angewendet werden.
```

```{admonition} Datenerschließung und Metadaten
:class: lernziele
- Die Lernenden haben sich mit dem Zweck von Metadatastandards befasst und kennen die Struktur von DCAT-AP.
```

```{admonition} Metadatenqualität
:class: lernziele
- Die Lernenden erkennen, dass die FAIR-Prinzipien ein Grundgerüst zur Messung von Metadatenqualität sind.
- Die Lernenden sind mit einem Messverfahren zur Metadatenqualität im europäischen Datenportal vertraut.
- Die Lernenden sind in der Lage, Prüfberichte zu bewerten und sich mit typischen Problemen der Metadatenqualität auseinanderzusetzen.
```

```{admonition} Abfragesprachen
:class: lernziele
- Die Lernenden können maschinelle Abfragen von Daten in Open Data Portalen unter Anwendung von SPARQL verfassen.
- Die Lernenden sind in der Lage, verschiedene SPARQL-Techniken über die API von data.europa anzuwenden.
```
