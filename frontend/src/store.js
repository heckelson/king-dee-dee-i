import { defineStore } from "pinia";

export const useMedStore = defineStore("medStore", {
  state: () => ({
    selectedMeds: [],
  }),
  getters: {
    meds: (state) => state.selectedMeds,
  },
  actions: {
    addMedication(medication) {
      if (this.$state.selectedMeds.indexOf(medication) === -1) {
        this.$state.selectedMeds.push(medication);
        this.$state.selectedMeds.sort();
      }
    },
    removeMedication(medication) {
      this.$state.selectedMeds = this.$state.selectedMeds.filter(
        (elem) => elem !== medication,
      );
    },
    clearAllSelectedMeds() {
      this.$state.selectedMeds = [];
    },
  },
});
