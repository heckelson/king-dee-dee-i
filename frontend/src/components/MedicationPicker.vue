<template>
  <div class="column items-center">
    <form @submit.prevent="searchForMedication()" class="input-group">
      <q-input
        v-model="searchString"
        :loading="loadingSpinnerShown"
        @keydown.enter.prevent="searchForMedication()"
        rounded
        outlined
        placeholder="Search medication"
      >
        <template v-slot:append>
          <q-icon name="search" @click="searchForMedication()" />
        </template>
      </q-input>
    </form>

    <div id="search-results">
      <div v-if="loadingSpinnerShown">
        <div class="q-pa-md">
          <div class="q-gutter-y-md">
            <q-skeleton animation="wave" type="rect" />
            <q-skeleton animation="wave" type="rect" />
            <q-skeleton animation="wave" type="rect" />
          </div>
        </div>
      </div>

      <q-list class="list">
        <div v-for="result of searchResults" v-bind:key="result">
          <q-item>
            <q-item-section>
              <q-item-label>{{ result }}</q-item-label>
            </q-item-section>
            <q-item-section side top>
              <q-btn
                outline
                rounded
                color="primary"
                label="Add"
                @click="this.addMedicationToSelection(result)"
              />
            </q-item-section>
          </q-item>
        </div>
        <q-item
          v-if="
            searchResults.length === 0 &&
            !loadingSpinnerShown &&
            !isInitialSearch
          "
        >
          <q-item-section>
            <q-item-label class="text-center">
              No medications found
            </q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </div>
  </div>
</template>

<script>
import { useMedStore } from "stores/store";
import { mapStores, storeToRefs } from "pinia";

import { SERVER_URL } from "src/constants";
import { useToast } from "vue-toastification";
import { notify } from "src/components/notify";

export default {
  data() {
    return {
      isInitialSearch: true,
      searchString: "",
      searchResults: [],
      medStore: undefined,
      loadingSpinnerShown: false,
    };
  },

  mounted() {
    this.medStore = storeToRefs(this.medStoreStore);
  },

  methods: {
    searchForMedication() {
      this.isInitialSearch = false;
      if (this.searchString.length > 2) {
        this.searchResults = [];
        this.loadingSpinnerShown = true;

        fetch(`${SERVER_URL}/mock-search/${this.searchString}`)
          .then((resp) => {
            resp.json().then((body) => {
              this.searchResults = body["searchResults"];

              // filter out all elements that are already in our selection.
              this.searchResults = this.searchResults.filter(
                (elem) => this.medStoreStore.selectedMeds.indexOf(elem) === -1
              );
            });
          })
          .catch((err) => {
            // TODO: Handle this better.
            console.error(err);
            const toast = useToast();
            toast("le toast");
          })
          .finally(() => {
            this.loadingSpinnerShown = false;
          });
      }
    },

    addMedicationToSelection(medication) {
      this.medStoreStore.addMedication(medication);

      // reset the form.
      this.$data.searchResults = [];
      this.searchString = "";
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
</style>
