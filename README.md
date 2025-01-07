# NessiTest

_NessiTest_ è un'applicazione per la creazione di questionari personalizzati, sviluppata in Python e fornita sia come script Python (NessiTest.py) che come file eseguibile (NessiTest.exe). L'app permette di creare questionari interattivi e di esportarli in formato HTML.

## Caratteristiche principali

### Creazione di Questionari

- Inserimento di un titolo e un footer opzionale.
- Aggiunta di domande con più opzioni di risposta, specificando quelle corrette.
- Modifica e gestione delle domande salvate.

### Esportazione in HTML
- Generazione di file HTML interattivi con risposte corrette evidenziate.
- Calcolo del punteggio finale tramite pulsanti interattivi.

### Compatibilità
- Eseguibile autonomo per ambienti Windows (NessiTest.exe).
- Script Python per utenti con configurazione Python installata.


### Istruzioni per l'uso

#### 1. Utilizzo del file .exe
Il file eseguibile NessiTest.exe è progettato per gli utenti che desiderano eseguire il programma senza necessità di installare Python.

**Passaggi**
1. Scaricare il file
Copiare o scaricare il file NessiTest.exe sul proprio computer.

2. Eseguire il programma:
Fare doppio clic su NessiTest.exe per avviare l'app.
Non sono necessarie ulteriori configurazioni.

3. Interfaccia utente
- Seguire i passaggi indicati per creare il questionario (vedi sezione "Uso dell'interfaccia").
- Salvare il file HTML tramite la funzione di esportazione.

#### 2. Utilizzo dello script Python

Se si preferisce lavorare con il codice sorgente, utilizzare il file NessiTest.py.

**Requisiti**

Python 3.x: Deve essere installato sul sistema.
Libreria Tkinter: Inclusa nella maggior parte delle distribuzioni Python.

**Passaggi**

1. Aprire un terminale o un prompt dei comandi.
2. Spostarsi nella directory contenente NessiTest.py.
Eseguire il comando:
```
python NessiTest.py
```
Seguire le istruzioni a schermo.

## Uso dell'interfaccia
L'interfaccia del programma (identica per il file .exe e lo script Python) è organizzata in più sezioni:

1. Titolo e Footer:

- Inserire il titolo del questionario.
- (Facoltativo) Aggiungere un footer, come una firma o una nota.

2. Domanda e Opzioni:
- Inserire il testo della domanda.
- Aggiungere opzioni di risposta tramite il pulsante "Aggiungi opzione".
- Selezionare le opzioni corrette utilizzando le checkbox accanto ad esse.

3. Gestione delle domande:
- Salvare la domanda per aggiungerla alla lista.
- Selezionare una domanda dalla lista per modificarla.

4. Esportazione HTML:

- Generare un file HTML interattivo con il pulsante "Genera HTML".
- Salvare il file tramite la finestra di dialogo.

## File HTML generato

Il file HTML generato presenta:
- Design chiaro e leggibile con uno stile CSS integrato.
- Funzionalità interattive tramite JavaScript per:
-- Verificare le risposte.
-- Evidenziare risposte corrette e sbagliate.
-- Calcolare il punteggio totale.

## Domande Frequenti

1. È necessario Python per utilizzare il programma?
- No, se utilizzi il file .exe.
- Sì, se preferisci lavorare con lo script Python (NessiTest.py).

2. Posso eseguire il programma su macOS o Linux?
- Il file .exe è progettato per Windows.
- Lo script Python è compatibile con tutti i sistemi operativi che supportano Python.

3. Dove vengono salvati i questionari?
- I file HTML generati vengono salvati nella posizione selezionata durante l'esportazione.

## Download

[Visita il repository su GitHub](https://github.com/antonio-vigilante/nessitest)
