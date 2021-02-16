# Todo

## Schema

1. ### Modulo 1:
 - Titolo: getFrame
 - Input: webcam_url
 - Output: singolo Frame in formato .jpg
 - Linguaggio: Java
 - Descrizione:
    1. riceve in input un url di una file .ts online (formato video dello stream);
    2. prende l'url e salva il file .ts;
    3. esporta il primo frame
    4. se necessario, ritaglia l'immagine in parti piu' piccole, pronte per essere passate al prossimo modulo
2. ### Modulo 2:
 - Titolo: countPeople
 - Input: Frame in formato .jpg
 - Output: Numero di persone presenti
 - Linguaggi: Java, python, shell
 - Descrizione:
    1. [optional] ritaglia l'immagine in parti piu' piccole chiamate partial
    2. conta il numero di persone tramite darknet yolov3
    3. [optional] se il frame e' stato ritagliato, somma il numero di persone dato dai partial
    4. restituisce il numero di totale di persone del frame
3. ### Modulo 3:
 - Titolo: streamDB
 - Input: Numero di persone in un determinato luogo e momento
 - Output: Varie possibili Query
 - Linguaggi: Java, no-Sql
 - Descrizione: programma in java che deve inserire e prelevare i dati dal mongoDB (da strutturare). Deve possedere delle funzioni che interrogano il DB e ritornano il dato.
4. ### Modulo 4:
 - Titolo: predict
 - Input: Dati dal DB
 - Output: Dato con la stima futura del numero di persone
 - Linguaggio: Java, python, ?
 - Descrizione:
    1. riceve i dati necessari dal streamDB
    2. training, elaborazione - modello ML
    3. restituisce i dati della previsione
5. ### Modulo 5:
 - Titolo: webApp
 - Input: Dati dal DB
 - Output: Heatmap
 - Linguaggi/framework: Java, vue.js, Javascript, Leaflet, HTML, Css e chi piu' ne ha piu' ne metta
 - Descrizione:
    1. riceve i dati necessari da streamDB
    2. utilizza i dati per generare le mappe tramite leaflet
    3. mostra l'interfaccia grafica all'utente, con la visualizzazione della mappa.
