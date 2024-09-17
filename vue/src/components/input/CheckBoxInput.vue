<template>
	<div class="form-control">
		<span class="label label-text">{{ label }}</span>
		<button 
			class="btn no-animation"
			:class="isChecked ? 'btn-square btn-primary' : 'input bg-base-200 shadow-sm w-12 p-0'"
			@click="toggleCheck"
		>
			<template v-if="isChecked">
				<svg class="h-icon w-icon fill-current pointer-events-none select-none" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="m10 15.586-3.293-3.293-1.414 1.414L10 18.414l9.707-9.707-1.414-1.414z"></path></svg>
			</template>
		</button>
	</div>
</template>

<script setup>
import { ref, watch } from 'vue';

const props = defineProps({
    label: String,
	name: String,
    checked: Boolean,
});

const isChecked = ref(props.checked);

const emit = defineEmits(['update:value']);
const toggleCheck = () => {
	isChecked.value = !isChecked.value;
	let name = props.name;
	emit('update:value', {name, value: isChecked.value});
};

watch(() => props.checked, (newVal) => {
    isChecked.value = newVal;
});
</script>