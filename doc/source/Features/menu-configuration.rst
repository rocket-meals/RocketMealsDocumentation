Menü-Konfiguration
==================

Die Menü-Konfiguration ermöglicht es Endnutzern, über das Menü an der Seite auf verschiedene Funktionen der Software zuzugreifen und zu diesen zu navigieren. Über das Backend haben Sie die Möglichkeit, einzelne Funktionen zu deaktivieren, wodurch die entsprechenden Reiter im Menü nicht mehr angezeigt werden. Dies ermöglicht es Ihnen, unerwünschte Funktionen auszublenden, beispielsweise wenn Sie bereits eine eigene Lageplan-Karte haben und Endnutzer auf diese weiterleiten möchten. Das Deaktivieren einzelner Funktionen kann in der entsprechenden Konfiguration der Funktionen im Backend angepasst werden. Ein weiterer Anwendungsfall könnte sein, dass Sie auf besondere Ereignisse oder Informationen hinweisen möchten, wie zum Beispiel einen Instagram-Kanal oder eine Umfrage.

Hinzufügen eigener Menüeinträge:
--------------------------------

Um eigene Menüeinträge hinzuzufügen, besuchen Sie: https://<ROCKET_MEALS_INSTANZ>/api/admin/content/wikis
Dort können Sie bestehende Wikis bearbeiten oder ein neues Wiki erstellen.

Jedes Wiki-Element enthält folgende Informationen, die Sie nach Belieben festlegen können:

- **Icon**: Wählen Sie eines der angezeigten Icons aus.
  - Wir verwenden die von der installierten Directus-Version unterstützten Icons: https://docs.directus.io/user-guide/overview/glossary.html#icons
    - Diese sind Material Icons (https://fonts.google.com/icons)
      - Auf dem Endgerät (nicht im Backend) ist die entsprechende Schriftart bereits heruntergeladen, um Datenschutzgründen zu entsprechen.
    - Social Icons: Font Awesome 5 Brand Icons (https://fontawesome.com/v5.15/icons?d=gallery&s=brands)
      - Auf dem Endgerät (nicht im Backend) ist die entsprechende Schriftart bereits heruntergeladen, um Datenschutzgründen zu entsprechen.
    - In einigen Fällen kann es aufgrund von Versionsunterschieden vorkommen, dass einzelne Icons nicht korrekt angezeigt werden. Wenn Sie ein Problem bemerken, kontaktieren Sie uns bitte. Wir bemühen uns, alle Icons sowohl im Web als auch auf den nativen Endgeräten korrekt anzuzeigen.

- **Private Note**: Eine Notiz für Ihre eigenen Zwecke. Diese Information kann über die API öffentlich gelesen werden. Als privat ist hier gemeint, dass Endnutzer diese Information nicht sehen können.
- **Parent**: Wenn Sie verschachtelte Menüs verwenden möchten, können Sie hier das übergeordnete Menü angeben.
- **Public**: Eine Checkbox, die bestimmt, ob jeder dieses Menü sehen darf, auch wenn er die Rocket Meals Software nur besucht, ohne anonym oder mit einem Konto fortzufahren.
- **Hide as Normal Wiki**: Mit dieser Option können Sie bestimmte Wiki-Einträge aus dem Menü ausblenden. Wir können diese Menüs verwenden, um sie an anderer Stelle zu implementieren.
- **Custom ID**: Ein eigener Bezeichner, mit dem Ihr Wiki-Eintrag gesondert erkannt werden kann. Wir verwenden diesen Eintrag, um das Impressum, den Datenschutz usw. zu kennzeichnen. Unzulässige Werte für neue Wiki-Einträge und von uns reservierte Bezeichner sind: "about_us", "license", "privacy_policy", "cookieComponentConsent", "cookieComponentAbout".
- **Role**: Nur Nutzer mit der entsprechenden Rolle dürfen dieses Menü sehen.
- **Title**: Der Titel des Menüs in der Seitenleiste und wenn es aufgerufen wird.
- **Content**: Der Inhalt im Menü, der für den Endnutzer angezeigt wird. Dies ist ein Markdown-Feld, sodass Sie auch Formatierungsoptionen nutzen können. Die Darstellung im Backend kann von der Darstellung auf den Endgeräten leicht abweichen, daher sollten Sie dies überprüfen.
- **URL**: Wenn Sie den Nutzer zu einem Link weiterleiten möchten, können Sie hier die neue URL eingeben. Dies kann nützlich sein, wenn Sie beispielsweise einen Link zu Ihrer Umfrage öffnen lassen möchten.

- **Children**: Diese Felder müssen Sie nicht ausfüllen.
- **Be Source for Translation**: Ob die angezeigte Sprache als Ausgangssprache verwendet werden soll (nur verfügbar, wenn die automatische Übersetzungsfunktion aktiviert ist). In diesem Fall sollten Sie bei den anderen Sprachen diese Option deaktivieren, wenn Sie die Ausgangssprache ändern möchten.
- **Let Be Translated**: Ob die angezeigte Sprache automatisch übersetzt werden soll (nur verfügbar, wenn die automatische Übersetzungsfunktion aktiviert ist).
- **Create Translations for All Languages**: Ob für alle Sprachen eine Übersetzung erstellt werden soll (nur verfügbar, wenn die automatische Übersetzungsfunktion aktiviert ist).
