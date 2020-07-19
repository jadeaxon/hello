<template>
<div class="concise-greeter">
	<p>Hi, {{user}}!</p>
	<input type="text" v-model="user">
</div>
</template>

<script>
module.exports = {
	data: function () {
		return { user: 'default user' }
	},
	props: ['user']

}
</script>

<style>
.concise-greeter {
	background-color: gray;
}
</style>


