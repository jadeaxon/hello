<template>
<div>
	<p>Hi, {{user}}!</p>
</div>
</template>

<script>
module.exports = {
	data: function () {
		return { user: 'default user' }
	}
}
</script>

<style scoped>
p {
	text-color: purple
}
</style>


