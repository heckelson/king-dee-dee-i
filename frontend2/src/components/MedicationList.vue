<template>
  <div class="container text-center">
    <div class="col">
      <div class="container">
        <div class="row">
          <div class="col-sm-7">
            <div class="text-h4">Your Medications</div>

            <q-list>
              <div
                v-for="medication of this.medStoreStore.selectedMeds"
                v-bind:key="medication"
              >
                <q-item>
                  <q-item-section>
                    <q-item-label>{{ medication }}</q-item-label>
                  </q-item-section>
                  <q-item-section side top>
                    <q-btn
                      outline
                      rounded
                      color="primary"
                      label="Remove"
                      @click="this.removeMedicationFromSelection(result)"
                    />
                  </q-item-section>
                </q-item>
              </div>
              <q-item-label v-if="this.medStoreStore.selectedMeds.length === 0">
                <q-item-section>
                  <q-item-label>No medications found</q-item-label>
                </q-item-section>
              </q-item-label>
            </q-list>

            <q-btn
              @click="this.clearMedicationSelection()"
              outline
              rounded
              color="warning"
            >
              Clear All
            </q-btn>
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
