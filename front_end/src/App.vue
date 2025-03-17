<template>
  <headersCustom />
  <main class = "crt-scanlines crt-flicker">
    <RouterView />
  </main>

  <p class = "crt-flicker"> This is a test </p>
</template>

<script>
import headersCustom from './components/headersCustom.vue'



export default {
  name: 'App',
  components: {
    headersCustom
  },
  data(){
    return{
      scanline : true,
      flicker : true,
      distortion : true,
      static : true
    }
  },
  methods: {
    flip_scanlines(){
      this.scanline = !this.scanline
    },
    flip_flicker(){
      this.flicker  = !this.flicker
    }
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

.crt-flicker {
  font-family: monospace; /* Or any retro font */
  color: #0f0; /* Green text */
  background-color: black;
  text-shadow: 0 0 5px #00ff00; /* Glow effect */
  animation: crt-flicker 0.1s infinite steps(2); /* Flicker animation */
}

@keyframes crt-flicker {
  0%, 100% {
    opacity: 1;
    text-shadow: 0 0 5px #0f0;
  }
  50% {
    opacity: 0.9; /* Slight opacity variation */
    text-shadow: 0 0 3px #0f0; /* Slight glow variation */
  }
}

.crt-scanlines {
  position: relative;
  overflow: hidden;
}

.crt-scanlines::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: repeating-linear-gradient(
    0deg,
    rgba(0, 0, 0, 1) 0px,
    rgba(0, 0, 0, 1) 1px,
    transparent 2px,
    transparent 4px
  );
  pointer-events: none; /* Allows clicks on the element itself */
  z-index: 1; /* Ensure scanlines are on top */
}

.crt-distortion {
  animation: crt-distortion 0.5s infinite alternate;
}

@keyframes crt-distortion {
  0%, 100% {
    transform: perspective(300px) rotateY(0deg) scale(1.0);
  }
  50% {
    transform: perspective(300px) rotateY(2deg) scale(1.01);
  }
}

</style>
