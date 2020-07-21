<template>
<div>
	<p>{{msg}}</p>
</div>
</template>


<script>
export default {
	// Any reason for msg to still be a prop?  Nope.	
	// props: ['msg'],
	computed: {
		msg() {
			// I guess $store is injected into components.
			return this.$store.state.msg
		}
	}
}

</script>


<style scoped>
</style>

