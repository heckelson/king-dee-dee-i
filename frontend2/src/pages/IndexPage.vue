<template>
  <q-page class="flex flex-center">
    <div class="container">
      <div class="row">
        <div class="col">
          <div class="container text-center">
            <img src="src/assets/dedede.png" alt="" />
          </div>

          <MedicationPicker class="card" />
        </div>
      </div>

      <div class="row">
        <div class="col-sm-4">
          <RiskScore class="card" />
        </div>
        <div class="col-sm-8">
          <KnownInteractions class="card" />
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import MedicationPicker from "src/components/MedicationPicker.vue";
import RiskScore from "src/components/RiskScore.vue";
import KnownInteractions from "src/components/KnownInteractions.vue";

export default defineComponent({
  name: "IndexPage",
  components: {
    MedicationPicker,
    RiskScore,
    KnownInteractions,
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
