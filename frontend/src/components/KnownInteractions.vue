<template>
  <div class="column items-center">
    <div class="q-pa-md" style="max-width: 700px">
      <q-expansion-item v-model="isAccordionExpanded" class="shadow-1 overflow-hidden" style="border-radius: 24px"
        :icon="icon" :label="label" :header-class="`bg-${color} text-white`" :expand-icon-class="isLoading ||
        interactions.searchResults == null ||
        interactions.searchResults?.length === 0
        ? 'hidden'
        : 'text-white'
        ">
        <q-card>
          <q-card-section>
            <div class="row">
              <q-list>
                <div v-for="interaction in interactions.searchResults" v-bind:key="interaction">
                  <q-item>
                    <q-item-section>
                      <q-item-label class="text-h6">
                        {{ interaction.condition_concept_name }}</q-item-label>
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
</template>

<script setup>
import { ref, computed, watch } from "vue";
import { useMedStore } from "stores/store";

const medStore = useMedStore();
const color = ref("green");
const icon = ref("check");
const label = ref("No known interactions");
const isAccordionExpanded = ref(false);

const isLoading = computed(() => medStore.isLoading);
const interactions = computed(() => medStore.interactions);

watch(
  isLoading,
  () => {
    if (isLoading.value === true) {
      color.value = "blue";
      icon.value = "hourglass_empty";
      label.value = "Looking for interactions ...";
      isAccordionExpanded.value = false;
      return;
    }
  }
);

watch(interactions, () => {
  if (interactions.value.searchResults?.length > 0) {
    color.value = "deep-orange";
    icon.value = "warning";
    label.value = `${interactions.value?.searchResults?.length ?? 0
      } possible interactions are known`;
  } else {
    color.value = "green";
    icon.value = "check";
    label.value = "No known interactions";
  }
}, { deep: true });

</script>

<style></style>
