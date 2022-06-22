<template>
  <div>
    <vs-navbar
      class="navbar"
      color="black"
      text-color="white"
      active-text-color="white"
    >
      <div slot="title">
        <vs-navbar-title class="navbar-title"
          ><router-link to="/"
            ><p class="navbar-title-text">IJRA</p></router-link
          >
        </vs-navbar-title>
      </div>
      <vs-navbar-item index="0" v-if="currentUser !== null">
        <a href="#">{{ currentUser.username }}</a>
      </vs-navbar-item>
      <vs-navbar-item index="0">
        <router-link to="/">Home</router-link>
      </vs-navbar-item>
      <vs-navbar-item index="1" v-if="currentUser === null">
        <router-link to="/login">Login</router-link>
      </vs-navbar-item>
      <vs-navbar-item
        index="2"
        v-if="currentUser === null"
        style="margin-right: 100px"
      >
        <router-link to="/register">Register</router-link>
      </vs-navbar-item>
      <vs-navbar-item index="2" v-else style="margin-right: 100px">
        <a href="#" @click="logoutUser">Logout</a>
      </vs-navbar-item>
    </vs-navbar>
  </div>
</template>
<script>
import { mapGetters, mapMutations } from "vuex";
export default {
  computed: {
    ...mapGetters(["currentUser"]),
  },
  methods: {
    ...mapMutations(["logout"]),
    logoutUser() {
      this.$store.commit("logout");
      this.$router.push("/login");
    },
  },
};
</script>
<style>
.navbar {
  height: 50px;
}
.navbar-title {
  margin-left: 300px;
}
.navbar-title-text {
  text-decoration: none;
  color: white;
}
.navbar-title-text:visited {
  text-decoration: none;
  color: white;
}
.navbar-title-text:visited {
  text-decoration: none;
  color: white;
}
.item-wrapper {
  /* margin-right: 50px; */
}
</style>
