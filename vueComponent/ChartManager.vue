<template>
  <div class="container">
    <button  @click="titi() " >
  
  évolution masse salariale globale dans le temps
  </button>
      <h3 class="green">
        Choisir un graphique sur l'ensemble des données : 
      </h3>
      <v-btn>
        <button  @click="titi() " >
  
          évolution masse salariale globale dans le temps
        </button>
      </v-btn>
      <button  @click="titi() " >
  
  évolution masse salariale globale dans le temps
  </button>
  
    <div id="progressCols" class="container" v-if="showGlobalEmployeesNumberOverMonths===false">
      <p>TOTO</p>
    </div>
  
  
      <h3>
        Rechercher un utilisateur pour avoir les graphiques le concernant : 
      <br>
        <input
    :value="text"
    @input="event => text = event.target.value">
    <br>
    <v-btn>
      <button @click="searchInput=text; test(text)">Chercher</button>
  </v-btn>
    
  
        
      </h3>
    </div>
    </template>
    
    <style scoped>
  h1 {
    font-weight: 500;
    font-size: 2.6rem;
    position: relative;
    top: -10%;
  }
  
  input{
    width: 60px;
    height: 40px;
  }
  h3 {
    font-size: 1rem;
  }
  
  .greetings h1,
  .container {
    text-align: center;
  }
  
  @media (min-width: 1024px) {
    .greetings h1,
    .greetings h3 {
      text-align: left;
    }
  }
    </style>
    
    <script setup>
  
  import { getAllUsers } from '@/repository/apiRequests';
  
  
     getAllUsers().then(data => {
      console.log("traitement de la promesse coté composant utilisateur", data)
  })
  
    var text = "";
    var searchInput = "";
    var showGlobalEmployeesNumberOverMonths = false;
  
  
  function test (text) {
      searchInput = text;
      console.log(searchInput);
    }
  
    function titi () {
      showGlobalEmployeesNumberOverMonths=!showGlobalEmployeesNumberOverMonths;
      console.log(showGlobalEmployeesNumberOverMonths);
  
    }
    
    </script>
    