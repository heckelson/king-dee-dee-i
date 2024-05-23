<template>
  <div class="column items-center">
    <div class="column q-gutter-md">
      <div class="text-h4">Your Medications</div>
    </div>

    <div class="list">
      <q-list>
        <div
          v-for="medication of this.medStoreStore.selectedMeds"
          v-bind:key="medication"
        >
          <q-item>
            <q-item-section>
              <q-item-label class="text-h6">{{ medication }}</q-item-label>
            </q-item-section>
            <q-item-section side top>
              <q-btn
                outline
                rounded
                color="primary"
                label="Remove"
                @click="this.removeMedicationFromSelection(medication)"
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
    </div>

    <q-btn
      v-if="this.medStoreStore.selectedMeds.length > 0"
      @click="this.clearMedicationSelection()"
      outline
      rounded
      color="warning"
      size="sm"
      class="self-center"
    >
      Remove All
    </q-btn>
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
.list {
  min-width: 500px;
}
</style>
