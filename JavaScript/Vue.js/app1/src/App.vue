<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
	
	<!-- Use my custom component. -->
	<concise-greeter />
  </div>
</template>


<script>
import HelloWorld from './components/HelloWorld.vue'

// Import my custom component.
import ConciseGreeter from './components/ConciseGreeter.vue'

export default {
  name: 'App',
  components: {
    HelloWorld: HelloWorld,
	// Register my custom component.
	ConciseGreeter: ConciseGreeter
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
