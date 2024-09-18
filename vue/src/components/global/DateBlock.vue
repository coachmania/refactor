<template>
	<div class="grid grid-cols-2 gap-md">
		<SelectInput
			label="Mois de début"
			name="start_month"
			:value="data.start_month"
			:items="data.month_choices"
			@update:value="updateValue"
		/>
		<NumberInput
			:min="0"
			:max="9999"
			label="Année de début"
			placeholder="2020"
			name="start_year"
			:value="data.start_year"
			@update:value="updateValue"
		/>
		<SelectInput
			label="Mois de fin"
			name="end_month"
			:value="data.end_month"
			:items="data.month_choices"
			@update:value="updateValue"
		/>
		<NumberInput
			:min="0"
			:max="9999"
			label="Année de fin"
			placeholder="2024"
			name="end_year"
			:value="data.end_year"
			@update:value="updateValue"
		/>
	</div>
</template>

<script setup>
import SelectInput from '../input/SelectInput.vue';
import NumberInput from '../input/NumberInput.vue';

const props = defineProps({
	data: Object,
});

const emit = defineEmits(['update:value']);
const updateValue = (value) => {
	emit('update:value', value);
};
</script>