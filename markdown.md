Projectopdracht python development Klaas Mouws : 
Voor de projectopdracht kregen wij als taak een trojan framework te maken.
De verschillende modules die ik gekozen heb om te maken zijn dan ook de aanbevolen door u.
Een keylogger, een automatische schreenshot nemer, een sniffer en een programma dat continu systeeminfo doorstuurd.


Keylogger : 
Bij de keylogger heb ik gebruik gemaakt van de pynput library.
Wanneer de keylogger opstart zal deze bij het beginnen automatisch een file aanmaken genaamd logfile met een random getal er achter.
Hier in zal de tekst dan komen te staan en automatisch naar Github worden verstuurd. Na 20 seconde zal deze stoppen met keyloggen en een nieuwe logfile aanmaken met een ander getal.

Screenshotter : 
De automatische screenshotter neemt om de 5 seconde een screenshot en stuurt deze automatisch door naar de Github repo.
Mijn code is heel simpel, in de klasse heb ik een methode 'take_screen' en een methode 'auto_screen' die de methode take screen met een 
scheduler automatisch om de 5 seconde uitvoert.
Voor deze methode heb ik gewerkt met ImageGrab en elke screenshot krijgt de naam screenshot-[de tijd waar de screenshot is op genomen]

Sniffer : 
De sniffer heb ik gemaakt met de scapy library.
Wanneer de sniffer wordt opgestart zal deze een bestand maken genaamd snifferlog-en een random getal en zal er in dit bestand
20 lijnen worden gesnift en dan automatisch worden doorgestuurd naar github. Dan zal er een nieuw bestand worden gemaakt en daar verder in worden gegaan.

Sysinfo : 
De sysinfo module haalt informatie op over het geheugen, hoeveel geheugen er wordt gebruik etc...
Deze wordt weergegeven in een grafiek, de grafiek zal in een bestand worden gezet genaamd memorylog-random getal en ook automatisch naar github worden gestuurd

Main : 
In de main roep alle verschillende modules aan en worden ze allemaal om de 20 seconde afgespeeld door een theading


Moeilijkheden:
Ik probeerde de commando's uitgelezen te laten worden uit een command.json file maar dit kreeg ik maar niet aan de praat. 
Ook waar ik grote problemen bij had was dat ik mijn modules om de 30 seconde wou laten afspelen maar telkens wanneer mijn programma in de module ging kwam deze er niet meer uit zeg maar.
Dit heb ik ook in elke module appart proberen aanpassen zonder succes.
Hier heb ik echt gigantisch lang aan gewerkt om dit op te lossen maar dit is niet gelukt.
Uiteindelijk heb ik het dan ongeveer opgelost met behulpt van een threading.


