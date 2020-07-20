<template>
<div class="concise-greeter">
	<p>Hi, {{user}} (now {{my_user}})!</p>
	<input type="text" v-model="my_user">
	<p v-if="debug">Debugging enabled (indirectly via props v-bind) for ConciseGreeter.</p>
</div>
</template>

<script>
/*
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
*/

// Create an ES6 module (instead of a CommonJS one).
export default {
	name: 'ConciseGreeter',
	data() {
		return { 
			my_user: 'ES6 component user',
		};
	},
	// The debug property will be dynamically bound in parent component via v-bind.
	// It will be bound to its debug value which is toggled via the DebugSwitch compenent.
	// Thus, that component will indirectly affect this one.
	// Note that unless you use a global bus, components can't listen to events from arbitrary
	// components.
	props: ['user', 'debug']
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


