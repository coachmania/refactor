<template>
	<div class="join grid" :class="class">
		<button 
			v-for="(item, index) in items" 
			:key="index" 
			class="btn join-item no-animation"
			:class="item === selectedItem ? 'btn-primary' : 'bg-base-100 border-base-content/15'"
		>
			{{ item }}
		</button>
	</div>
</template>

<script setup>
const props = defineProps({
	items: Array,
	selectedItem: String,
	class: String,
});
</script>