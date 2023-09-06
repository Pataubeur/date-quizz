<script setup lang="ts">

import {store} from "../store.ts";
</script>

<template>
  <div class="flex justify-center items-center h-screen text-center">
    <div class="space-x-4">
      <h1 class="text-5xl mb-7 text-black-500 font-bold">
        Score final : {{ store.score }}
      </h1>
      <div class="justify-center flex items-center">
        <router-link to="/"><button class="btn">Retour au menu</button></router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>