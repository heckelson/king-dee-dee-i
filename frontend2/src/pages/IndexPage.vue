<template>
  <q-page class="page flex flex-center">
    <div class="column q-gutter-md">
      <MedicationPicker />
      <MedicationList></MedicationList>
      <RiskScore />
      <KnownInteractions />
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

<style scoped>
.page {
  padding: 22px;
}
</style>
