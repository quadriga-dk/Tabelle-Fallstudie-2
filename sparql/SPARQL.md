(sparql)=
# SPARQL

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

```{admonition} Lernziel: Abfragesprache SPARQL
:class: lernziele
1. Die grundlegenden Komponenten der SPARQL-Syntax können aufgezählt und ihre Rollen erläutert werden.
2. Einfache SPARQL-Abfragen können erstellt und durchgeführt werden, um spezifische Informationen aus einem Datenkatalog abzurufen.
```

In diesem Kapitel wird die Abfragesprache <a href="https://de.wikipedia.org/wiki/SPARQL" class="external-link" target="_blank">SPARQL</a> vorgestellt, die speziell zur Abfrage von Daten in RDF-Formaten entwickelt wurde {cite}`ducharme_learning_2013`. SPARQL ermöglicht es, gezielt Metadaten aus Open Data Portalen wie <a href="https://data.europa.eu/de" class="external-link" target="_blank">data.europa.eu</a> abzurufen und komplexe Fragestellungen maschinell zu beantworten. Ziel dieses Kapitels ist es, eine praxisnahe Anwendung von SPARQL zu veranschaulichen und unterschiedliche Abfragetechniken zu erlernen.

````{margin}
```{admonition} Hinweis 
:class: hinweis
Mehr zum Thema Queries erfahren Sie in diesem <a href="https://www.heise-homepages.de/glossary/query/" class="external-link" target="_blank">Artikel</a> von Heise.
```
````

Das Erfragen von Metadaten kann durch die Erstellung von sogenannten *Queries* erreicht werden. Dies ist der englische Begriff für das Abfragen von Daten oder Informationen, beispielsweise aus Datenbanken, Suchmaschinen oder Datensuchportalen wie Google oder aus wissenschaftlichen Archiven. Solche Abfragen können mithilfe von SPARQL durchgeführt werden. 

In den folgenden Übungen dieses Kapitels befassen Sie sich mit der eingangs vorgestellten Forschungsfrage, die die Bereitstellung von offenen Daten analysiert. Durch den technischen Einsatz von Jupyter Notebooks wird eine interaktive Umgebung geschaffen, die sowohl Code als auch Erläuterungen integriert, um die SPARQL-Syntax und deren praktische Anwendung verständlich zu machen. Ein besonderer Fokus liegt auf der Definition von *Endpoints* sowie der Nutzung von *Prefixes*, um Abfragen effizient zu gestalten. Im Laufe des Kapitels werden zudem typische Herausforderungen, wie unvollständige Metadaten und fehlende Paginierungsfunktionen, angesprochen und Lösungsansätze aufgezeigt.

```{admonition} Weiterführende Informationen
:class: seealso
Weitere Informationen zum Thema SPARQL und RDF, die allerdings ein gewisses Maß an Vorkenntnissen zum Verständnis benötigen, finden Sie auf den Seiten des <a href="https://www.w3.org/TR/sparql11-query/" class="external-link" target="_blank">W3C</a>.  
```


In diesem Kapitel finden Sie folgende Abschnitte: 

- [SPARQL Grundlagen](https://quadriga-dk.github.io/Tabelle-Fallstudie-2/sparql/SPARQL_Grundlagen.html)
- [SPARQL Übung 1](https://quadriga-dk.github.io/Tabelle-Fallstudie-2/sparql/SPARQL_%C3%9Cbung_1.html)
- [SPARQL Übung 2]([/SPARQL_Übung_2.md](https://quadriga-dk.github.io/Tabelle-Fallstudie-2/sparql/SPARQL_%C3%9Cbung_2.html))
- [SPARQL Reflexion]([/SPARQL_Reflexion.md](https://quadriga-dk.github.io/Tabelle-Fallstudie-2/sparql/SPARQL_Reflexion.html))

**Literatur**

```{bibliography}
:filter: docname in docnames
```
