<template>
<div>
	<!-- Should not use a prop as a model. -->
	<input type="text" v-model="msg" @keyup="keyHandler">
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

