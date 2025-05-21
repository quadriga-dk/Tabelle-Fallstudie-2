# Beispiel und Implementierungen 

````{margin}
```{admonition} Hinweis
:class: hinweis
CKAN unterstützt Organisationen und Gruppen, die jeweils ihre eigenen Daten verwalten, aber Teil eines gemeinsamen Portals sein können. Damit eignet es sich besonders für dezentrale Verwaltungsstrukturen, z. B. bei föderalen Behörden oder wissenschaftlichen Konsortien.
```
````

Die Umsetzung von Metadatenrepositorien mit DCAT-AP-Vokabular erfolgt meistens durch die Verwendung des *Comprehensive Knowledge Archive Network (CKAN)*. CKAN ist die weltweit führende Open-Source-Plattform für Datenportale und erleichtert das Veröffentlichen, Teilen und Arbeiten mit Daten. Dabei handelt es sich um ein Datenmanagementsystem, das eine leistungsstarke Plattform zum Katalogisieren, Speichern und Zugreifen auf Datensätze bietet. Zu den Funktionen von CKAN gehören neben einer benutzerfreundlichen Oberfläche unter anderem ein vollständiges Application Programming Interface, API (für Daten und Katalog), diverse Visualisierungstools und vieles mehr {cite}`CKAN_User_Guide`.

````{margin}
```{admonition} Hinweis
:class: hinweis
CKAN bietet einfache Visualisierungsfunktionen an (Diagramme, Tabellenansichten), kann aber durch Plugins oder externe Tools wie Recline.js, DataWrapper, Grafana, Jupyter Notebooks erweitert werden. Auch die direkte Integration mit RDF-Triplestores oder SPARQL-Endpunkten ist über Erweiterungen denkbar.
```
````

In CKAN werden Daten als Datensätze organisiert, die jeweils eine Sammlung von Informationen wie beispielsweise Kriminalstatistiken oder Wetterdaten enthalten. Jeder Datensatz umfasst Metadaten (z. B. Titel, Herausgeber, Format) und mehrere Ressourcen, die die eigentlichen Daten in verschiedenen Formaten (z. B. CSV, PDF) bereitstellen {cite}`CKANWang`. Ressourcen können direkt in CKAN gespeichert oder als Links auf externe Quellen bereitgestellt werden. CKAN ermöglicht eine flexible Datenverwaltung und Zugänglichkeit in verschiedenen Formaten und fördert dadurch sowohl die Zusammenarbeit auf interinstitutioneller Ebene als auch das zivile Vertrauen durch erhöhte Transparenz. Des Weiteren können die Datenverwaltungskapazitäten des CKAN zur Datenanalyse, Datenaufbewahrung und Veröffentlichung im akademischen und dienstlichen Bereich verhelfen {cite}`Winn2013`. 

Das deutsche Metadatenportal [govdata.de](https://www.govdata.de/) wurde genau nach den zuvor beschriebenen Standards und Systemen entwickelt. Im Portal können unterschiedlichste Datensätze durchsucht werden, mit detaillierten Informationen darüber, woher sie stammen, welche Institution sie bereitgestellt hat und vieles mehr. 

Im nächsten Kapitel befassen wir uns mit ausgewählten Datensätzen, die im Portal verfügbar sind (dank interoperabler Technologien), sowie mit den Vorteilen und Schwächen der aktuellen Umsetzung im Rahmen der Philosophie offener Daten.
