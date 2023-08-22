Wäschereiverwaltung
=====================

Einleitung
--------------

Studierende in Wohnheimen haben oft Schwierigkeiten, den geeigneten Zeitpunkt zum Waschen ihrer Wäsche zu finden. Als Lösung bieten wir eine Funktion in unserer Software an, die den Status von Waschmaschinen in ihren Wohnanlagen überwacht und benutzerfreundliche Benachrichtigungen bereitstellt.

Funktionen
-----------------

Diese Funktion erlaubt Studierenden, den Status der Waschmaschinen in ihren Wohnanlagen über eine mobile App zu überprüfen. Dies kann bequem vom Sofa, während der Vorlesung oder von jedem anderen Ort aus geschehen. Auf diese Weise können Studierende sicherstellen, dass ihre Wäsche pünktlich fertig ist und auch überprüfen, wann eine Waschmaschine frei wird.

Für registrierte Benutzer der Rocket Meals Software gibt es noch weitere Vorteile. Sie können Benachrichtigungen erhalten, sobald eine bestimmte Waschmaschine frei wird. Dies bietet mehr Komfort und Flexibilität, da sie nicht ständig ihr Smartphone überprüfen oder einen Wecker stellen müssen.

Aktualisierung der Waschmaschinen-Informationen
--------------------------------------------------

Automatische Aktualisierungen sind in diesem Kontext unerlässlich. Manuell jede Waschmaschine in jeder Wohnanlage zu überprüfen, würde den Zweck dieser Funktion untergraben. Zur Einbindung der Waschmaschinen müssen diese internetfähig sein und ein Zugang zu diesen Informationen muss uns ermöglicht werden.

Wenn Sie in der Lage sind, uns Zugang zu den Informationen Ihrer Waschmaschinen zu gewähren, können wir ein automatisiertes Skript implementieren. Abhängig von der Komplexität und dem Umfang der Implementierung wird ein individuelles Angebot besprochen.

**API**:

Nutzen Sie die `API <../Reference/api.html>`_, um die Informationen der Waschanlagen zu aktualisieren. Diese automatisierte Methode stellt sicher, dass die Informationen regelmäßig aktualisiert und immer auf dem neuesten Stand sind.

**Manuell**:

Alternativ können Sie die Informationen der Waschanlagen manuell unter der Adresse des Backends aktualisieren: https://<Rocket Meals Instanz>/api/admin/content/washingmachines
Eine manuell aktualisierte Waschanlage enthält verschiedene Felder, die Sie nach Belieben ausfüllen können:

- **Name**: Name des Gebäudes.
- **Apartment**: Beziehung zur Wohnanlage.
- **Date Finished**: Datum, wann die Waschmaschine fertig ist.

Zusammenfassung
---------------------

Mit dieser Funktion bieten wir eine komfortable und zeitsparende Lösung für Studierende, die Schwierigkeiten haben, ihre Wäsche in Wohnheimen zu waschen. Wir bieten eine unkomplizierte Überwachung des Waschmaschinenstatus und benutzerfreundliche Benachrichtigungen, um den Waschprozess zu optimieren.
