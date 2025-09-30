# Definition & theoretische Grundsätze

````{margin}
```{admonition} Was sind Software-Agenten? 
:class: hinweis
Software-Agenten sind autonome Programme, die selbstständig im Sinne eines definierten Ziels handeln. Sie können Informationen sammeln, Entscheidungen treffen und Aufgaben ausführen, ohne dass ein Mensch direkt eingreifen muss. <span style="color:red">*Quelle?*</span>

```
````


Der Begriff *Semantische Technologien* entstand als Forschungsfeld in der Informatik Anfang der 2000er Jahre. Im Mai 2001 veröffentlichte Sir Tim Berners-Lee einen grundlegenden Artikel, in dem er die Vision des Semantic Web präsentierte {cite}`berners-lee2001semantic`. Das Ziel des Semantic Web besteht darin, Webinhalte strukturiert und maschinenlesbar zu machen, sodass Software-Agenten eigenständig komplexe Aufgaben für Benutzer ausführen können. Die Semantischen Technologien sollen wiederum als Werkzeuge verstanden werden, die dazu verhelfen, das Semantic Web aufzubauen. Sie sollen Informationen maschinell verständlich machen, indem sie die Bedeutung (Semantik) und die Beziehungen zwischen Daten explizit definieren. Zu den zentralen Werkzeugen gehören Ontologien, Taxonomien und logische Schlussfolgerungsmechanismen, die wir später genauer erklären werden.
<span style="color:red">*hier fehlt m. E. eine Quelle*</span>

Die zentrale Idee ist, dass Maschinen Informationen verstehen und ohne menschliche Unterstützung komplexe Interaktionen durchführen können {cite}`Sabucedo2010eService`. Zur Realisierung dieser Vision wurden in den letzten Jahren bedeutende technologische Fortschritte erzielt. Ein wichtiger Standard ist die Ontology Web Language (<a href="https://www.w3.org/OWL/" class="external-link" target="_blank">OWL</a>), die vom World Wide Web Consortium (<a href="https://www.w3.org/" class="external-link" target="_blank">W3C</a>) entwickelt wurde. OWL ermöglicht die formale Definition von Wissen über bestimmte Domänen, also die Erstellung von Ontologien, wie sie nach der Definition von Gruber [1993] verstanden werden.
<span style="color:red">*Gruber fehlt als Literaturangabe*</span>
<span style="color:red">*Ist das 2025 noch relevant?*</span>


---

Die Integration semantischer Technologien in IT-Lösungen erlaubt die Automatisierung von Prozessen und die Einführung von "Intelligenz" in Softwaresysteme {cite}`valiente2012integration`. Dadurch können Operationen ausgeführt werden, die mit herkömmlichen, datenbasierten Ansätzen nicht möglich sind. Semantische Technologien machen implizite Informationen explizit und fördern dadurch Interoperabilität und logische Schlussfolgerungen. Software-Agenten können somit Dienste für Benutzer suchen und bereitstellen.

Um dieses Wissen für Maschinen zugänglich zu machen, ist eine formale und gemeinsame Repräsentation erforderlich, die durch Ontologien ausgedrückt wird. Ontologien sind zu einem wichtigen Instrument geworden, ohne die die produktive Datenadministrierung und -implementierung heutzutage unvorstellbar wären {cite}`gardner_ontologies_2005`. Diese Standards sorgen für eine interoperable Plattform, die solide und zukunftssicher ist. Die bevorzugte Sprache OWL findet in der verwaltungswissenschaftlichen Gemeinschaft breite Akzeptanz.

---

Die Betrachtung des Semantic Web ist in vielerlei Hinsicht relevant: Es eröffnet neue Möglichkeiten für die Datenverarbeitung, verbessert die Interoperabilität zwischen verschiedenen Systemen und erleichtert die Nachnutzung von Daten. Dies ist besonders für Forschungsfelder von Bedeutung, in denen große Datenmengen analysiert und reproduzierbare Ergebnisse angestrebt werden.

```{admonition} Semantic Web und Verwaltung(swissenschaft) 
:class: keypoint
Auch für die Verwaltungswissenschaft sind Semantic Web und Linked Data von großer Bedeutung - sie ermöglichen eine effizientere Vernetzung und Integration von Verwaltungsdaten über Behörden- und Ressortgrenzen hinweg, fördern Transparenz und Nachvollziehbarkeit staatlichen Handelns und unterstützen datenbasierte Entscheidungsprozesse. Darüber hinaus erleichtert die semantische Aufbereitung öffentlicher Daten die Entwicklung innovativer E-Government-Lösungen sowie die Umsetzung und Strukturierung von Open-Data-Initiativen.
```

---

Das Semantic Web ist die Bezeichnung für eine neue Generation von Webtechnologien, die darauf abzielen, die Kommunikation zwischen Menschen, die unterschiedliche Terminologien verwenden, zu verbessern {cite}`Hendler2003ScienceAT`. Die Wortwahl von Menschen unterscheidet sich oft, auch wenn sie über dieselben Themen sprechen oder schreiben. Deshalb ist es hilfreich, über ein Werkzeug zu verfügen, das Datenbanken besser miteinander verbindet und die Nutzung von multimedialen Sammlungen erleichtert. Darüber hinaus ermöglicht das Semantic Web neue Mechanismen zur Unterstützung des "agentenbasierten" Rechnens, bei dem Menschen und Maschinen interaktiver zusammenarbeiten {cite}`gibbins_agent-based_2003`.

Im Gegensatz zum aktuellen Web, das Links zwischen Seiten bereitstellt, die für den menschlichen Konsum gedacht sind, ergänzt das Semantic Web diese Struktur um Informationseinheiten, die maschinenlesbare Beschreibungen von Webseiten und anderen Webressourcen enthalten. Diese Dokumente können so miteinander verknüpft werden, dass der Computer Informationen darüber erhält, wie die Begriffe in einem Dokument mit den Begriffen in einem anderen Dokument in Beziehung stehen. Dies ermöglicht das automatisierte Annotieren, Entdecken, Veröffentlichen, Bewerben und Zusammenstellen von Diensten {cite}`taye_understanding_2010`.

Um dies zu erreichen, verwendet das Semantic Web neue Websprachen, die auf RDF (Resource Description Framework) basieren (s. Abb. 2.2). RDF ist ein Standardmodell zur Beschreibung von Informationen im Web, welches ermöglicht, Daten in einer maschinenlesbaren Form zu strukturieren und zu verknüpfen {cite}`decker_semantic_2000`. Diese Sprachen gehen über die Präsentationsmöglichkeiten von HTML (Hypertext Markup Language), das für die meisten heutigen Webseiten verwendet wird, und die Dokumenten-Tagging-Funktionen von XML (Extensible Markup Language) hinaus. RDF ermöglicht es, Beziehungen zwischen Ressourcen darzustellen und unterstützt die Interoperabilität zwischen verschiedenen Datenquellen, was für die Entwicklung intelligenter Anwendungen von entscheidender Bedeutung ist.

```{figure} /assets/Explanatory_diagram_for_the_comprehensive_concept_of_Semantic_Web.png
---
name: Konzept Semantic Web
alt: Ein erläuterndes Diagramm zum umfassenden Konzept des Semantic Web
width: 420px
---
Erläuterndes Diagramm zum umfassenden Konzept des Semantic Web, <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.de" class="external-link" target="_blank">CC BY-SA</a> <a href="https://commons.wikimedia.org/wiki/File:Explanatory_diagram_for_the_comprehensive_concept_of_Semantic_Web.png" class="external-link" target="_blank">Luís M. Machado</a>.
```

Insgesamt zielt das Semantic Web darauf ab, die Art und Weise, wie Informationen im Internet strukturiert und interpretiert werden, weiterzuentwickeln, sodass eine intelligentere und effizientere Interaktion zwischen Benutzern und Maschinen ermöglicht wird. Das Semantic Web ist die natürliche Entwicklung des World Wide Web, wie von dem Informationswissenschaftler Tim Berners-Lee erdacht {cite}`Cardoso2006`. Wenn Web 1.0 auf verlinkten Webseiten beruhte, und Web 2.0 auf verlinkten Applikationen (bspw. Soziale Netzwerke), steht das Web 3.0 in Beziehung mit verlinkten Daten ([Semantic Web](https://www.techtarget.com/searchcio/definition/Semantic-Web)).
<span style="color:red">*Ist das ein Literaturverweis?*</span>


```{admonition} Was  Sie mitnehmen sollten
:class: keypoint 
Das Semantic Web erweitert das heutige Web um maschinenlesbare Datenstrukturen, die eine intelligentere Interaktion zwischen Mensch und Maschine ermöglichen. Es schafft damit die Grundlage für eine vernetzte, automatisierte und semantisch interpretierbare Datenwelt, in der Informationen effizienter gefunden, verarbeitet und genutzt werden können.
```

```{admonition} Weiterführende Literatur
:class: seealso
Das W3C hat eine sehr kurze <a href="https://www.w3.org/RDF/Metalog/docs/sw-easy" class="external-link" target="_blank">Zusammenfassung</a> des Semantic Web veröffentlicht (auf Englisch).

Eine weitere Zusammenfassung hat der deutsche Internetdienstanbieter <a href="https://www.ionos.de/digitalguide/online-marketing/suchmaschinenmarketing/semantic-web/" class="external-link" target="_blank">IONOS</a> veröffentlicht.
```

**Literatur**

```{bibliography}
:filter: docname in docnames
```