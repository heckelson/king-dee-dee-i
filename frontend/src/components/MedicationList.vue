<template>
  <div class="column items-center q-gutter-y-md listWrapper">
    <div class="column">
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
              <q-item-label class="text-h6 text-capitalize">{{
                medication
              }}</q-item-label>
            </q-item-section>
            <q-item-section side top>
              <q-btn
                outline
                rounded
                color="primary"
                label="Remove"
                @click="this.removeMedicationFromSelection(medication)"
                size="sm"
              />
            </q-item-section>
          </q-item>
        </div>
        <q-item-label v-if="this.medStoreStore.selectedMeds.length === 0">
          <q-item-section>
            <q-item-label class="text-center"
              >No medications selected</q-item-label
            >
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
  min-width: 300px;
}

.listWrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
</style>
