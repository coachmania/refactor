<template>
	<div class="form-control">
		<span class="label label-text">{{ label }}</span>
		<input 
			type="text"
			class="input shadow-sm bg-base-200"
			:class="customClass"
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
    value: String,
	name: String,
	customClass: String,
});

const emit = defineEmits(['update:value']);
const updateValue = (event) => {
    handleInput(event.target.value, emit, props.name);
};
</script>