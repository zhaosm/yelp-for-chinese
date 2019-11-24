<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Whatever",
  data() {
    return {
      msg: ""
    };
  },
  methods: {
    getMessage() {
      const path = "http://localhost:5000/whatever";
      axios
        .get(path)
        .then(res => {
          this.msg = res.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  created() {
    this.getMessage();
  }
};
</script>
