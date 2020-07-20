<template>
  <div id="app">
    <!--
    <img alt="Vue logo" src="./assets/logo.png">
	<HelloWorld msg="Welcome to Your Vue.js App"/>
	-->

	<!-- This does not change even though we bound user to the component. -->
	<p>App user: {{user}}</p>
	<p v-if="debug">Debug enabled in App component.</p>

	<!-- Use my custom components. -->
	<concise-greeter :user='user' :debug='debug' />
	
	<!-- WARNING: The debug-mode event won't bubble up to the <div>. -->
	<!-- Thus, you must attach the event handler to the component that emitted the event. -->
	<!-- This is how you communicate from child component back up to parent component. -->
	<debug-switch v-on:debug-mode="handleDebug" />

  </div>
</template>


<script>
// Import an ES6 module.
// import HelloWorld from './components/HelloWorld.vue'

// Import (require) a CommonJS module.
// var ConciseGreeter = require('./components/ConciseGreeter.vue');
// Interestingly, the above does not work.
// There's some kind of magic with the way Webpack interacts with import.
// That, or I just have no idea what the heck I'm doing.
import ConciseGreeter from './components/ConciseGreeter.vue'

import DebugSwitch from './components/DebugSwitch.vue'

export default {
	name: 'App',
	
	// We'll v-bind this to a props property in ConciseGreeter.
	data: function () {
		return {
			user: 'parent user',
			debug: false
		};
	},
	// Not exactly sure why a list works between {}.
	components: {
		// HelloWorld,
		// Register my custom component.
		ConciseGreeter,
		DebugSwitch
	},
	methods: {
		handleDebug(value) {
			this.debug = value;
		}
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

