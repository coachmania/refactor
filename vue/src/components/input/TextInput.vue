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
import { ref } from 'vue';

const props = defineProps({
    label: String,
    placeholder: String,
    value: String,
	name: String,
});

const emit = defineEmits(['update:value']);
const timeout = ref(null);
const updateValue = (target) => {
	if (timeout.value) {
		clearTimeout(timeout.value);
	}
	timeout.value = setTimeout(() => {
		emit('update:value', {name: target.name, value: target.value});
	}, 500);
};
</script>