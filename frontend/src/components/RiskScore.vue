<template>
  <div class="column items-center">
    <q-circular-progress
      rounded
      :value="getRiskScore(riskValue_percent) * 10"
      size="90px"
      :thickness="0.2"
      :color="color"
      track-color="transparent"
      class="q-ma-md"
      show-value
      :indeterminate="isLoading"
    >
      <div v-if="!isLoading">{{ getRiskScore(riskValue_percent) }}</div>
      <!-- <q-skeleton v-if="isLoading" type="rect" width="1em" /> -->
    </q-circular-progress>
    <div class="text-uppercase text-h6">{{ `${isLoading ? "Calculating ..." : "Risk score "}` }}</div>
  </div>
</template>

<script setup>
import { useMedStore } from "src/stores/store";
import { computed, watch } from "vue";

const riskValue_percent = 0;
const medStore = useMedStore();
const isLoading = computed(() => medStore.isLoading);

const color = computed(() => {
  if (isLoading.value === true) {
    return "grey";
  }
  if (riskValue_percent < 25) {
    return "green";
  } else if (riskValue_percent < 50) {
    return "amber";
  } else if (riskValue_percent < 75) {
    return "orange";
  } else {
    return "red";
  }
});

const getRiskScore = (riskValue_percent) => {
  return Math.max(1, Math.round(riskValue_percent / 10));
};

watch(
  medStore.interactions,
  () => {
    console.log("Selected meds changed", interactions);
    riskValue_percent = Math.min(100, (searchResults * 100) / 500);
  },
  { deep: true }
);
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
