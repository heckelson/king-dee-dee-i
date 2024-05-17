import { defineStore } from "pinia";

export const useMedStore = defineStore("medStore", {
  state: () => ({
    count: 0,
  }),
  getters: {
    count: (state) => state.count,
  },
  actions: {
    increment() {
      this.$state.count += 1;
    },
  },
});
