<template>
	<div
		class="h-full grid"
		:class="{ 'grid-rows-2': subtitle }"
	>
		<h1 class="h-full flex items-center">
			<slot></slot>
		</h1>
		<p v-if="subtitle" class="font-thin h-full flex items-center">{{ subtitle }}</p>
	</div>
</template>

<script setup>
const props = defineProps({
	title: String,
	subtitle: String
});
</script>