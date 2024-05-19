<template>
  <div class="container text-center">
    <div class="col">
      <img src="../assets/dedede.png" alt="" />
      <h1 class="h1">Medication Picker</h1>

      <div class="container">
        <div class="row">
          <div class="col-sm-5">
            <h3>Add Medication</h3>

            <form @submit.prevent="searchForMedication()" class="input-group">
              <input
                class="input-group-text"
                v-model="searchString"
                placeholder="Search medication"
              />
              <button class="btn btn-primary">Search</button>
            </form>

            <h4>Results</h4>
            <div id="search-results">
              <div
                class="text-start"
                v-for="result in searchResults"
                v-bind:key="result"
              >
                {{ result }}
                <button
                  class="btn btn-sm btn-primary"
                  @click="this.addMedicationToSelection(result)"
                >
                  Add
                </button>
              </div>
            </div>
          </div>

          <div class="col-sm-7">
            <h3>Selected Medications</h3>

            <button
              class="btn btn-danger"
              @click="this.clearMedicationSelection()"
            >
              Clear All
            </button>

            <div
              class=""
              v-for="medication in this.medStoreStore.selectedMeds"
              v-bind:key="medication"
            >
              {{ medication }}
              <button
                class="btn btn-sm btn-danger"
                @click="this.removeMedicationFromSelection(medication)"
              >
                Remove
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useMedStore } from "@/store";
import { mapStores } from "pinia";

import { SERVER_URL } from "@/constants";

export default {
  data() {
    return {
      searchString: "",
      searchResults: [],
    };
  },

  mounted() {
    console.log("Mounted!");
  },

  methods: {
    searchForMedication() {
      if (this.searchString.length > 2) {
        fetch(`${SERVER_URL}/mock-search/${this.searchString}`)
          .then((resp) => {
            resp.json().then((body) => {
              this.searchResults = body["searchResults"];
            });
          })
          .catch((err) => {
            // TODO: Handle this better.
            console.error(err);
          });
      }
    },

    addMedicationToSelection(medication) {
      this.medStoreStore.addMedication(medication);

      // reset the form.
      this.$data.searchResults = [];
      this.searchString = "";
    },

    removeMedicationFromSelection(medication) {
      this.medStoreStore.removeMedication(medication);
    },

    clearMedicationSelection() {
      this.medStoreStore.clearAllSelectedMeds();
    },
  },
  computed: {
    ...mapStores(useMedStore),
  },
};
</script>

<style scoped>
#search-results {
  min-height: 200px;
}
</style>
