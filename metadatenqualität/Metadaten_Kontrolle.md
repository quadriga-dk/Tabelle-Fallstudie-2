# Kontrolle und Werkzeuge
Es ist zunächst sinnvoll, sich mit dem Konzept der Metadaten vertraut zu machen, bevor wir uns mit deren Abfrage beschäftigen. Die einfachste Definition von Metadaten lautet: „Daten über Daten“ – also Informationen, die dazu dienen, Datensätze einzuordnen und zu kategorisieren, damit diese leichter auffindbar und übersichtlich bleiben. Verschiedene Arten von Metadaten erfüllen unterschiedliche Funktionen {cite}`riley2017understanding`. So enthalten zum Beispiel beschreibende Metadaten für ein Dokument Informationen wie den Autor, das Erstellungsdatum, die Dateigröße und Schlagwörter. Technische Metadaten für eine relationale Datenbank könnten dagegen die Struktur der Tabellen, Datentypen und Beziehungen zwischen den Tabellen beschreiben.

Das Bundesministerium des Innern und für Heimat hat 2018 über sein Online-Angebot "Verwaltung innovativ" einen <a href="https://www.verwaltung-innovativ.de/SharedDocs/Publikationen/eGovernment/open_data_leitfaden.html" class="external-link" target="_blank">"Leitfaden Metadaten"</a> veröffentlicht, der eine gute Einführung in die Thematik bietet. 

Aufgrund der enormen Datenmengen, die heutzutage verarbeitet werden, sind Metadaten unverzichtbar. Sie ermöglichen einen verbesserten Datenzugriff und vereinfachen die Navigation durch umfangreiche Datensätze, wodurch Rohdaten in wertvolle Erkenntnisse umgewandelt werden können.
Ein Einzelhandelsunternehmen könnte beispielsweise Metadaten nutzen, um Verkaufsdaten für einen bestimmten Monat, gefiltert nach Produktkategorie und Region, schnell zu finden, ohne das gesamte Datenvolumen durchsuchen zu müssen {cite}`duval2002metadata`. Metadaten sind auch somit entscheidend für die Datenverwaltung und das Datenmanagement.

Metadaten sollten, wie die Daten, die sie beschreiben, auffindbar, zugänglich, interoperabel (bzw. kompatibel) und wiederverwendbar sein. Sie sollten also entsprechend den <a href="https://www.go-fair.org/fair-principles/" class="external-link" target="_blank">FAIR-Prinzipien</a> ausgezeichnet sein. In einer weiteren unserer Lerneinheiten finden Sie eine <a href="https://quadriga-dk.github.io/Tabelle-Fallstudie-1/Markdown/3_1_FairPrinzipien.html" class="external-link" target="_blank">Einführung in die FAIR-Prinzipien</a>.

Die FAIR-Prinzipien dienen als Grundlage für das <a href="https://data.europa.eu/mqa/methodology?locale=de" class="external-link" target="_blank">Metadata Quality Assessment (MQA)</a>, ein vom Konsortium des europäischen Datenportals <a href="https://data.europa.eu/de" class="external-link" target="_blank">data.europa.eu</a> entwickeltes Tool zur Bewertung der Qualität der von data.europa.eu erhobenen Metadaten.

Das MQA zielt darauf ab, die Qualität der Metadaten für Daten des öffentlichen Sektors in Europa zu bewerten und die größten Hindernisse, die einer besseren Datenqualität entgegenstehen, zu identifizieren. Die Untersuchung konzentriert sich auf spezifische Fragestellungen, wie die Einhaltung von DCAT-AP-Standards, die Offenlegung zusätzlicher Informationen, die Zugänglichkeit und Maschinenlesbarkeit der referenzierten Daten sowie die Lizenzverwendung.

Auf dem <a href="https://data.europa.eu/mqa/?locale=de" class="external-link" target="_blank">Metadata Quality Dashboard</a> des europäischen Metadatenportals wird eine Bewertung aller europäischen Portale geboten und die besten 12 Portale hervorgehoben. Die Bewertung ist an die FAIR-Prinzipien angelehnt und erfolgt in den 5 Dimensionen Auffindbarkeit, Zugänglichkeit, Interoperabilität, Wiederverwendbarkeit und Kontext. 

```{figure} /_images/mqa_screenshot_20250703.png
---
align: left
width: 100%
name: Indikatoren der Dimensionen des Metadata Quality Assessment
alt: Darstellung der Indikatoren der Dimensionen des Metadata Quality Assessment.
---
Darstellung einzelner Indikatoren innerhalb der Dimensionen Auffindbarkeit und Zugänglichkeit.
```
Bildquelle: Screenshot der Indikatoren der Bewertungsdimensionen Auffindbarkeit und Zugänglichkeit des Metadata Quality Assessment, <a href="https://data.europa.eu/mqa/?locale=de" class="external-link" target="_blank">https://data.europa.eu/mqa/?locale=de</a>, Amt für Veröffentlichungen der Europäischen Union, 03.07.2025.


Die Prozentzahlen geben den Anteil der Datensätze an, die den jeweiligen Kriterien entsprechen. Durch den Verlauf kann man nachvollziehen, wie diese Anteile im Laufe der Jahre schwanken, insbesondere da kontinuierlich neue Datensätze hinzugefügt werden, die die Kriterien erfüllen oder nicht. Im Übersichtsbereich ist beispielsweise ersichtlich, dass das [nationale spanische Datenportal](https://data.europa.eu/mqa/catalogues/yoda/?locale=de) eine ausgezeichnete Bewertung erhalten hat (Stand März 2025). 
Lassen Sie uns nun das [Open Data Portal Deutschland](https://data.europa.eu/mqa/catalogues/govdata/?locale=de) betrachten und einschätzen, wie fortgeschritten die Open-Data-Initiative in Deutschland ist und welche Schwachstellen noch bestehen. In der folgenden Übung können Sie eigenständig die Seite durchstöbern und potenzielle Unzulänglichkeiten ausfindig machen.

```{admonition} Was  Sie mitnehmen sollten
:class: keypoint
Metadaten sind entscheidend, um Daten schnell und effizient zu organisieren, zu kategorisieren und auffindbar zu machen. Sie ermöglichen eine bessere Navigation durch große Datenmengen und tragen zur Umwandlung von Rohdaten in wertvolle Informationen bei. Die Anwendung der FAIR-Prinzipien für Metadaten stellt sicher, dass diese Daten zugänglich, interoperabel und wiederverwendbar sind, und wird durch Werkzeuge wie das Metadata Quality Assessment (MQA) zur Bewertung und Verbesserung der Metadatenqualität unterstützt.
```

**Literatur**

```{bibliography}
:filter: docname in docnames
```