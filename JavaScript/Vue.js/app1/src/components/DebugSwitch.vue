<template>
<div>
	<label>Debug: </label><input v-on:change="changeHandler" type="checkbox" v-model="debug">
	<p>Changes: {{changes}}</p>
	<p v-if="debug">Debugging is turned on.</p>
</div>
</template>


<script>
export default {
	name: 'DebugSwitch',
	data() {
		return { 
			debug: false,
			changes: 0
		};
	},
	methods: {
		// Counts how many times the checkbox state has changed.
		changeHandler() {
			this.changes += 1;
		}
	}
}

</script>


<style scoped>
div {
	background-color: orange;
}
</style>


