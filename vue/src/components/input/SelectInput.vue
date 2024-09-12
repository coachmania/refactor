<template>
	<div class="form-control">
		<span class="label label-text">{{ label }}</span>
		<select 
			class="select select-bordered w-full"
			autocomplete="off"
			:value="value"
			:name="name" 
			@input="updateValue($event)"
		>
			<option 
				v-for="item in items" 
				:key="item.id" 
				:value="item.id"
			>
				{{ item }}
			</option>
		</select>
	</div>
</template>

<script setup>
const props = defineProps({
    label: String,
    value: String,
	name: String,
	items: Array,
});

const emit = defineEmits(['update:value']);
const updateValue = (event) => {
	let name = props.name;
	emit('update:value', {name, value: event.target.value});
};
</script>