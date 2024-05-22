<template>
  <div class="container text-center">
    <div class="col">
      <div class="container">
        <div class="row">
          <div class="col-sm-7">
            <h3>Selected Medications</h3>

            <div>
              <button
                class="btn btn-danger"
                @click="this.clearMedicationSelection()"
              >
                Clear All
              </button>
            </div>
            <div>
              <table class="table table-hover">
                <tbody>
                  <tr
                    v-for="medication of this.medStoreStore.selectedMeds"
                    v-bind:key="medication"
                  >
                    <td class="text-start">{{ medication }}</td>
                    <td>
                      <button
                        class="btn btn-sm btn-danger"
                        @click="this.removeMedicationFromSelection(medication)"
                      >
                        Remove
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useMedStore } from "stores/store";
import { mapStores, storeToRefs } from "pinia";

export default {
  data() {
    return {
      medStore: undefined,
      loadingSpinnerShown: false,
    };
  },

  mounted() {
    this.medStore = storeToRefs(this.medStoreStore);
  },

  methods: {
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
