# StudiService-3000-
Dokumentation von Jan Mehr, Raphael, Leander Mitsch 

Studentendatenbank mit SQLite 

## Projektübersicht 
Die entwickelte Anwendung ist ein einfaches Verwaltungssystem für Studierende und Kurse mit Anbindung an eine SQLite-Datenbank. Ziel ist es, die Verwaltung von Studierenden, Kursen und deren Einschreibungen zu ermöglichen. Die Anwendung bietet alle grundlegenden CRUD-Funktionen (Hinzufügen, Bearbeiten, Löschen, Anzeigen) über eine einfache Benutzeroberfläche. 

## Wichtige Module und Klassen  
**main.py**  
Startpunkt der Anwendung. Startet die Benutzeroberfläche über TKInter. Über Menüs können Studierende und Kurse verwaltet und Studierende in Kurse eingeschrieben werden.  

**Database.py**  
Enthält die Klasse Database für die Verwaltung der SQLite-Verbindung. Hier werden die Datenbanktabellen erstellt und ein Interface für CRUD-Operationen via SQL-Queries und Parameter bereitgestellt. Die Klasse wurde als Singleton entworfen, um Mehrfachzugriffe auf dieselbe Datenbank zu ermöglichen und Race-Conditions zu vermeiden 
### Models:  
**Studierender.py**  
Enthält die Klasse Studierender. Diese ist der Bauplan für ein Studentenobjekt und gibt an welche Methoden und Attribute in ihr enthalten sind. 

**Kurs.py**   
Beinhaltet die Klasse Kurs. Diese ist der Bauplan für ein Kursobjekt und gibt an welche Methoden und Attribute in ihr enthalten sind. 

### Service: 
**StudierendeService.py**   
Die Klasse StudierendeService verwaltet alle Datenbankoperationen für Studierende. Sie stellt Methoden bereit, um Studierende in der Datenbank zu erstellen, zu aktualisieren, zu löschen, zu suchen und einzuschreiben. Zudem bietet es die Methoden für das Einschreiben und Löschen der Studenten in oder aus Kursen. 

**KursService.py**  
Die Klasse KursService kümmert sich um die Verwaltung der Kursdatenbankeinträge. Sie stellt Methoden bereit, um Kurse in der Datenbank zu erstellen, zu aktualisieren, zu löschen und abzurufen. 

### GUI 
**MainMenuFrame.py, KursListFrame.py, StudentListFrame.py**   
Diese Klassen verwalten die verschiedenen Fenster der GUI, erstellen darin UI-Elemente und verknüpfen Methodenaufrufe mit diesen Elementen, um die Benutzerführung zu ermöglichen. 

**widgets.py**   
Hier werden einige TKInter Elemente, welche häufiger in der GUI vorkommen oder etwas komplexer sind, mittels Klassen überschrieben und auf die jeweiligen Anforderungen angepasst. 

## Tabellenübersicht 

Die SQLite-Datenbank enthält folgende Tabellen: 

- **kurs**( <ins>id</ins>, kursname, dozent, semester ) 

- **studierende**( <ins>id</ins>, name, matrikelnummer, studiengang ) 

- **teilnahme**( <ins>id</ins>, kursId, studierendeId ) 

### Anleitung zur Nutzung 

1. Stellen Sie sicher, dass Python auf Ihrem Computer installiert ist. 
2. Speichern Sie alle Projektdateien im selben Ordner ab. 
3. Starten Sie die Anwendung, indem Sie main.py ausführen. 
4. Nach dem Start öffnet sich die Benutzeroberfläche. Dort können Sie auswählen, ob Sie Studierende oder Kurse verwalten möchten: 
5. Studierende anzeigen und bearbeiten 
6. Kurse anzeigen und bearbeiten 
7. Nach Ihrer Auswahl gelangen Sie zum jeweiligen Übersichtsbildschirm: 
8. Unter Aktionen können Sie einen neuen Studierenden oder Kurs anlegen. 
9. Unter Aktionen ist ein CSV Export mit dem gleichnamigen Button möglich. 
10. Mit Speichern wird der neue Eintrag in der Datenbank gespeichert. 
11. In der Übersichtstabelle sehen Sie alle vorhandenen Studierenden bzw. Kurse. 
12. Jeder Eintrag hat die Optionen Bearbeiten (um Daten zu ändern) und Löschen (um den Datensatz zu entfernen). 
13. In der Benutzeroberfläche der Studierenden und der Option Bearbeiten kann man zudem den jeweiligen Studenten zu einem oder mehreren Kursen, über eine Zwischentabelle, hinzufügen 
14. Um zurück zum Hauptmenü zu gelangen, klicken Sie auf die Zurück-Taste oben links in der Anwendung. 

### Hinweise zur Einrichtung der Datenbank 

- Die SQLite-Datenbank (database.db) wird automatisch beim ersten Programmstart erstellt. 
- SQLite ist in Python enthalten, es ist keine separate Installation erforderlich. 
- Sicherstellen, dass Schreibrechte im Projektordner vorhanden sind. 
- Testdaten können über das GUI angelegt werden 