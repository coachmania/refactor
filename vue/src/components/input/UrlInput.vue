<template>
	<div class="form-control">
		<span class="label label-text">{{ label }}</span>
		<input 
			type="text"
			class="input input-bordered" 
			:placeholder="placeholder" 
			:name="name" 
			:value="value"
			@input="updateValue($event)"
		>
	</div>
</template>

<script setup>
import { handleInput } from './handleInput';

// TODO ajouter la logique de verification de l'url
const props = defineProps({
	label: String,
    placeholder: String,
    value: String,
	name: String,
});

const emit = defineEmits(['update:value']);
const updateValue = (event) => {
    handleInput(event, emit, props.name);
};
</script>