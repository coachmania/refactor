<template>
	<div class="join grid" :class="colsClass">
		<button 
			v-for="(item, index) in items" 
			:key="index" 
			class="btn join-item no-animation"
			:class="[
				item === selectedItem ? 'btn-primary' : 'bg-base-100',
				item !== selectedItem && customClass ? customClass : ''
			]"
			@click="$emit('clicked', item)"
		>
			{{ item }}
		</button>
	</div>
</template>

<script setup>
const props = defineProps({
	items: Array,
	selectedItem: String,
	colsClass: String,
	customClass: String,
});
</script>