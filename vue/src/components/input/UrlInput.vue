<template>
	<div class="form-control">
		<span class="label label-text">{{ label }}</span>
		<input 
			type="text"
			class="input input-bordered" 
			:placeholder="placeholder" 
			:name="name" 
			:value="value"
			@input="updateValue($event.target)"
		>
	</div>
</template>

<script setup>
// TODO ajouter la logique de verification de l'url
const props = defineProps({
	label: String,
    placeholder: String,
    value: String,
	name: String,
});

const emit = defineEmits(['update:value']);
const updateValue = (target) => {
	emit('update:value', {name: target.name, value: target.value});
};
</script>