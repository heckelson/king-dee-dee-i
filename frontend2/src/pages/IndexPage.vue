<template>
  <q-page class="flex flex-center">
    <div class="container">
      <MedicationPicker class="card" />

      <MedicationList></MedicationList>

      <KnownInteractions class="card" />
      <RiskScore class="card" />
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import MedicationPicker from "src/components/MedicationPicker.vue";
import RiskScore from "src/components/RiskScore.vue";
import KnownInteractions from "src/components/KnownInteractions.vue";
import MedicationList from "src/components/MedicationList.vue";

export default defineComponent({
  name: "IndexPage",
  components: {
    MedicationPicker,
    MedicationList,
    RiskScore,
    KnownInteractions,
  },
  setup() {
    return {};
  },
});
</script>

<style>
* {
  box-sizing: border-box;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.card {
  margin-top: 12px;
}
</style>
