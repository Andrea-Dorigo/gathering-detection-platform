# Gathering Detection Platform

Un software in grado di mostrare il flusso di persone in tempo reale in un determinato luogo e di prevederne l'evoluzione tramite Machine Learning.
Il progetto e' ancora in via di sviluppo e pertanto puo' essere incompleto o inaccurato.

# Introduzione

Il software e' suddiviso in 3 parti:

1. acquisizione dati:
  + un back-end scritto in python scarica un video da un url di una webcam online, estrapola un frame e utilizza OpenCv e YOLOv3 per contare il numero di persone ivi presenti
2. predizione dati:
  + utilizzando Anacoda e Sci-kit Learn utilizziamo i dati raccolti nel database per creare un modello di Machine Learning capace di fornire una previsione sull'andamento del flusso di persone nelle prossime ore
3. applicazione web:
  + un'applicazione web scritta in Java e Vue.js rappresenta i dati in una heatmap tramite il framework leaflet.js


# Dipendenze

+ Python3
+ MongoDB
+ Opencv2
+ Anaconda
+ Sci-kit Learn
+ Python3
+ Java
+ Vue.js
