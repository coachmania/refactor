<template>
	<div class="form-control">
		<span class="label label-text">{{ label }}</span>
		<input 
			type="number"
			class="input bg-base-200" 
			:min=min
			:max=max
			:placeholder="placeholder" 
			:name="name" 
			:value="value"
			@input="updateValue($event)"
		>
	</div>
</template>

<script setup>
import { handleInput } from './handleInput';

const props = defineProps({
    label: String,
    placeholder: String,
    value: Number,
	name: String,
	min: Number,
	max: Number,
});

const emit = defineEmits(['update:value']);
const updateValue = (event) => {
    handleInput(event.target.value, emit, props.name);
};
</script>