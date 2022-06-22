<template>
  <div class="wrapper">
      <vs-alert title="Danger" active="true" color="danger" v-if="error">User already exists</vs-alert>
    <vs-row>
      <h2 style="margin: 0 auto; margin-top: 20px; margin-bottom: 15px">Register:</h2>
      <vs-col vs-type="flex" vs-align="center" vs-justify="center">
        <vs-input label-placeholder="Username" v-model="username" />
      </vs-col>
      <vs-col vs-type="flex" vs-align="center" vs-justify="center">
        <vs-input label-placeholder="Password" type="password" v-model="password" />
      </vs-col>
      <vs-col vs-type="flex" vs-align="center" vs-justify="center" style="margin-top:20px;">
          <vs-button color="rgb(50,205,50)" type="filled" @click="register">Register</vs-button></vs-col>
      </vs-col>
    </vs-row>
  </div>
</template>

<script>
import { registerUser } from "../api/shortcuts";
export default {
  data: () => {
    return {
      username: null,
      password: null,
      error: false,
    };
  },
  methods: {
    register() {
      //   console.log(this.username, this.password);
      registerUser(this.username, this.password)
        .then((response) => {
          //   console.log(response);
          if (response.status === 201) {
            this.$store.dispatch("getAccessToken", {
              username: this.username,
              password: this.password,
            });
            this.$router.push("/");
          }
        })
        .catch((error) => (this.error = true));
    },
  },
};
</script>

<style>
</style>