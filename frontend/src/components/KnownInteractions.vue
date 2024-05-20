<template>
  <div class="text-center">
    <h1>Known Interactions</h1>
    <div class="container">
      <p>Table</p>

      <pre class="text-start">{{ this.interactions }}</pre>
    </div>
  </div>
</template>

<script>
import { useMedStore } from "@/store";
import { mapStores, storeToRefs } from "pinia";

import { SERVER_URL } from "@/constants";

export default {
  data() {
    return {
      interactions: [],
      medStore: undefined, // defined in `mounted()`
    };
  },

  mounted() {
    this.medStore = storeToRefs(this.medStoreStore);
  },

  methods: {
    fetchInteractions() {
      const encodedSelection = encodeURI(this.medStore.selectedMeds);

      if (this.medStore.selectedMeds.length >= 2) {
        fetch(
          `${SERVER_URL}/mock-interactions?selectedMeds=${encodedSelection}`,
        )
          .then((resp) => {
            resp.json().then((body) => {
              this.interactions = body;
            });
          })
          .catch((err) => {
            console.error(err);
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
        if (newState.selectedMeds.length > 1) {
          this.fetchInteractions();
        } else {
          // we can't have interactions with only 1 med, thus we clear the variable.
          this.interactions = [];
        }
      },
      deep: true,
    },
  },
};
</script>

<style></style>
