<template>
<div class="concise-greeter">
	<p>Hi, {{user}} now {{my_user}}!</p>
	<input type="text" v-model="my_user">
</div>
</template>

<script>
// This is the older CommonJS way of creating a module.
// Use require() with these. 
// Basically module.exports is the object returned when you require this module.
// Each file kind of is implicitly a module (has a module variable).
module.exports = {
	data: function () {
		return { my_user: 'component user' }
	},
	props: ['user']

}
</script>

<!-- Using <style scoped> makes this CSS apply only to ConciseGreeter components. -->
<!-- Seems to be broken though. -->
<!--
For some reason, scoped styles don't get applied during hot reload when
they are first added to the component. Full page reload fixes the issue,
from there the styles, since they have been detected, get updated with
consecutive hot reloads.
-->
<style scoped>
p {
	color: purple;
}
.concise-greeter {
	background-color: gray;
}
</style>


