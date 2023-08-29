<script setup lang="ts">
  import {ref} from "vue";
  import date from "../assets/date.json"

  const checked = ref(false)
  const answer = ref('')
  let date_asked = date.dates[Math.floor(Math.random()*date.dates.length-1)]
  let good_answer = false
  function submit() {
    checked.value = true
    good_answer = date_asked['year'] === (answer.value);
    setTimeout(() => {
      focusNext();
    }, 20);
  }

  function next() {
    date_asked = date.dates[Math.floor(Math.random()*date.dates.length-1)]
    checked.value = false
    answer.value = ''
    setTimeout(() => {
      focusNextInput();
    }, 20);
  }

  function focusNext(){
    let btn = document.getElementById("nextButton");
    if(btn !== null) {
      btn.focus({});
    }
  }

  function focusNextInput(){
    let input = document.getElementById("inputAnswer");
    if(input !== null) {
      input.focus({});
    }
  }

</script>

<template>
  <div class="flex justify-center items-center h-screen text-center">
    <div v-if="!checked" class="space-x-4">
      <h1 class="text-5xl mb-7 text-black-500 font-bold">
        {{ date_asked['event'] }}
      </h1>
      <div class="justify-center flex items-center">
        <input v-model="answer" @keydown.enter="submit" type="text" placeholder="Entrer une date" class="input w-full max-w-xs mr-3" id="inputAnswer"/>
        <button @click="submit" class="btn">Valider</button>
      </div>
    </div>
    <div v-else class="space-x-4">
      <div v-if="good_answer" class="space-x-4">
        <h1 class="text-5xl mb-7 text-black-500 font-bold">
          <span> {{ date_asked['event'] }} </span>
        </h1>
        <div class="justify-center flex items-center mb-10">
          <div class="w-full max-w-xs mr-3 text-3xl">
            Bonne réponse !
          </div>
          <button @click="next" class="btn" id="nextButton">Suivant</button>
        </div>
        <div class="text-5xl mr-3 text-green-600">
          <span> {{ date_asked['year'] }} </span>
        </div>
      </div>
      <div v-else class="space-x-4">
        <h1 class="text-5xl mb-7 text-black-500 font-bold">
          <span> {{ date_asked['event'] }} </span>
        </h1>
        <div class="justify-center flex items-center mb-10">
          <div class="w-full max-w-xs mr-3 text-3xl">
            Mauvaise réponse !
          </div>
          <button @click="next" class="btn" id="nextButton">Suivant</button>
        </div>
        <div class="text-5xl mr-3 text-red-600">
          <span> {{ date_asked['year'] }} </span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>