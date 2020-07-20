<template>
<div>
	<!-- Should not use a prop as a model. -->
	<input type="text" v-model="msg">
</div>
</template>


<script>
export default {
	props: ['msg']
}

</script>


<style scoped>
</style>

