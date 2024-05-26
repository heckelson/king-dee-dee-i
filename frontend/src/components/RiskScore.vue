<template>
  <div class="column items-center">
    <q-circular-progress
      rounded
      :value="riskScore_Likert * 10"
      size="90px"
      :thickness="0.2"
      :color="color"
      track-color="transparent"
      class="q-ma-md"
      show-value
      :indeterminate="isLoading"
    >
      <div v-if="!isLoading">{{ riskScore_Likert }}</div>
      <!-- <q-skeleton v-if="isLoading" type="rect" width="1em" /> -->
    </q-circular-progress>
    <div class="text-uppercase text-h6">Risk Score</div>
  </div>
</template>

<script setup>
import { useMedStore } from "src/stores/store";
import { computed, watch } from "vue";

const medStore = useMedStore();
const isLoading = computed(() => medStore.isLoading);

const color = computed(() => {
  if (isLoading.value === true) {
    return "grey";
  }
  if (riskValue_percent.value < 25) {
    return "green";
  } else if (riskValue_percent.value < 50) {
    return "amber";
  } else if (riskValue_percent.value < 75) {
    return "orange";
  } else {
    return "red";
  }
});

const riskValue_percent = computed(() => {
  if ((medStore.interactions.searchResults?.length ?? 0) <= 1) return 0;
  const frequencies = medStore.interactions.searchResults.map((result) => {
    const frequency = parseFloat(result.mean_reporting_frequency);
    return frequency;
  });
  console.log("frequencies", frequencies);
  const maxFrequency =
    frequencies.length === 0
      ? 0
      : Math.max(
          ...frequencies.filter((f) => typeof f === "number" && isFinite(f))
        );
  return Math.min(100, (maxFrequency * 100) / 0.11);
});

const riskScore_Likert = computed(() => {
  return Math.max(1, Math.round(riskValue_percent.value / 10));
});
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
