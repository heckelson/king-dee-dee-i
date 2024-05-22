<template>
  <div class="column items-center">
    <q-circular-progress
      rounded
      :value="getRiskScore(riskValue_percent) * 10"
      size="90px"
      :thickness="0.2"
      :color="getColor(riskValue_percent)"
      track-color="transparent"
      class="q-ma-md"
      show-value
    >
      {{ getRiskScore(riskValue_percent) }}
    </q-circular-progress>
    <div class="text-uppercase text-h6">Risk Score</div>
  </div>
</template>

<script setup>
const number = 12;
const riskValue_percent = 88;

const getColor = (riskValue_percent) => {
  if (riskValue_percent < 25) {
    return "green";
  } else if (riskValue_percent < 50) {
    return "amber";
  } else if (riskValue_percent < 75) {
    return "orange";
  } else {
    return "red";
  }
};

const getRiskScore = (riskValue_percent) => {
  return Math.max(1, Math.round(riskValue_percent / 10));
};
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
