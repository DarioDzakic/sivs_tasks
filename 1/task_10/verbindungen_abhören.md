# Abhören von Verbindungen und Sicherheit im Browser

## Möglichkeiten zum Abhören unverschlüsselter Verbindungen
1. **Packet Sniffing:** Tools wie Wireshark oder tcpdump können den gesamten Datenverkehr im Netzwerk mitlesen, wenn keine Verschlüsselung verwendet wird.
2. **Man-in-the-Middle (MitM):** Ein Angreifer kann sich zwischen zwei Kommunikationspartner schalten und den Datenverkehr abfangen oder manipulieren.
3. **ARP-Spoofing:** Durch Manipulation der Adressauflösung im lokalen Netzwerk kann der Angreifer den Datenverkehr auf sich umleiten.
4. **Netzwerk-Taps:** Hardware, die direkt in die Leitung eingeschleust wird, um den Datenverkehr mitzulesen.

## Methoden zum Abhören verschlüsselter Verbindungen
1. **Man-in-the-Middle mit gefälschtem Zertifikat:** Angreifer schleusen ein eigenes Zertifikat ein, um den verschlüsselten Datenverkehr zu entschlüsseln (z.B. durch kompromittierte Root-CAs oder lokale Manipulation).
2. **SSL-Stripping:** Der Angreifer zwingt den Client, statt HTTPS nur HTTP zu verwenden, und kann so den Datenverkehr mitlesen.
3. **Schwache oder kompromittierte Verschlüsselung:** Veraltete Protokolle (z.B. SSLv2/v3) oder unsichere Cipher Suites können geknackt werden.
4. **Key-Logging oder Malware:** Angreifer greifen die Daten direkt am Endgerät ab, bevor sie verschlüsselt werden.

## Beurteilung der Aussage
„Ein geschlossenes Schloss in der Browserleiste bedeutet, dass die Verbindung sicher ist und die besuchte Domain authentisch ist.“

**Bewertung:**
- Das Schloss zeigt an, dass die Verbindung zwischen Browser und Server verschlüsselt ist (HTTPS).
- Es bedeutet jedoch nicht zwangsläufig, dass die besuchte Domain authentisch ist! Ein Angreifer kann z.B. ein gültiges Zertifikat für eine Phishing-Domain erhalten.
- Auch bei verschlüsselter Verbindung können Angriffe wie Phishing, gefälschte Zertifikate oder kompromittierte CAs auftreten.
- Nutzer sollten zusätzlich auf die korrekte Domain und Zertifikatsdetails achten.

**Fazit:**
Das Schloss ist ein Indikator für Verschlüsselung, aber kein Garant für Authentizität oder absolute Sicherheit.
