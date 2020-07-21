<template>
<div id="app">
	<editor />
	<viewer />
</div>
</template>


<script>
import Editor from './Editor.vue';
import Viewer from './Viewer.vue';
import store from './vuex/store';

export default {
	name: 'app',
	data () {
		return {
			msg: 'App: Welcome to your Vue.js Vuex app'
		}
	},
	// ES6 adds the shorthand of being able to use 'foo' for 'foo: foo' in object literals.
	/*
	components: {
		Viewer: Viewer,
		Editor: Editor
	}
	*/
	components: {Viewer, Editor},
	store
}
</script>


<style scoped>
</style>
