import { defineStore } from "pinia";
import { SERVER_URL } from "src/constants";

export const useMedStore = defineStore("medStore", {
  state: () => ({
    selectedMeds: [],
    interactions: {},
    isLoading: false,
  }),
  getters: {
    // meds: (state) => state.selectedMeds,
  },
  actions: {
    addMedication(medication) {
      if (this.$state.selectedMeds.indexOf(medication) === -1) {
        this.$state.selectedMeds.push(medication);
        this.$state.selectedMeds.sort();
      }
      this.fetchInteractions(this.$state.selectedMeds);
    },

    removeMedication(medication) {
      const other_meds = this.$state.selectedMeds.filter(
        (elem) => elem !== medication,
      );

      this.$state.selectedMeds = other_meds;
      this.$state.selectedMeds.sort();

      this.fetchInteractions(this.$state.selectedMeds);
    },

    clearAllSelectedMeds() {
      this.$state.selectedMeds = [];
      this.fetchInteractions(this.$state.selectedMeds);
    },

    fetchInteractions(selectedMeds) {
      const encodedSelection = encodeURI(selectedMeds);

      if (selectedMeds?.length >= 2) {
        this.isLoading = true;
        fetch(
          `${SERVER_URL}/mock-interactions?selectedMeds=${encodedSelection}`
        )
          .then((resp) => {
            console.log(resp);
            resp.json().then((body) => {
              this.interactions = body;
              console.log(this.interactions);
            });
          })
          .catch((err) => {
            console.error(err);
          })
          .finally(() => {
            this.isLoading = false;
          });
      }
    },
  },
});
