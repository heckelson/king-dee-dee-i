<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <MedicationPicker />
      </div>
    </div>

    <div class="row">
      <div class="col-sm-4">
        <RiskScore />
      </div>
      <div class="col-sm-8">
        <KnownInteractions />
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

div {
  border: 1px solid red;
}
</style>
