# "Layer cake" Architektur
![The Semantic Web Layer Cake](The-Semantic-Web-layer-cake-presented-by-Tim-Berners-Lee-at-the-XML-2000-conference.png)
*Abbildung 1: Der Semantic Web Layer Cake* Bildquelle: {cite}`Hendler2001`

The Semantic Web "layer cake" presented by Tim Berners-Lee at the XML 2000 conference.

Auf der obenstehenden Grafik wird die Struktur vom Semantic Web dargestellt als eine geschichtete Architektur, indem verschiedene Technologien und Konzepte zusammenkommen und interagieren, um das Framework von sinnvollen und strukturierten Daten und den Bezügen darunter zu unterstützen.
Wir gehen stufenmäßig bei der Erklärung jeder Schicht vor:
1. Unicode & URI (Universal Resource Indicator) - Unicode in der Grundschicht stellt sicher, dass der ganze Text konsistent repräsentiert durch eine globale Codierung von allen Zeichen wird. URI dient als Standartidentifikator für alle Ressourcen im Web. 
2. XML, Namespace, & XML Schema - eXtensible Markup Language (XML) ist ein flexibles Textformat für Datenstrukturierung. Es ist eine Datenvermittlungswerkzeug. Namespace verhilft dazu, Namenkonflikte durch die Identifizierung von Vokabularien zu vermeiden. XML-Schemata definieren die Struktur und Datentypen von XML-Dokumenten durch die Feststellung von Regeln diesbezüglich.
3. RDF (Resource Description Framework) & RDF Schema - die schon obenerklärten Konzepte werden mit eingewoben, damit Informationen über Datenressourcen strukturierend dargestellt werden können.
4. Ontology & Vocabulary - die Ontologie bietet eine Möglichkeit, strukturierte Vokabulare zu definieren, die Beziehungen und Kategorien in einem bestimmten Bereich beschreiben (z. B. „eine Katze ist ein Tier“). Diese Schicht ist entscheidend, um Maschinen zu ermöglichen, Beziehungen zwischen verschiedenen Datenpunkten zu verstehen und so Schlussfolgerungen und logische Ableitungen zu unterstützen. Das Vokabular bezieht sich auf die spezifischen Begriffe und Konzepte, die verwendet werden, um Entitäten und Beziehungen in einem Wissensbereich zu beschreiben.
5. Logik - die Logik ermöglicht automatisierte Prozesse von Entscheidungstreffen aufgrund strukturierter Daten.
6. Proof - die Prüfschicht sorgt für valide Ergebnisse durch die Validierung von den Schritten, die zu einer Schlussfolgerung führen. 
7. Trust - die oberste Schicht der Architektur setzt sich mit der Etablierung der Vertrauenwürdigkeit der Daten durch Authentifizierungsmechanismen und die Prüfung der Zuverlässigkeit der Datenquellen. 
Ein wichtiger Bauteil, der auf mehreren Schichten mitwirkt, ist die digitale Signatur als Technologie, die die Datenintegrität sicherstellt und die Nachprüfung davon, wer die Daten erstellt hat. 

Das Konzept von verlinkten Daten, oder *Linked Data* ist wichtig für die vollkommene Durchsetzung einer erfolgreichen Semantic-Web-Struktur. In unseren vorherigen Fallstudie über die Reproduzierbarkeit von Datenanalysen haben wir uns eben mit diesem Konzept auseinandergesetzt - [hier](https://quadriga-dk.github.io/Tabelle-Fallstudie-1/Markdown/16_Linked-Data.html).