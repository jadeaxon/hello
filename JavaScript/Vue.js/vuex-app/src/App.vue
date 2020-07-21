<template>
<div id="app">
	<editor :msg="msg" />
	<viewer :msg="msg" />
</div>
</template>


<script>
import Editor from './Editor.vue'
import Viewer from './Viewer.vue'

export default {
	name: 'app',
	data () {
		return {
			msg: 'Welcome to your Vue.js Vuex app'
		}
	},
	// ES6 adds the shorthand of being able to use 'foo' for 'foo: foo' in object literals.
	/*
	components: {
		Viewer: Viewer,
		Editor: Editor
	}
	*/
	components: {Viewer, Editor}
}
</script>


<style scoped>
</style>
