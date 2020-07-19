<template>
<div class="concise-greeter">
	<p>Hi, {{user}} now {{my_user}}!</p>
	<input type="text" v-model="my_user">
</div>
</template>

<script>
module.exports = {
	data: function () {
		return { my_user: 'component user' }
	},
	props: ['user']

}
</script>

<!-- Using <style scoped> makes this CSS apply only to ConciseGreeter components. -->
<!-- Seems to be broken though. -->
<style>
.concise-greeter {
	background-color: gray;
	color: purple;
}
</style>


