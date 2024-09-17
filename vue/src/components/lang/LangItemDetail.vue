<template>
	<div class="grid grid-cols-[1fr,auto]">
		<CardTitle>{{ data.name }}</CardTitle>
		<button class="btn btn-outline btn-error btn-square" @click="handleClick">
			<svg class="w-icon h-icon fill-current" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="m16.192 6.344-4.243 4.242-4.242-4.242-1.414 1.414L10.535 12l-4.242 4.242 1.414 1.414 4.242-4.242 4.243 4.242 1.414-1.414L13.364 12l4.242-4.242z"></path></svg>
		</button>
	</div>
	<TextInput
		label="Nom de la langue"
		customClass="bg-base-200"
		placeholder="Anglais"
		name="name"
		:value="data.name"
		@update:value="updateValue"
	/>
	<div>
		<span class="label label-text">Niveau</span>
		<MultiButton
			class="grid-cols-5"
			:items="data.level_choices"
			:selectedItem="data.level"
			@clicked="updateLevel"
		/>
	</div>
	<TextInput
		label="Justification"
		customClass="bg-base-200"
		placeholder="Voyage en Angleterre"
		name="justification"
		:value="data.justification"
		@update:value="updateValue"
	/>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import apiClient from '@/services/api.js';
import CardTitle from '../global/CardTitle.vue';
import TextInput from '../input/TextInput.vue';
import MultiButton from '../button/MultiButton.vue';

const data = reactive({});

const props = defineProps({
	langId: Number
});

const emit = defineEmits(['close']);
const handleClick = () => {
	emit('close');
};

const updateLevel = async (value) => {
	data.level = value;
	await updateValue({name: 'level', value});
};

const updateValue = async ({name, value}) => {
	try {
		let sendData = {[name]: value,}
		await apiClient.put(`/cv_lang/fields/${props.langId}/`, sendData);
	} catch (error) {
		console.error('Error updating language data:', error);
	}
};

const fetchLangData = async () => {
	try {
		const response = await apiClient.get(`/cv_lang/item/${props.langId}/`);
		Object.assign(data, response.data);
	} catch (error) {
		console.error('Error fetching language data:', error);
	}
};

onMounted(() => {
	fetchLangData();
});
</script>