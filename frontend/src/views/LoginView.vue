<template>
  <div class="login-form">
    <h2 style="margin-top:50px;">Login:</h2>
    <vs-row>
      <vs-col vs-type="flex" vs-align="center" vs-justify="center" style="margin-top:20px; margin-bottom: 10px">
          <vs-input placeholder="Username" v-model="username"/></vs-col>
      <vs-col vs-type="flex" vs-align="center" vs-justify="center" style="margin-bottom: 10px;">
        <vs-input
          type="password"
          placeholder="Password"
          v-model="password"
        /></vs-col>
      </vs-col>
      <vs-col vs-type="flex" vs-align="center" vs-justify="center">
      <vs-button color="rgb(50,205,50)" type="filled" @click="login">Login</vs-button></vs-col>
    </vs-row>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  data: () => {
    return {
      username: null,
      password: null,
    };
  },
  methods: {
    login() {
      this.$store.dispatch("getAccessToken", {
        username: this.username,
        password: this.password,
      });
      // this.$store.commit("authorizeUser");
      this.$router.push("/");
    },
  },
  computed: {},
};
</script>

<style>
</style>