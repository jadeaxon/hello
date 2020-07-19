<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
	
	<!-- This does not change even though we bound user to the component. -->
	<p>App user: {{user}}</p>

	<!-- Use my custom component. -->
	<concise-greeter :user='user' />
  </div>
</template>


<script>
import HelloWorld from './components/HelloWorld.vue'

// Import my custom component.
import ConciseGreeter from './components/ConciseGreeter.vue'

export default {
	name: 'App',
	
	// We'll v-bind this to a props property in ConciseGreeter.
	data: function () {
		return {
			user: 'parent user'
		};
	},
	// Not exactly sure why a list works between {}.
	components: {
		HelloWorld,
		// Register my custom component.
		ConciseGreeter
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
