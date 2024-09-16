<template>
	<button class="btn btn-block" @click="handleClick">CLOSE</button>
	<p>{{ lang }}OKK</p>
</template>

<script setup>
const props = defineProps({
	lang: String
});

const emit = defineEmits(['close']);
const handleClick = () => {
	emit('close');
};
</script>