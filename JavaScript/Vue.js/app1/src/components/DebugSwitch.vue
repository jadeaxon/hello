<template>
<div>
	<label>Debug: </label><input type="checkbox" v-model="debug">
	<p v-if="debug">Debugging is turned on.</p>
</div>
</template>


<script>
export default {
	name: 'DebugSwitch',
	data() {
		return { debug: false };
	},
}

</script>


<style scoped>
div {
	background-color: orange;
}
</style>


