<template>
<div id="app">
	<editor />
	<viewer />
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
	components: {
		Viewer: Viewer,
		Editor: Editor
	}
}
</script>


<style scoped>
</style>
