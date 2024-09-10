<template>
	<div class="form-control">
		<span class="label label-text">{{ text }}</span>
		<input 
			class="input input-bordered" 
			:type="type"
			:placeholder="placeholder" 
			:name="name" 
			:value="value"
			@input="updateValue($event.target)"
		>
	</div>
</template>

<script setup>
const props = defineProps({
    text: String,
    placeholder: String,
    value: String,
	name: String,
	type: {
		type: String,
		default: 'text',
	},
});

const emit = defineEmits(['update:value']);
const updateValue = (target) => {
	emit('update:value', {name: target.name, value: target.value});
};
</script>