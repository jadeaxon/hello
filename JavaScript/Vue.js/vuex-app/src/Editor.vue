<template>
<div>
	<!-- Should not use a prop as a v-model. -->
	<!-- When using Vuex, v-model is no longer even needed here. -->
	<!-- You do need to v-bind it to value though. -->
	<label>Message: </label><input type="text" :value="msg" @keyup="keyHandler" size="80">
</div>
</template>


<script>
export default {
	// No longer have this be a prop since we are using the Vuex store instead.
	// props: ['msg'],
	computed: {
		msg() {
			return this.$store.state.msg;
		}
	},
	methods: {
		keyHandler(e) {
			// The changeMessage mutation is defined in our Vuex in store.js.
			// e.target.value is the value of the tex input on a key up event.
			this.$store.commit('changeMessage', e.target.value);
		}
	}
}

</script>


<style scoped>
</style>

