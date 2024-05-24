<template>
  <q-page class="page">
    <div class="column q-gutter-xl items-center">
      <div class="appTitle">
        <q-img
          src="src/assets/pill_dedede.png"
          style="height: 100px"
          fit="contain"
        />
        <div class="text-h4 appTitleHeader">Dedede's Medication Picker</div>
      </div>
      <MedicationPicker />
      <div class="row justify-center">
        <MedicationList />
        <RiskScore class="riskScore" />
      </div>
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

.appTitle {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 48px;
}

.appTitleHeader {
  font-weight: 700;
  min-width: 300px;
}

.riskScore {
  padding-left: 48px;
}
</style>
