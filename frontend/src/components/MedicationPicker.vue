<template>
  <div class="container text-center">
    <div class="col">
      <img src="../assets/dedede.png" class="" />
      <h1 class="h1">Medication Picker</h1>

      <div class="container">
        <p>Table</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useMedStore } from "../store.js";
const store = useMedStore();

store;
</script>

<style></style>
