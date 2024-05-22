<template>
  <q-page class="flex flex-center">
    <div class="container">
      <div class="row">
        <div class="col">
          <MedicationPicker class="card" />
        </div>
      </div>

      <MedicationList></MedicationList>

      <KnownInteractions class="card" />
    </div>

    <q-dialog v-model="isPopupShown" seamless position="bottom">
      <q-card>
        <q-card-section class="row items-center no-wrap">
          <RiskScore class="card" />
        </q-card-section>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";
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
    const isPopupShown = ref(true);

    return {
      isPopupShown,
    };
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
