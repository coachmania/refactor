<template>
	<button
		class="btn btn-square no-animation"
		:class="ghost ? 'btn-ghost' : 'btn-primary'"
	>
		<slot></slot>
	</button>
</template>

<script setup>
const props = defineProps({
	ghost: Boolean,
});
</script>