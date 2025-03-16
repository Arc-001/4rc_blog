<template>
  <headersCustom />
  <main>
    <RouterView />
  </main>
</template>

<script>
import headersCustom from './components/headersCustom.vue'



export default {
  name: 'App',
  components: {
    headersCustom
  }
}
</script>


<style>
#app {
  font-family: monospace;
  background-color: black;
  color: green;
  padding: 10px;
  border: 1px solid #000;
  overflow-x: scroll;
  text-align: left;
}
html, body {
  margin: 0;
  padding: 0;
  background-color: #1a1a1a; /* Dark background for the whole page */
  height: 100%;
  width: 100%;
  overflow-x: hidden; /* Prevent horizontal scrolling outside app */
}

/* Apply dark background to all elements by default */
* {
  box-sizing: border-box;
}

body {
  display: flex;
  flex-direction: column;
}

/* Ensure Vue app container fills available space */
#app {
  flex: 1;
}
</style>
