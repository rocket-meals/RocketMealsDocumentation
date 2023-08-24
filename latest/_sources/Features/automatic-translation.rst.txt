Automatische Übersetzung
========================

Die Fähigkeit, mehrere Sprachen zu sprechen, ist ein wertvolles Gut, aber nicht jeder hat das Glück, mehrsprachig erzogen worden zu sein oder eine natürliche Begabung für Sprachen zu haben. Bei der Implementierung der Mehrsprachigkeitsunterstützung in Rocket Meals sind wir auf dieses Problem gestoßen. Während statische Texte (wie z.B. "Weiter") einmalig übersetzt und wiederverwendet werden können, erfordert die Übersetzung von dynamischen Inhalten, wie z.B. Speisebeschreibungen, eine andere Herangehensweise. Wenn Sie beispielsweise sechs verschiedene Gerichte anbieten, müssen bei Unterstützung von 12 Sprachen insgesamt 72 Texte übersetzt werden.

Wenn Sie diese Funktion aktiviert haben, werden standardmäßig eine Vielzahl von Texten automatisch übersetzt, darunter Speisen, Nachrichten, Beschreibungen von Gebäuden und Wohnanlagen und vieles mehr.
Die Unterstützung mehrerer Sprachen bringt natürlich auch die Herausforderung mit sich, diese Inhalte einzupflegen. Mit der automatischen Übersetzungsfunktion von Rocket Meals können Sie jedoch sicherstellen, dass Ihre Inhalte immer in mehreren Sprachen verfügbar sind, um ein breiteres Publikum anzusprechen.

Um diese Herausforderung zu bewältigen, unterstützen wir die Verwendung von `DeepL <https://www.deepl.com>`_. DeepL ist ein leistungsstarker Übersetzungsdienst, der auf maschinellem Lernen basiert und qualitativ hochwertige Übersetzungen in einer Vielzahl von Sprachen bietet. Die Kosten für die automatische Übersetzung sind an die von DeepL gekoppelt. Dank des Pro-Services von DeepL werden Ihre Daten im europäischen Raum verarbeitet und nicht von DeepL gespeichert (`DeepL Datenschutzrichtlinie <https://www.deepl.com/privacy.html>`_).

Aktivieren
---------

Um die Funktion der automatischen Übersetzung zu aktivieren, benötigen Sie einen `DeepL Pro API Account <https://www.deepl.com/de/pro/change-plan#developer>`_.

1. Richten Sie einen `DeepL Pro API Account <https://www.deepl.com/de/pro/change-plan#developer>`_ ein.
2. Folgen Sie den Anweisungen im Backend: https://<ROCKET_MEALS_INSTANZ>/api/admin/content/auto_translation_settings
    - Besuchen Sie: https://www.deepl.com/de/account/summary
    - Kopieren Sie den "Authentifizierungsschlüssel für die DeepL-API"
    - Fügen Sie den Authentifizierungsschlüssel im Backend ein
