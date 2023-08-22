Wohnanlagen
=====================

Eine der größten Herausforderungen für Studierende ist es, bezahlbaren Wohnraum zu finden, insbesondere in Städten mit hohen Mietpreisen. Wahrscheinlich bietet Ihr Studierendenwerk ebenfalls Wohnanlagen für den schmalen Geldbeutel an. Die Wohnanlagenfunktion in der Rocket Meals Software kann Studierenden helfen, geeignete Wohnmöglichkeiten zu finden und sich über Ihre Einrichtungen und Dienstleistungen zu informieren, die in Ihren Wohnanlagen angeboten werden.

**Waschmaschinen**:

Ein häufiges Problem für Studierende in Wohnanlagen ist die Verfügbarkeit und der Zugang zu Waschmaschinen. Unsere Erfahrungen haben gezeigt, dass ein Hauptproblem der Studierenden darin besteht, zu wissen, wann ihre Wäsche fertig ist. Wir bieten eine Lösung für dieses Problem an. Lesen Sie mehr unter der Funktion: `Waschanlagen <../Reference/washingmachines.html>`_.

Einrichtung der Wohnanlageninformationen
-------------------------------------

**Einmalige Einrichtung**:

Im Rahmen der Einrichtungsgebühren kann eine einmalige Einrichtung der Wohnanlageninformationen vorgenommen werden. Dabei benötigen wir die Informationen Ihrer Wohnanlagen. Unser Team wird vor Ort weitere Informationen sammeln und Fotos von den Gebäuden machen. Dies bietet den Vorteil, dass die Informationen von Anfang an in der App verfügbar sind und die Studierenden sofort davon profitieren können. Bitte beachten Sie, dass dieser Service einen vertretbaren Aufwand von 1-2 Arbeitstagen beinhaltet.

Aktualisierung der Wohnanlageninformationen
----------------------------------------

**Strukturiertes Format**:

- **FTP oder REST-Schnittstelle**: Wenn Sie uns Ihre Wohnanlageninformationen in einem gängigen Format wie JSON oder CSV anbieten können, z. B. über einen FTP-Job oder eine REST-Schnittstelle, können wir ein Skript implementieren, das Ihr Format automatisch einpflegt. Hierfür wird abhängig vom Umfang und der Komplexität ein gesondertes Angebot besprochen.

- **Web-Crawler**:
  - Nicht immer haben Sie die Möglichkeit, Daten von Ihrer Webseite und dem zugehörigen Content-Management-System bereitzustellen. Eine Nachimplementierung bei Ihrem Anbieter kann sich aus finanziellen Gründen möglicherweise nicht lohnen oder es gibt andere Gründe, die dagegen sprechen. In diesem Fall bieten wir die Möglichkeit, die öffentlich zugänglichen Informationen von Ihrer Webseite automatisiert in Rocket Meals einpflegen zu lassen. Dabei verwenden wir einen sogenannten "Crawler", ein Programm, das Ihre Webseite wie ein Benutzer aufruft. Diese Lösung muss individuell auf Ihre Webseite zugeschnitten werden und bedarf einer Anpassung, wenn sich Grundlegendes an den zu besuchenden Seiten ändert. TODO: Bewertung dieser Lösung
  - Hierfür wird abhängig vom Umfang und der Komplexität ein gesondertes Angebot besprochen.

**Community-basierte Lösung**:

In der Zukunft möchten wir eine Community-basierte Lösung anbieten, bei der Studierende die Informationen aktuell halten können, indem sie Vorschläge machen. Dies ermöglicht es, die Informationen stets auf dem neuesten Stand zu halten und die Studierenden aktiv in den Prozess der Aktualisierung der Wohnanlageninformationen einzubeziehen.

**API**:

Sie können die `API <../Reference/api.html>`_ verwenden, um die Wohnanlageninformationen zu aktualisieren. Dies bietet eine automatisierte Möglichkeit, die Informationen regelmäßig zu aktualisieren und sicherzustellen, dass sie stets auf dem neuesten Stand sind.

**Manuell**:

Sie können die Wohnanlageninformationen manuell unter der Adresse des Backend aktualisieren: https://<Rocket Meals Instanz>/api/admin/content/buildings
Eine manuell aktualisierte Wohnanlageninformation enthält verschiedene Felder, die Sie nach Belieben ausfüllen können:

- **Available From**: Sofern die Wohnanlage frei zur Vermietung ist, kann hier ein Datum angegeben werden, welches den Endnutzern angezeigt wird.
- **Handicapped Accessible**: Ob diese Wohnung barrierefrei ist.
- **Family Friendly**: Ob diese Wohnung familienfreundlich ist.
- **Singleflat**: Ob diese Wohnung für Single-Personen ist, die nicht in einer WG wohnen möchten.
- **Building**: Relation zu einem zugehörigen Gebäude. Diese Informationen werden verwendet für die allgemeinen Informationen zum Gebäude der Wohnanlage.

- **Be Source for Translation**: Ob die angezeigte Sprache als Ausgangssprache verwendet werden soll (nur verfügbar, wenn die automatische Übersetzungsfunktion aktiviert ist). In diesem Fall sollten Sie bei den anderen Sprachen diese Option deaktivieren, wenn Sie die Ausgangssprache ändern möchten.
- **Let Be Translated**: Ob die angezeigte Sprache automatisch übersetzt werden soll (nur verfügbar, wenn die automatische Übersetzungsfunktion aktiviert ist).
- **Create Translations for All Languages**: Ob für alle Sprachen eine Übersetzung erstellt werden soll (nur verfügbar, wenn die automatische Übersetzungsfunktion aktiviert ist).

Unabhängig von der gewählten Methode zur Einbindung und Aktualisierung der Wohnanlageninformationen bietet diese Funktion einen Mehrwert für die Studierenden und kann dazu beitragen, die Nutzung der Rocket Meals App zu erhöhen.
