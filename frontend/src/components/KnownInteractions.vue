<template>
  <div class="column items-center">
    <div class="q-pa-md" style="max-width: 700px">
      <q-expansion-item
        v-model="isAccordionExpanded"
        class="shadow-1 overflow-hidden"
        style="border-radius: 24px"
        :icon="icon"
        :label="label"
        :header-class="`bg-${color} text-white`"
        :expand-icon-class="
          loadingSpinnerShown ||
          interactions.searchResults == null ||
          interactions.searchResults?.length === 0
            ? 'hidden'
            : 'text-white'
        "
      >
        <q-card>
          <q-card-section>
            <div class="row">
              <q-list>
                <div
                  v-for="interaction in this.interactions.searchResults"
                  v-bind:key="interaction"
                >
                  <q-item>
                    <q-item-section>
                      <q-item-label class="text-h6">
                        {{ interaction.condition_concept_name }}</q-item-label
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
</template>

<script>
import { useMedStore } from "stores/store";
import { mapStores, storeToRefs } from "pinia";

import { SERVER_URL } from "src/constants";

export default {
  data() {
    return {
      interactions: {},
      medStore: undefined, // defined in `mounted()`
      loadingSpinnerShown: false,
      color: "green",
      icon: "check",
      label: "No known interactions",
      isAccordionExpanded: false,
    };
  },

  mounted() {
    this.medStore = storeToRefs(this.medStoreStore);
  },

  methods: {
    fetchInteractions() {
      const encodedSelection = encodeURI(this.medStore.selectedMeds);

      this.loadingSpinnerShown = true;

      if (this.medStore.selectedMeds?.length >= 2) {
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
            this.loadingSpinnerShown = false;
          });
      }
    },
  },
  computed: {
    ...mapStores(useMedStore),
  },

  watch: {
    medStore: {
      handler(newState, _) {
        if (newState === undefined) return;
        if (newState.selectedMeds?.length > 1) {
          this.fetchInteractions();
        } else {
          // we can't have interactions with only 1 med, thus we clear the variable.
          this.interactions = [];
        }
      },
      deep: true,
    },
    loadingSpinnerShown: {
      handler(newState, _) {
        if (this.loadingSpinnerShown) {
          this.color = "blue";
          this.icon = "hourglass_empty";
          this.label = "Looking for interactions ...";
          this.isAccordionExpanded = false;
          return;
        }
      },
    },
    interactions: {
      handler(newState, _) {
        console.log("interactions changed", newState);
        if (newState.searchResults?.length > 0) {
          this.color = "deep-orange";
          this.icon = "warning";
          this.label = `${
            this.interactions?.searchResults?.length ?? 0
          } possible interactions are known`;
        } else {
          this.color = "green";
          this.icon = "check";
          this.label = "No known interactions";
        }
      },
      deep: true,
    },
  },
};
</script>

<style></style>
