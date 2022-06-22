<template>
  <div id="app">
    <Navbar />
    <div v-if="tokenValid === false">not valid</div>
    <router-view />
  </div>
</template>
<script>
import Navbar from "./components/Navbar.vue";

export default {
  data: () => {
    return {
      tokenValid: null,
    };
  },
  components: {
    Navbar,
  },
  watch: {
    $route(to, from) {
      // this.verifyToken();
    },
  },
  methods: {
    verifyToken() {
      this.$store.dispatch("isTokenValid");
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
