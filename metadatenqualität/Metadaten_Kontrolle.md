# Metadaten und Werkzeuge zur Qualitätsbestimmung

<span style="color:red">*Der Titel "Kontrolle und Werkzeuge" erscheint mir nicht passend. Zudem ist es unsinnig, Grundlagenwissen zu Metadaten zu vermitteln oder nur zu wiederholen, wenn im vorherigen Kapitel bereits DCAT-AP thematisiert wurde. Habe es trotzdem drin gelassen, da sonst das ganze Kapitel keinen Sinn hat.*</span>

## Metadaten

Bevor wir uns mit der Abfrage von Metadaten beschäftigen, ist es sinnvoll, vorhandenes Wissen zu Metadaten zu rekapitulieren. 
Metadaten sind Informationen über Daten, die dazu dienen, diese einzuordnen und zu kategorisieren, damit sie u. a. leichter auffindbar sind.  
Es gibt verschiedene Arten von Metadaten, die unterschiedliche Funktionen erfüllen {cite}`riley2017understanding`. So enthalten zum Beispiel *beschreibende Metadaten* Informationen wie die Autor:innen, das Erstellungsdatum, die Dateigröße und Schlagwörter. *Technische Metadaten* (beispielsweise einer relationalen Datenbank) könnten dagegen die Struktur von Tabellen, Datentypen und Beziehungen zwischen den Tabellen beschreiben.

```{admonition} Weitere Informationen
:class: seealso
Das <a href="https://www.bva.bund.de/DE/Services/Behoerden/Beratung/OpenData/opendata_node.html" class="external-link" target="_blank">"Kompetenzzentrum Open Data"</a> (CCOD) des <a href="https://www.bva.bund.de/DE/Home/home_node.html" class="external-link" target="_blank">"Bundesverwaltungsamtes"</a> (BVA) hat 2023 eine 2. Version des <a href="https://www.bva.bund.de/SharedDocs/Downloads/DE/Behoerden/Beratung/Methoden/open_data_leitfaden_metadaten.pdf?__blob=publicationFile&v=2" class="external-link" target="_blank">"Leitfadens Metadaten"</a> veröffentlicht, der eine kurze Einführung in die Thematik mit Fokus auf den Auszeichnungsprozess beim deutschen Datenportal <a href="https://www.govdata.de/" class="external-link" target="_blank">"GovData"</a> bietet.
```

Metadaten sind unverzichtbar, um Daten zu finden. Das bedeutet im Umkehrschluss auch, dass Metadaten der Schlüssel sind, wenn es darum geht, eigene (Forschungs)Daten auffindbar zu veröffentlichen.
Sie ermöglichen einen verbesserten Datenzugriff und vereinfachen die Navigation durch umfangreiche Datensätze, wodurch Rohdaten in wertvolle Erkenntnisse umgewandelt werden können.
Ein Einzelhandelsunternehmen könnte beispielsweise Metadaten nutzen, um Verkaufsdaten für einen bestimmten Monat, gefiltert nach Produktkategorie und Region, schnell zu finden, ohne das gesamte Datenvolumen durchsuchen zu müssen {cite}`duval2002metadata`. Metadaten sind somit auch entscheidend für die Datenverwaltung und das Datenmanagement.

Metadaten sollten, wie die Daten, die sie beschreiben, auffindbar, zugänglich, interoperabel (bzw. kompatibel) und wiederverwendbar sein. Sie sollten also entsprechend den <a href="https://www.go-fair.org/fair-principles/" class="external-link" target="_blank">FAIR-Prinzipien</a> ausgezeichnet sein. In einer weiteren unserer Lerneinheiten finden Sie eine <a href="https://quadriga-dk.github.io/Tabelle-Fallstudie-1/Markdown/3_1_FairPrinzipien.html" class="external-link" target="_blank">Einführung in die FAIR-Prinzipien</a>.


```{admonition} Weitere Informationen
:class: seealso
Der Open Data Support der Europäischen Kommission hat ein <a href="https://data.europa.eu/sites/default/files/d2.1.2_training_module_2.2_open_data_quality_de_edp.pdf" class="external-link" target="_blank">Trainingsmodul</a> als Präsentation (pdf) zur Qualität von offenen Daten und Metadaten veröffentlicht. 

Die Qualität von Daten ist zudem Thema einer weiteren 
<a href="https://quadriga-dk.github.io/Tabelle-Fallstudie-1/Markdown/4_Qualit%C3%A4tsbewertung.html" class="external-link" target="_blank">Lerneinheit</a> des Projektes QUADRIGA.

Falls Sie noch nach einem grundsätzlichen Überblick zum Thema Metadaten suchen, sei Ihnen das 
<a href="https://wiki.dnb.de/download/attachments/43523047/201209_metadaten.pdf" class="external-link" target="_blank">Kleine Handbuch Metadaten</a> von Stefanie Rühle, Kompetenzzentrum Interoperable Metadaten, empfohlen.
```


## Überprüfen der Metadatenqualität

Die FAIR-Prinzipien dienen auch als Grundlage für das <a href="https://data.europa.eu/mqa/methodology?locale=de" class="external-link" target="_blank">Metadata Quality Assessment (MQA)</a>, ein vom Konsortium des europäischen Datenportals <a href="https://data.europa.eu/de" class="external-link" target="_blank">data.europa.eu</a> entwickeltes Tool zur Bewertung der Qualität der von data.europa.eu erhobenen Metadaten.

Das MQA zielt darauf ab, die Qualität der Metadaten für Daten des öffentlichen Sektors in Europa zu bewerten und die größten Hindernisse, die einer besseren Datenqualität entgegenstehen, zu identifizieren. Die Untersuchung konzentriert sich auf spezifische Fragestellungen, wie die Einhaltung von DCAT-AP-Standards, die Offenlegung zusätzlicher Informationen, die Zugänglichkeit und Maschinenlesbarkeit der referenzierten Daten sowie die Lizenzverwendung.

Die Bewertung ist an die FAIR-Prinzipien angelehnt und erfolgt in den fünf Dimensionen Auffindbarkeit, Zugänglichkeit, Interoperabilität, Wiederverwendbarkeit und Kontext. Dabei werden für einzelne Dimensionen verschiedene Indikatoren bewertet und Punkte vergeben. Die insgesamt erreichte Punktzahl entscheidet am Ende über die Bewertung in den vier Kategorien "Exzellent", "Gut", "Ausreichend" oder "Mangelhaft".  

```{figure} /assets/mqa_screenshot_20250703.png
---
align: left
width: 100%
name: Indikatoren der Dimensionen des Metadata Quality Assessment
alt: Darstellung der Indikatoren der Dimensionen des Metadata Quality Assessment.
---
Darstellung einzelner Indikatoren innerhalb der Dimensionen Auffindbarkeit und Zugänglichkeit.
```
Bildquelle: Screenshot der Indikatoren der Bewertungsdimensionen Auffindbarkeit und Zugänglichkeit des Metadata Quality Assessment, <a href="https://data.europa.eu/mqa/?locale=de" class="external-link" target="_blank">https://data.europa.eu/mqa/?locale=de</a>, Amt für Veröffentlichungen der Europäischen Union, Zugriff am 03.07.2025.


Durch den Verlauf kann man nachvollziehen, wie diese Anteile im Laufe der Jahre schwanken, insbesondere da kontinuierlich neue Datensätze hinzugefügt werden, die die Kriterien erfüllen oder nicht. Im Übersichtsbereich ist beispielsweise ersichtlich, dass das spanische Datenportal <a href="https://data.europa.eu/mqa/catalogues/yoda/?locale=de" class="external-link" target="_blank">Your Open DAta</a> auf data.europa.eu eine gute Bewertung erhalten hat, wobei in auffällig ist, dass die Auffindbarkeit 100% erhält, während die Zugänglichkeit voll oder fast gar nicht gegeben ist:

```{figure} /assets/2025-08-01_Screenshot_Portal_DataEuropa.png
---
name: Werte Spanisches Portal
alt: Darstellung der Auffindbarkeit und der Zugänglichkeit des spanischen Datenportals "Your Open DAta"
width: 512px
---
Darstellung der Auffindbarkeit und der Zugänglichkeit des spanischen Datenportals Your Open DAta.
```
Screenshot der Evalutaion des spanischen Datenportals Yor Open DAta, https://data.europa.eu/mqa/catalogues/yoda?locale=de, Amt für Veröffentlichungen der Europäischen Union, Zugriff am 01.08.2025. 

Auf dem <a href="https://data.europa.eu/mqa/?locale=de" class="external-link" target="_blank">Metadata Quality Dashboard</a> des europäischen Metadatenportals wird eine Bewertung aller europäischen Portale geboten und die besten 12 Portale hervorgehoben.


```{admonition} Was  Sie mitnehmen sollten
:class: keypoint
Metadaten erleichtern die Suche nach und die Verwendung von Daten. Sie ermöglichen eine bessere Navigation durch große Datenmengen und erleichtern die Nachnutzung. Die Anwendung der FAIR-Prinzipien auf die Metadaten stellt sicher, dass diese Daten auffindbar, zugänglich, interoperabel und wiederverwendbar sind, was durch Werkzeuge wie das Metadata Quality Assessment (MQA) überprüft werden kann.
```

**Literatur**

```{bibliography}
:filter: docname in docnames
```
