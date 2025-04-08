# SPARQL

```{admonition} Lernziele
:class: lernziele
- Lernende befassen sich mit der maschinellen Abfrage von Daten in Open Data Portalen unter Anwendung von SPARQL
- Lernende praktizieren verschiedene SPARQL Techniken über die API von data.europa
```

In diesem Kapitel wird die Abfragesprache <a href="https://de.wikipedia.org/wiki/SPARQL" class="external-link" target="_blank">SPARQL</a> vorgestellt, die speziell zur Abfrage von Daten in RDF-Formaten entwickelt wurde {cite}`ducharme_learning_2013`. SPARQL ermöglicht es, gezielt Metadaten aus Open Data Portalen wie data.europa.eu abzurufen und komplexe Fragestellungen maschinell zu beantworten. Ziel dieses Kapitels ist es, eine praxisnahe Anwendung von SPARQL zu veranschaulichen und unterschiedliche Abfragetechniken zu erlernen.

Das Erfragen von Metadaten kann durch die Erstellung von sogenannten *queries* erreicht werden. Dies ist der englische Begriff für das Abfragen von Daten oder Informationen, beispielsweise aus Datenbanken, Suchmaschinen oder Datensuchportalen wie Google oder aus wissenschaftlichen Archiven. Solche Abfragen können mithilfe von SPARQL durchgeführt werden. 

In den folgenden Übungen dieses Kapitels befassen Sie sich mit der eingangs vorgestellten Forschungsfrage, die die Bereitstellung von Daten durch die deutschen Bundesländer analysiert. Durch den technischen Einsatz von Jupyter Notebooks wird eine interaktive Umgebung geschaffen, die sowohl Code als auch Erläuterungen integriert, um die SPARQL-Syntax und deren praktische Anwendung verständlich zu machen. Ein besonderer Fokus liegt auf der Definition von *Endpoints* sowie der Nutzung von *Prefixes*, um Abfragen effizient zu gestalten. Im Laufe des Kapitels werden zudem typische Herausforderungen, wie unvollständige Metadaten und fehlende Paginierungsfunktionen, angesprochen und Lösungsansätze aufgezeigt.

```{admonition} Weiterführende Informationen
:class: seealso
Weitere Informationen zum Thema SPARQL und RDF, die allerdings ein gewisses Maß an Vorkenntnissen zum Verständnis benötigen, finden Sie auf den Seiten des <a href="https://www.w3.org/TR/sparql11-query/" class="external-link" target="_blank">W3C</a>.  
```


In diesem Kapitel finden Sie folgende Abschnitte: 

- [SPARQL Grundlagen](/SPARQL_Grundlagen.md)
- [SPARQL Übung 1](/SPARQL_Übung_1.md)
- [SPARQL Übung 2](/SPARQL_Übung_2.md)
- [SPARQL Reflexion](/SPARQL_Reflexion.md)