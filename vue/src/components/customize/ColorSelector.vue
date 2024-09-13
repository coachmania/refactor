<template>
	<h2><slot></slot></h2>
	<div class="grid grid-cols-8 gap-md">
		<button
			v-for="n in 8"
			class="aspect-square rounded-btn border-4 border-base-300 hover:opacity-70"
			:class="data.primary === 'TODO' ? 'border-primary' : 'border-base-300'"
		></button>
	</div>
</template>

<script setup>
// TODO temp
const data = {
	primary: '1',
};
</script>