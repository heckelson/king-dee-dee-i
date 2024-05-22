<template>
    <div class="text-center">
        <h1>Known Interactions</h1>
        <div class="container">
            <p>Table</p>

            <div class="container text-center" v-show="loadingSpinnerShown">
                <div class="spinner-grow text-primary" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
            </div>

            <pre class="text-start">{{ this.interactions }}</pre>
        </div>
    </div>
</template>

<script>
import { useMedStore } from 'stores/store';
import { mapStores, storeToRefs } from 'pinia';

import { SERVER_URL } from 'src/constants';

export default {
    data() {
        return {
            interactions: [],
            medStore: undefined, // defined in `mounted()`
            loadingSpinnerShown: false,
        };
    },

    mounted() {
        this.medStore = storeToRefs(this.medStoreStore);
    },

    methods: {
        fetchInteractions() {
            const encodedSelection = encodeURI(this.medStore.selectedMeds);

            this.loadingSpinnerShown = true;

            if (this.medStore.selectedMeds.length >= 2) {
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
