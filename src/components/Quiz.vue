<script setup lang="ts">
  import {ref} from "vue";
  import date from "../assets/date.json"
  import {store} from "../store.ts";
  import router from "../router.ts";

  const checked = ref(false)
  const answer = ref('')
  let date_asked = date.dates[Math.floor(Math.random()*date.dates.length-1)]
  let good_answer = false
  let question_number = 1
  const question_limit = 15
  let questions_asked : string[] = []
  questions_asked.push(date_asked['event'])
  store.score = 0

  function submit() {
    checked.value = true
    let date_good_answer = ''
    if(date_asked['year'].includes('(')) {
      date_good_answer = date_asked['year'].split('(')[0]
    } else {
      date_good_answer = date_asked['year']
    }
    good_answer = date_good_answer === (answer.value);
    store.score = store.score + calculateScore(+date_good_answer, +answer.value)
    setTimeout(() => {
      focusNext();
    }, 20);
  }

  function next() {
    question_number++
    date_asked = date.dates[Math.floor(Math.random()*date.dates.length-1)]
    for (let i = 0; i < questions_asked.length ; i++) {
      if(date_asked['event'] === questions_asked[i]) {
        date_asked = date.dates[Math.floor(Math.random()*date.dates.length-1)]
        i = 0
      }
    }
    questions_asked.push(date_asked['event'])
    checked.value = false
    answer.value = ''
    if(question_number == question_limit+1) {
      router.push('/score')
    }
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

  function calculateScore(good_answer: number, answer_value: number) {
    console.log(good_answer)
    console.log(answer_value)
    let question_score = 0
    const difference = Math.abs(good_answer - answer_value)
    console.log(difference)
    if(difference > 100) {
      question_score = 0
    } else {
      question_score = 100 - difference
    }
    console.log(question_score)
    return question_score
  }

</script>

<template>
  <div class="flex justify-center items-center h-screen text-center">
    <div v-if="!checked" class="space-x-4">
      <h1 class="text-2xl mb-7 text-black-500">
        Question : {{ question_number }} / {{ question_limit }}
      </h1>
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
        <h1 class="text-2xl mb-7 text-black-500">
          Question : {{ question_number }} / {{ question_limit }}
        </h1>
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
        <h1 class="text-2xl mb-7 text-black-500">
          Question : {{ question_number }} / {{ question_limit }}
        </h1>
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
    <span class="absolute bottom-10 right-10 text-4xl">
      Score : {{ store.score }}
    </span>
  </div>
</template>

<style scoped>

</style>