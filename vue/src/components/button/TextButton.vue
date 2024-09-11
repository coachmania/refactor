<template>
	<button class="btn btn-primary btn-block no-animation">
		<slot></slot>
		<p>{{ text }}</p>
	</button>
</template>

<script setup>
const props = defineProps({
	text: String,
});
</script>