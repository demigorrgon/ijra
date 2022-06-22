<template>
  <div class="home">
    <p style="border: 1px black; margin: 15px 0px 15px 0px">Home</p>
    <DraggableMenu />
  </div>
</template>

<script>
// @ is an alias to /src
import DraggableMenu from "../components/DraggableMenu.vue";
export default {
  name: "HomeView",
  components: { DraggableMenu },
};
</script>
