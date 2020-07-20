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
		changeHandler: function () {
			this.changes += 1;
			// Emit a custom event whenever the debug value changes.
			// This will let us affect the parent component state.
			this.$emit('debug-mode', this.debug);
		}
	}
}

</script>


<style scoped>
div {
	background-color: orange;
}
</style>


