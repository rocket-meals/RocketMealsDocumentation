Neuigkeiten
===========

Eine Plattform ohne Neuigkeiten ist wie ein Tag ohne Sonnenschein. Mit der News-Funktion können Sie Nachrichten anzeigen. In der Rocket Meals Software für die Endnutzer werden die aktuellsten Nachrichten (maximal 20) angezeigt. Wenn Nutzer die Neuigkeiten auswählen, gelangen sie zu einer detaillierteren Ansicht.

Wenn Sie die Neuigkeiten-Funktion deaktivieren möchten, können Sie dies im Backend unter folgender Adresse selbst einstellen: https://<Rocket Meals Instanz>/api/admin/content/app_settings_news

Es gibt zwei Möglichkeiten, wie Sie Neuigkeiten in die Software einbinden können:

Synchronisierung
-----------------------

Wahrscheinlich haben Sie bereits ein System, über das Sie Ihre Informationen verbreiten und darstellen. Eine manuelle Übertragung in Rocket Meals bedeutet für Sie natürlich doppelte Arbeit. Deshalb bieten wir Ihnen eine Möglichkeit der automatischen Synchronisierung. Hierfür haben Sie zwei Optionen:

- **Strukturiertes Format**:
  - Wenn Sie uns Ihre Neuigkeiten in einem gängigen Format wie JSON oder CSV anbieten können, z. B. über einen FTP-Job oder eine REST-Schnittstelle, können wir ein Skript implementieren, das Ihr Format automatisch einpflegt. Hierfür wird abhängig vom Umfang und der Komplexität ein gesondertes Angebot besprochen.

- **Web-Crawler**:
  - Nicht immer haben Sie die Möglichkeit, Daten von Ihrer Webseite und dem zugehörigen Content-Management-System bereitzustellen, wie beispielsweise mit einem Typo3-System. Eine Nachimplementierung bei Ihrem Anbieter kann sich aus finanziellen Gründen möglicherweise nicht lohnen oder es gibt andere Gründe, die dagegen sprechen. In diesem Fall bieten wir die Möglichkeit, die öffentlich zugänglichen Informationen von Ihrer Webseite automatisiert in Rocket Meals einpflegen zu lassen. Dabei verwenden wir einen sogenannten "Crawler", ein Programm, das Ihre Webseite wie ein Benutzer aufruft. Diese Lösung muss individuell auf Ihre Webseite zugeschnitten werden und bedarf einer Anpassung, wenn sich Grundlegendes an den zu besuchenden Seiten ändert. TODO: Bewertung dieser Lösung
  - Hierfür wird abhängig vom Umfang und der Komplexität ein gesondertes Angebot besprochen.

API
-----------------------

Sie können die `API <../Reference/api.html>`_ verwenden.

Manuell
-----------------------

Sie können Neuigkeiten manuell unter der Adresse des Backend erstellen: https://<Rocket Meals Instanz>/api/admin/content/news
Eine manuell angelegte Neuigkeit enthält folgende Felder, die Sie nach Belieben ausfüllen können:

- **Notice Private**: Eine private Notiz, die in der Rocket Meals Software nicht sichtbar ist, aber über die API abgerufen werden kann.
- **Image**: Hier können Sie ein Bild hochladen.
- **Image Remote URL**: Hier können Sie eine URL zu einem Bild angeben. Dieses wird vorzugsweise verwendet, anstelle des Bildes, das Sie hochladen können.
- **Title**: Der Titel Ihrer Neuigkeit.
- **Content**: Der Inhalt Ihrer Neuigkeit im Markdown-Format.

- **Be Source for Translation**: Ob die angezeigte Sprache als Ausgangssprache verwendet werden soll (nur verfügbar, wenn die automatische Übersetzungsfunktion aktiviert ist). In diesem Fall sollten Sie bei den anderen Sprachen diese Option deaktivieren, wenn Sie die Ausgangssprache ändern möchten.
- **Let Be Translated**: Ob die angezeigte Sprache automatisch übersetzt werden soll (nur verfügbar, wenn die automatische Übersetzungsfunktion aktiviert ist).
- **Create Translations for All Languages**: Ob für alle Sprachen eine Übersetzung erstellt werden soll (nur verfügbar, wenn die automatische Übersetzungsfunktion aktiviert ist).
