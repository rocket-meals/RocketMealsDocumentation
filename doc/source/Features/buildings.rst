Gebäudeinformationen
=====================

Eine der Herausforderungen für Studierende, insbesondere für Erstsemester, ist es, sich auf dem Campus zurechtzufinden und die wichtigsten Gebäude für ihr Studium zu finden. Obwohl dies nicht direkt in den Zuständigkeitsbereich eines Studierendenwerks fällt, kann es ein zusätzlicher Vorteil sein, der Studierenden hilft und sie dazu ermutigt, Ihre App zu nutzen.

Mit der Gebäudeinformationsfunktion können Sie den Studierenden und Endnutzern helfen, die wichtigsten Gebäude für ihr Studium zu finden. Diese Funktion kann in der Rocket Meals Software für die Endnutzer implementiert werden.

Einrichtung der Gebäudeinformationen
-------------------------------------

**Einmalige Einrichtung**:

Im Rahmen der Einrichtungsgebühren kann eine einmalige Einrichtung der Gebäudeinformationen vorgenommen werden. Dabei benötigen wir die Informationen Ihrer Gebäuden (wie Mensen, Wohnanlagen, ...). Zudem werden öffentliche Informationen der am Ort ansässigen Hochschulen und Universitäten genutzt. Unser Team wird vor Ort die Informationen sammeln und Fotos von den Gebäuden machen. Dies bietet den Vorteil, dass die Informationen von Anfang an in der App verfügbar sind und die Studierenden sofort davon profitieren können. Bitte beachten Sie, dass dieser Service einen vertretbaren Aufwand von 1-2 Arbeitstagen beinhaltet.

**Kooperation mit Hochschulen und Universitäten**:

Eine weitere Möglichkeit ist die Zusammenarbeit mit den Hochschulen und Universitäten, um eine automatische Schnittstelle für die Gebäudeinformationen zu nutzen. Dies kann besonders nützlich sein, wenn regelmäßige Aktualisierungen der Gebäudeinformationen erforderlich sind oder wenn die Hochschulen und Universitäten bereits über ein System verfügen, das diese Informationen bereitstellt.

Aktualisierung der Gebäudeinformationen
----------------------------------------

Unabhängig von der gewählten Methode zur Einbindung und Aktualisierung der Gebäudeinformationen bietet diese Funktion einen Mehrwert für die Studierenden und kann dazu beitragen, die Nutzung der Rocket Meals App zu erhöhen.

Wahrscheinlich haben Sie bereits ein System, über das Sie Ihre Informationen verbreiten und darstellen. Eine manuelle Übertragung in Rocket Meals bedeutet für Sie natürlich doppelte Arbeit. Deshalb bieten wir Ihnen eine Möglichkeit der automatischen Synchronisierung. Hierfür haben Sie zwei Optionen:

**Strukturiertes Format**:

- **FTP oder REST-Schnittstelle**: Wenn Sie uns Ihre Informationen in einem gängigen Format wie JSON oder CSV anbieten können, z. B. über einen FTP-Job oder eine REST-Schnittstelle, können wir ein Skript implementieren, das Ihr Format automatisch einpflegt. Hierfür wird abhängig vom Umfang und der Komplexität ein gesondertes Angebot besprochen.

- **Web-Crawler**:
  - Nicht immer haben Sie die Möglichkeit, Daten von Ihrer Webseite und dem zugehörigen Content-Management-System bereitzustellen, wie beispielsweise mit einem Typo3-System. Eine Nachimplementierung bei Ihrem Anbieter kann sich aus finanziellen Gründen möglicherweise nicht lohnen oder es gibt andere Gründe, die dagegen sprechen. In diesem Fall bieten wir die Möglichkeit, die öffentlich zugänglichen Informationen von Ihrer Webseite automatisiert in Rocket Meals einpflegen zu lassen. Dabei verwenden wir einen sogenannten "Crawler", ein Programm, das Ihre Webseite wie ein Benutzer aufruft. Diese Lösung muss individuell auf Ihre Webseite zugeschnitten werden und bedarf einer Anpassung, wenn sich Grundlegendes an den zu besuchenden Seiten ändert. TODO: Bewertung dieser Lösung
  - Hierfür wird abhängig vom Umfang und der Komplexität ein gesondertes Angebot besprochen.

**Community-basierte Lösung**:

In der Zukunft möchten wir eine Community-basierte Lösung anbieten, bei der Studierende die Informationen aktuell halten können, indem sie Vorschläge machen. Dies ermöglicht es, die Informationen stets auf dem neuesten Stand zu halten und die Studierenden aktiv in den Prozess der Aktualisierung der Gebäudeinformationen einzubeziehen.

**API**:

Sie können die `API <../Reference/api.html>`_ verwenden, um die Gebäudeinformationen zu aktualisieren. Dies bietet eine automatisierte Möglichkeit, die Informationen regelmäßig zu aktualisieren und sicherzustellen, dass sie stets auf dem neuesten Stand sind.

**Manuell**:

Sie können die Gebäudeinformationen manuell unter der Adresse des Backend aktualisieren: https://<Rocket Meals Instanz>/api/admin/content/buildings
Eine manuell aktualisierte Gebäudeinformation enthält verschiedene Felder, die Sie nach Belieben ausfüllen können:

- **Name**: Der Name des Gebäudes.
- **Image**: Hier können Sie ein Bild hochladen.
- **Image Remote URL**: Hier können Sie eine URL zu einem Bild angeben. Dieses wird vorzugsweise verwendet, anstelle des Bildes, das Sie hochladen können.
- **URL**: Hier können Sie eine URL zu weiteren Informationen des Gebäudes hinterlegen.
- **Content**: Der Inhalt zur Beschreibung des Gebäudes im Markdown-Format.
- **Year of Construction**: Jahr der Errichtung
- **Canteens**: Relation zu einer zugehörigen Mensa, welche in diesem Gebäude vorhanden ist.
- **Apartments**: relation zu mehreren Apartments / Wohnanlagen.
- **Coord**: Koordination Informationen, welche den Standort des Gebäudes repräsentieren.

- **Be Source for Translation**: Ob die angezeigte Sprache als Ausgangssprache verwendet werden soll (nur verfügbar, wenn die automatische Übersetzungsfunktion aktiviert ist). In diesem Fall sollten Sie bei den anderen Sprachen diese Option deaktivieren, wenn Sie die Ausgangssprache ändern möchten.
- **Let Be Translated**: Ob die angezeigte Sprache automatisch übersetzt werden soll (nur verfügbar, wenn die automatische Übersetzungsfunktion aktiviert ist).
- **Create Translations for All Languages**: Ob für alle Sprachen eine Übersetzung erstellt werden soll (nur verfügbar, wenn die automatische Übersetzungsfunktion aktiviert ist).


