# Steganographie

### Funktionsweise (kurz)
- **Einbettung:** Cover-Bild + geheime Datei → Stego-Bild.  
- **Extraktion:** Stego-Bild → geheime Datei wird wiederhergestellt (ggf. Passwort nötig).  
- Von außen sieht das Stego-Bild fast identisch aus.

---

## 2. Grundlagen der Steganographie
- Ziel: **Nachricht verstecken**, sodass niemand merkt, dass kommuniziert wird.  
- Typische Träger: Bilder, Audio, Video, Text, Netzwerkpakete.  
- Häufigste Methode: **LSB-Verfahren** → niederwertige Bits in Pixeln werden minimal verändert.

---

## 3. Erkennungsmethoden (Steganalyse)
- **Visuelle Analyse:** Auffälligkeiten im Bild (Artefakte, Rauschen) bei großer Vergrößerung.  
- **Statistische Analyse:** Tests auf ungewöhnliche Bitmuster oder Pixelverteilungen (z. B. Chi-Quadrat, RS-Analyse).  
- **Vergleich mit Originalbild:** Unterschiede sichtbar.  
- **Machine Learning:** Trainingsmodelle erkennen typische Muster versteckter Daten.

---

## 4. Vorteile / Nachteile

### Vorteile
- Unauffällige Kommunikation (anders als reine Kryptographie).  
- Kann zusätzlich mit Verschlüsselung kombiniert werden.  
- Funktioniert mit vielen Dateiarten.

### Nachteile
- Begrenzte Datenmenge einbettbar.  
- Bearbeitung/Komprimierung zerstört oft die versteckten Daten.  
- Moderne Analyseverfahren können einfache Methoden leicht erkennen.  
- Gute, schwer erkennbare Verfahren sind technisch aufwendig.

---
