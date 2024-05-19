<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <div class="container text-center">
          <img src="./assets/dedede.png" alt="" />
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
</template>

<script>
import MedicationPicker from "./components/MedicationPicker.vue";
import RiskScore from "./components/RiskScore.vue";
import KnownInteractions from "./components/KnownInteractions.vue";

export default {
  name: "App",
  components: {
    MedicationPicker,
    RiskScore,
    KnownInteractions,
  },
};
</script>

<style>
@import "bootstrap";

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
