<template>
  <div class="text-center">
    Risk Score
    <div id="risk-score" class="container container-sm">{{ number }}</div>
  </div>
</template>

<script setup>
const number = 12;
</script>

<style>
#risk-score {
  max-width: 80px;
  height: 80px;
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;

  color: var("color");
}
</style>
