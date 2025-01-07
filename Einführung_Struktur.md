# Struktur der Fallstudie
Die modellhafte Forschungsfrage dieser Fallstudie lautet: **Welche offenen Daten gibt es, die dazu beitragen, den Bewässerungsbedarf von Bäumen in einer bestimmten Region zu ermitteln?**

Basierend auf den verfügbaren offenen Datenquellen werden Abfragen mithilfe der Abfragesprache SPARQL entwickelt, um relevante Informationen zu extrahieren. Dabei wird die Nachnutzbarkeit der Daten untersucht, ihre Qualität bewertet sowie der Entstehungskontext nachvollzogen. Die Abfragen ermöglichen eine strukturierte Analyse der Daten, um spezifische Antworten zur Bewässerung zu erhalten.

Die Nutzung und erste Schritte mit SPARQL werden in dieser Fallstudie anschaulich erläutert.

Die Gliederung der Fallstudie in Kapitel und Abschnitte können Sie immer in der Menüleiste auf der linken Seite nachvollziehen. Die rechte Menüleiste zeigt Ihnen an, in welchem Abschnitt eines Kapitels Sie sich gerade befinden.

Um die Forschungsfrage zu beantworten, benötigen wir Daten. Diese können und wollen wir nicht selbst erheben, weshalb wir Daten nachnutzen müssen. Wir greifen in dieser Fallstudie auf Metadaten aus dem europäischen Metadatenportal zurück. Daher werden in einem 1. Schritt die grundlegenden Technologien, die gängige Metadatenschemata ausmachen erläutert, nämlich Semantic Web & Linked Data .

Im 2. Schritt machen wir Sie mit einem der wichtigsten Werkzeuge für die Operationalisierung von Metadatenrepositorien - das DCAT-AP-Standardiesierungsschema, indem auch die politisch-administrativen Dimensionen im Kontext der öffentlichen Verwaltung und Opendata mit berücksichtigt werden.

Im 3. Schritt geht es dann darum, die Maßnahmen zur Qualitätsmessung von Metadaten durchzugehen , um zu prüfen, ob sie den Ansprüchen gerecht werden. Dazu stellen wir Ihnen verschiedene die Qualitätskriterien des Metadata Quality Assessment (MQA) für Metadaten vor.

Im 4. Schritt bewegen wir uns näher an die Praxis und zeigen Ihnen, wie Metadaten erfragt werden können mithilfe der SPARQL-Abfragesprache. Dazu machen wir Sie mit den Grundlagen des Arbeitens mit SPARQL vertraut, samt der Syntax und wichtigster Befehle. Schließlich vollziehen wir einige Abfragen, die sich auf unsere Fragestellung beziehen, und reflektieren darüber, inwiefern der jetzige Stand der implementierten Konzepte gelingen oder verbesserungsbedürftig ist.

Das ganze JupyterBook lässt sich darüber hinaus in zwei Blöcke teilen. Den ersten Block bilden die Kapitel 2, 3 und 4, die aus mindestens einem Wissen vermittelnden Abschnitt und jeweils einer kurze Übung bestehen, in der die erworbenen Kenntnisse geprüft werden können. Diese Kapitel nehmen jedes für sich etwa 15 Minuten Bearbeitungszeit in Anspruch. Den zweiten Block nimmt Kapitel 5 ein, das aus einer Einführung in die statistische Software R und dessen Nutzung zur Analyse der Reproduzierbarkeit und letztlich zur Beantwortung der Forschungsfrage besteht. Dies ist wesentlich umfangreicher als die vorherigen Kapitel und kann - je nach Vorkenntnissen - gute 2 bis 3 Stunden Bearbeitungszeit umfassen.