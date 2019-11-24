<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <Whatever></Whatever>
      </div>
      <v-spacer></v-spacer>
    </v-app-bar>
  </v-app>
</template>

<script>
import Whatever from "./components/Whatever.vue";

export default {
  name: "App",

  components: {
    Whatever
  },

  data: () => ({
    //
  })
};
</script>
