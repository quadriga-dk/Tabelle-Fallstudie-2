# "Layer cake" Architektur
![The Semantic Web Layer Cake](The-Semantic-Web-layer-cake-presented-by-Tim-Berners-Lee-at-the-XML-2000-conference.png)


*Abbildung 1: Der Semantic Web Layer Cake* Bildquelle: {cite}`Hendler2001`

Die Grafik oben zeigt die die geschichtete Architektur (Layer Cake-Architektur) des Semantic Web. Diese Struktur beschreibt, wie verschiedene Technologien und Konzepte zusammenarbeiten, um das Web mit verständlichen und vernetzten Daten anzureichern.
Wir erklären nun stufenweise jede Schicht und beginnen bei der untersten:

1. Unicode & URI (Universal Resource Indicator) - Unicode stellt sicher, dass Texte weltweit einheitlich und in allen Sprachen korrekt dargestellt werden können. URI dient als eindeutige Adresse, um jede Ressource im Web identifizieren zu können.
2. XML, Namespace, & XML Schema - eXtensible Markup Language (XML) ist ein flexibles Textformat, um Daten in strukturierter Form darzustellen – ähnlich wie eine Tabelle oder eine Liste. Es dient als Datenvermittlungswerkzeug. Namespaces verhindern Verwechslungen, wenn unterschiedliche Datensätze dieselben Begriffe verwenden. Sie schaffen also klare Zuordnungen. XML-Schemata definieren die Struktur und Datentypen von XML-Dokumenten, indem sie entsprechende Regeln festlegen.
3. RDF (Resource Description Framework) & RDF Schema - RDF erlaubt es, Informationen so zu verknüpfen, dass Maschinen sie verstehen können. Zum Beispiel: „Max arbeitet bei Firma XY“. Das RDF Schema erweitert RDF, indem es definiert, welche Art von Informationen angegeben werden können (Bei diesem Beispiel Personen, Firmen oder Beziehungen zwischen ihnen).

4. Ontology & Vocabulary - die Ontologie bietet eine Möglichkeit, strukturierte Vokabulare zu definieren, die Beziehungen und Kategorien in einem bestimmten Bereich beschreiben (z. B. „Eine Katze ist ein Tier“). Diese Schicht ist entscheidend, um es Maschinen zu ermöglichen, die Beziehungen zwischen verschiedenen Datenpunkten zu verstehen und dadurch Schlussfolgerungen sowie logische Ableitungen zu unterstützen. Das Vokabular bezieht sich auf spezifische Begriffe und Konzepte, die verwendet werden, um Entitäten und ihre Beziehungen innerhalb eines Wissensbereichs zu beschreiben, wie ein Wörterbuch für Daten. 
5. Logic - Diese Schicht ermöglicht es, automatisierte Entscheidungen basierend auf den Daten zu treffen. Beispiel: „Wenn A wahr ist und B wahr ist, dann folgt C.“
6. Proof - die Prüfschicht stellt die Validität der Ergebnisse sicher, indem sie die Schritte überprüft, die zu einer Schlussfolgerung führen. Ähnlich wie bei einer mathematischen Beweisführung.
7. Trust - Die oberste Schicht schafft Vertrauen in die Daten, z. B. durch digitale Signaturen. Diese zeigen an, wer die Daten erstellt hat und ob sie unverändert sind. 

Jede dieser Schichten baut auf den vorherigen auf. Das Konzept von verlinkten Daten, oder *Linked Data*, ist essenziell für die vollständige Umsetzung einer erfolgreichen Semantic-Web-Struktur. In unserer vorherigen Fallstudie zur Reproduzierbarkeit von Datenanalysen haben wir uns genau mit diesem Konzept auseinandergesetzt - [Weitere Informationen finden Sie hier](https://quadriga-dk.github.io/Tabelle-Fallstudie-1/Markdown/16_Linked-Data.html).
