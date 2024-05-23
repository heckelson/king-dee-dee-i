import { defineStore } from "pinia";

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
    },
    removeMedication(medication) {
      const other_meds = this.$state.selectedMeds.filter(
        (elem) => elem !== medication,
      );

      this.$state.selectedMeds = other_meds;
      this.$state.selectedMeds.sort();
    },
    clearAllSelectedMeds() {
      this.$state.selectedMeds = [];
    },
    setInteractions(interactions) {
      console.log("setting interactions", interactions);
      this.$state.interactions = interactions;
    },
    fetchInteractions(selectedMeds) {
      const encodedSelection = encodeURI(selectedMeds);

      this.isLoading = true;

      if (selectedMeds?.length >= 2) {
        fetch(
          `${SERVER_URL}/mock-interactions?selectedMeds=${encodedSelection}`
        )
          .then((resp) => {
            resp.json().then((body) => {
              this.interactions = body;
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
