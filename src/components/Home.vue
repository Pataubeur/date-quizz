<script setup lang="ts">

</script>

<template>
  <div class="justify-center flex flex-col items-center h-screen text-center">
    <div class="justify-center flex items-center mb-5">
      <img class="w-20" src="../assets/book_red.svg" />
      <h1 class="text-5xl mb-2 text-black-500 font-bold">
        Quiz d'Hérodote
      </h1>
    </div>
    <div>
      <router-link to="/quiz"><button class="btn">Commencer le quiz</button></router-link>
    </div>
  </div>
</template>

<style scoped>

</style>