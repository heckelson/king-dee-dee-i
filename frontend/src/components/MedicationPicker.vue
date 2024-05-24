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
                @click="addMedicationToSelection(result)"
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

<script setup>
import { useMedStore } from "stores/store";
import { SERVER_URL } from "src/constants";
import { ref } from "vue";
import { useQuasar } from "quasar";

const isInitialSearch = ref(true);
const searchString = ref("");
const searchResults = ref([]);
const medStore = useMedStore();
const loadingSpinnerShown = ref(false);
const quasar = useQuasar();

const searchForMedication = () => {
  isInitialSearch.value = false;
  if (searchString.value.length > 2) {
    searchResults.value = [];
    loadingSpinnerShown.value = true;

    fetch(`${SERVER_URL}/mock-search/${searchString.value}`)
      .then((resp) => {
        resp.json().then((body) => {
          searchResults.value = body["searchResults"];

          // filter out all elements that are already in our selection.
          searchResults.value = searchResults.value.filter(
            (elem) => medStoreStore.selectedMeds.indexOf(elem) === -1
          );
        });
      })
      .catch((err) => {
        // TODO: Handle this better.
        console.error(err);
        quasar.notify({
          type: "negative",
          message: "Error fetching medications",
        });
      })
      .finally(() => {
        loadingSpinnerShown.value = false;
      });
  }
};

const addMedicationToSelection = (medication) => {
  medStoreStore.addMedication(medication);

  // reset the form.
  searchResults.value = [];
  searchString.value = "";
};
</script>

<style scoped>
.list {
  min-width: 300px;
}
</style>
