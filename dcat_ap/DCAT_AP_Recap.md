---
lang: de-DE
---

(recap)=
# Metadaten

Bevor wir uns mit der Abfrage von Metadaten bzw. Metadatenstandards beschäftigen, ist es sinnvoll, vorhandenes Wissen zu Metadaten zu rekapitulieren.  
Metadaten sind Informationen über Daten, die dazu dienen, diese zu beschreiben, einzuordnen und zu kategorisieren, damit sie u. a. verständlich und auffindbar werden.  

```{figure} /assets/512px-Schlagwortkatalog.jpg
---
name: Schlagwortkatalog
alt: Ein Schlagwortkatalog an der Universitätsbibliothek Graz
width: 512px
---
Karteikarten in einem Schlagwortkatalog, <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.de" class="external-link" target="_blank">CC BY-SA</a> <a href="https://commons.wikimedia.org/wiki/File:Schlagwortkatalog.jpg?uselang=de" class="external-link" target="_blank">Marcus Gossler</a>.
```

Es gibt verschiedene Arten von Metadaten, die unterschiedliche Funktionen erfüllen {cite}`riley2017understanding`. So enthalten zum Beispiel *beschreibende Metadaten* Informationen wie die Autor:innen, das Erstellungsdatum, die Dateigröße und Schlagwörter. *Technische Metadaten* (beispielsweise einer relationalen Datenbank) könnten dagegen die Struktur von Tabellen, Datentypen und Beziehungen zwischen den Tabellen beschreiben.


```{admonition} Weitere Informationen
:class: seealso
Das <a href="https://www.bva.bund.de/DE/Services/Behoerden/Beratung/OpenData/opendata_node.html" class="external-link" target="_blank">"Kompetenzzentrum Open Data"</a> (CCOD) des <a href="https://www.bva.bund.de/DE/Home/home_node.html" class="external-link" target="_blank">"Bundesverwaltungsamtes"</a> (BVA) hat 2023 eine 2. Version des <a href="https://www.bva.bund.de/SharedDocs/Downloads/DE/Behoerden/Beratung/Methoden/open_data_leitfaden_metadaten.pdf?__blob=publicationFile&v=2" class="external-link" target="_blank">"Leitfadens Metadaten"</a> veröffentlicht, der eine kurze Einführung in die Thematik mit Fokus auf den Auszeichnungsprozess beim deutschen Datenportal <a href="https://www.govdata.de/" class="external-link" target="_blank">"GovData"</a> bietet.
```

Metadaten sind unverzichtbar, um Daten zu finden. Das bedeutet im Umkehrschluss auch, dass Metadaten der Schlüssel sind, wenn es darum geht, eigene (Forschungs-)Daten oder Verwaltungsdaten auffindbar zu veröffentlichen.
Sie ermöglichen einen verbesserten Datenzugriff und vereinfachen die Navigation durch umfangreiche Datensätze.
Ein Einzelhandelsunternehmen könnte beispielsweise Metadaten nutzen, um Verkaufsdaten für einen bestimmten Monat, gefiltert nach Produktkategorie und Region, schnell zu finden, ohne das gesamte Datenvolumen durchsuchen zu müssen {cite}`duval2002metadata`. Gleiches gilt für Verwaltungs- oder statistische Daten: auch dort ermöglichen Metadaten eine gezielte Suche nach spezifischen Daten einer Kommune (zum Beispiel Baumkatasterdaten einer Stadt) zu einem konkreten Zeitpunkt. Aufgrund dieser Filterfunktion sind Metadaten auch entscheidend für die Datenverwaltung und das Datenmanagement.

Metadaten sollten, wie die Daten, die sie beschreiben, auffindbar, zugänglich, interoperabel (bzw. kompatibel) und wiederverwendbar sein. Sie sollten also entsprechend den <a href="https://www.go-fair.org/fair-principles/" class="external-link" target="_blank">FAIR-Prinzipien</a> ausgezeichnet sein. In einer weiteren unserer Lerneinheiten finden Sie eine <a href="https://quadriga-dk.github.io/Tabelle-Fallstudie-1/Markdown/3_1_FairPrinzipien.html" class="external-link" target="_blank">Einführung in die FAIR-Prinzipien</a>.


```{admonition} Weitere Informationen
:class: seealso
Der Open Data Support der Europäischen Kommission hat ein <a href="https://data.europa.eu/sites/default/files/d2.1.2_training_module_2.2_open_data_quality_de_edp.pdf" class="external-link" target="_blank">Trainingsmodul</a> als Präsentation (pdf) zur Qualität von offenen Daten und Metadaten veröffentlicht. 

Die Qualität von Daten ist zudem Thema einer weiteren 
<a href="https://quadriga-dk.github.io/Tabelle-Fallstudie-1/Markdown/4_Qualit%C3%A4tsbewertung.html" class="external-link" target="_blank">Lerneinheit</a> unseres Projektes <a href="https://www.quadriga-dk.de/de/" class="external-link" target="_blank">QUADRIGA</a>.

Falls Sie noch nach einem grundsätzlichen Überblick zum Thema Metadaten suchen, sei Ihnen das 
<a href="https://wiki.dnb.de/download/attachments/43523047/201209_metadaten.pdf" class="external-link" target="_blank">Kleine Handbuch Metadaten</a> von Stefanie Rühle, Kompetenzzentrum Interoperable Metadaten, empfohlen.
```

**Literatur**

```{bibliography}
:filter: docname in docnames
```