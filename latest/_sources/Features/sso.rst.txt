Single Sign-On (SSO)
=====================

Single Sign-On (SSO) ist ein Authentifizierungsverfahren, das es Benutzern ermöglicht, auf mehrere Anwendungen oder Dienste zuzugreifen, indem sie sich nur einmal anmelden. Mit SSO können Benutzer ihre Anmeldeinformationen (z.B. Benutzername und Passwort) einmal eingeben und dann auf verschiedene Dienste zugreifen, ohne sich jedes Mal erneut anmelden zu müssen.

Vorteile von SSO
----------------

1. **Benutzerfreundlichkeit**: Benutzer müssen sich nur einmal anmelden, um auf mehrere Dienste zuzugreifen, was den Anmeldeprozess vereinfacht und beschleunigt.
2. **Verbesserte Sicherheit**: Da Benutzer nur ein Passwort benötigen, können sie ein stärkeres Passwort wählen und es regelmäßig ändern, ohne sich an mehrere Passwörter erinnern zu müssen.
3. **Vereinfachtes Passwortmanagement**: IT-Abteilungen müssen weniger Passwörter verwalten und zurücksetzen, was den Verwaltungsaufwand reduziert.
4. **Schnellerer Zugriff**: Benutzer können schneller auf die benötigten Dienste zugreifen, da sie den Anmeldeprozess nicht für jede Anwendung wiederholen müssen.

Einrichtung von SSO
-------------------

Für die Einrichtung von SSO in Rocket Meals werden entsprechende Konten bei den jeweiligen Plattformen benötigt. Wir übernehmen gerne die Einrichtung von ausgewählten Plattformen als SSO-Anbieter, sofern die notwendigen Voraussetzungen von `Google <../Requirements/google_developer_account.html>`_ und `Apple <../Requirements/apple_developer_account.html>`_ erfüllt sind.

Unterstützte SSO-Mechanismen
----------------------------

Rocket Meals unterstützt vier Standardtypen von SSO-Mechanismen:

1. **OpenID**: Ein offener Standard für die Authentifizierung von Benutzern. Weitere Informationen finden Sie in der `OpenID Connect Core 1.0 Spezifikation <https://openid.net/specs/openid-connect-core-1_0.html>`_.
2. **OAuth 2.0**: Ein Protokoll, das es Anwendungen ermöglicht, auf Kontoinformationen von Benutzern zuzugreifen, ohne deren Passwort zu kennen. Weitere Informationen finden Sie im `RFC 6750 <https://www.ietf.org/rfc/rfc6750.txt>`_.
3. **LDAP**: Ein Protokoll zur Abfrage und Änderung von Verzeichnisdiensten, das häufig in Unternehmensumgebungen verwendet wird. Weitere Informationen finden Sie im `RFC 4511 <https://datatracker.ietf.org/doc/html/rfc4511>`_.
4. **SAML**: Ein XML-basiertes Framework für den Austausch von Authentifizierungs- und Autorisierungsinformationen. Weitere Informationen finden Sie im `RFC 7522 <https://datatracker.ietf.org/doc/html/rfc7522>`_.

Intern verwenden wir die SSO-Mechanismen von Directus, die in der `Directus-Dokumentation <https://docs.directus.io/self-hosted/sso.html>`_ beschrieben sind.
