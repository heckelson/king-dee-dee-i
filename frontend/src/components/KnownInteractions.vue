<template>
  <div class="column items-center">
    <div class="q-pa-md" style="max-width: 500px">
      <div v-if="isLoading || (interactions.searchResults?.length ?? 0) === 0">
        <q-expansion-item
          class="shadow-1 overflow-hidden"
          style="border-radius: 24px"
          :icon="icon"
          :label="label"
          :header-class="`bg-${color} text-white`"
          expand-icon-class="hidden"
        >
        </q-expansion-item>
      </div>

      <div v-else>
        <div
          v-for="medicationPair in Object.keys(groupedInteractions)"
          v-bind:key="medicationPair"
          class="q-mb-md"
        >
          <q-expansion-item
            class="shadow-1 overflow-hidden"
            style="border-radius: 24px"
            icon="warning"
            :label="`${groupedInteractions[medicationPair].length} possible interactions between ${medicationPair}`"
            :header-class="`bg-deep-orange text-white`"
            expand-icon-class="text-white"
          >
            <q-card>
              <q-card-section>
                <div class="row">
                  <q-list>
                    <div
                      v-for="interaction in groupedInteractions[medicationPair]"
                      v-bind:key="interaction"
                    >
                      <q-item>
                        <q-item-section>
                          <q-item-label class="text-h6">
                            {{ interaction }}</q-item-label
                          >
                        </q-item-section>
                      </q-item>
                    </div>
                  </q-list>
                </div>
              </q-card-section>
            </q-card>
          </q-expansion-item>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from "vue";
import { useMedStore } from "stores/store";

const medStore = useMedStore();
const color = ref("green");
const icon = ref("check");
const label = ref("No known interactions");

const isLoading = computed(() => medStore.isLoading);
const interactions = computed(() => medStore.interactions);
const lastStoreError = computed(() => medStore.lastError);

const groupedInteractions = computed(() => {
  const interactionsList = interactions.value.searchResults;
  const groupedInteractions = {};

  if (interactionsList) {
    interactionsList.forEach((interaction) => {
      const {
        drug_1_concept_name,
        drug_2_concept_name,
        condition_concept_name,
      } = interaction;

      const key = `${drug_1_concept_name} and ${drug_2_concept_name}`;
      if (!groupedInteractions[key]) {
        groupedInteractions[key] = [];
      }

      groupedInteractions[key].push(condition_concept_name);
    });
  }

  console.log("groupedInteractions", groupedInteractions);
  return groupedInteractions;
});

watch(isLoading, () => {
  if (isLoading.value === true) {
    color.value = "blue";
    icon.value = "hourglass_empty";
    label.value = "Looking for interactions ...";
    return;
  }
});

watch(
  interactions,
  () => {
    if (interactions.value.searchResults?.length > 0) {
      color.value = "deep-orange";
      icon.value = "warning";
      label.value = `${
        interactions.value?.searchResults?.length ?? 0
      } possible interactions are known`;
    } else {
      color.value = "green";
      icon.value = "check";
      label.value = "No known interactions";
    }
  },
  { deep: true }
);

watch(lastStoreError, () => {
  if (lastStoreError.value != null) {
    color.value = "red";
    icon.value = "error";
    label.value = "Error looking for interactions";
  }
});
</script>

<style></style>
