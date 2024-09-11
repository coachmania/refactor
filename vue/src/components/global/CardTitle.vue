<template>
	<h1 class="card-title">{{ title }}</h1>
</template>

<script setup>
const props = defineProps({
	title: String,
});
</script>