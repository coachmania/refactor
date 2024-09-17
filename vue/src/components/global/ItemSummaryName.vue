<template>
	<div class="h-full grid grid-rows-2">
		<h1 class="h-full flex items-center">
			{{ title }}
		</h1>
		<p class="font-thin h-full flex items-center">{{ subtitle }}</p>
	</div>
</template>

<script setup>
const props = defineProps({
	title: String,
	subtitle: String
});
</script>