<!--
  Project Name: GDP- Gathering Detection Platform
  File Name: aboutUs.vue
  Author: Margherita Mitillo
  Creation Date: 2021-03-25
  Summary: the file is the page "about us" of the webapp with all the information about us, synclab and the webapp.
  Last change date: 2021-03-31
-->

<template>
  <div id="chiSiamo">
    <h2>Il gruppo</h2>
    <p>
      Il gruppo Jawa Druids è composto da sette studenti dell'università di
      studio di Padova del corso di laurea triennale di Informatica.
    </p>
    <h2>L'azienda</h2>
    <p>
      Sync Lab nasce come Software house tramutatasi rapidamente in System
      Integrator attraverso un processo di maturazione delle competenze
      tecnologiche, metodologiche ed applicative nel dominio del software.
      L'azienda, propone sul mercato interessanti quanto innovativi prodotti
      software, nati nel nostro laboratorio di ricerca e sviluppo. Attraverso
      questi prodotti. Sync Lab ha gradualmente conquistato significativamente
      fette di mercato nei seguenti settori: mobile, videosorveglianza e
      sicurezza delle infrastrutture informatiche aziendali.
    </p>
    <h2>GDP</h2>
    <p>
      GDP è un sito creato con lo scopo di poter visualizzare e predirre il
      rischio assembramento nelle città in modo tale da garantire la sicurezza a
      tutti i cittadni. Il sito deve essere a disposizione degli utenti
      amministrativi come i dipendenti delle sedi comunali. Grazie a questa web
      application si potranno organizzare eventi in sicurezza riuscendo a
      predirre quante persone saranno presenti.
    </p>
    <ul id="loghi">
      <li id="synclab">
        <img src="../assets/synclab.png" alt="Sync Lab" />
      </li>
      <li>
        <img src="../assets/DRUIDSLOGO.jpg" alt="Jawa Druids" />
      </li>
      <li class="unipd"><img src="../assets/unipd.png" alt="Unipd" /></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "chiSiamo",
};
</script>

<style scoped>
#chiSiamo {
  padding-left: 8%;
  padding-top: 5%;
  padding-right: 8%;
}
#chiSiamo ul {
  display: flex;
  list-style-type: none;
  align-items: center;
}
/* #chiSiamo #loghi li {
  padding-left: 3%;
  padding-right: 3%;
}
#chiSiamo #synclab {
  padding-top: 9%;
  padding-bottom: 5%;
} */

img {
  max-width: 200px;
  max-height: 200px;
  width: 100%;
  height: 100%;
  margin: auto;
}



/* .unipd {
  width: 800%;
  height: 80%;;
}  */
/* #loghi {
  text-align: center;
} */
</style>
