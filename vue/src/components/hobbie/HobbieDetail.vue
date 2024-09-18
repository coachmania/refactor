<template>
	<div class="grid grid-cols-[1fr,auto]">
		<CardTitle>{{ data.name || 'Nouveau centre d\'intérêt' }}</CardTitle>
		<ExitDetailButton @click="handleClick"/>
	</div>
	<div class="grid grid-cols-2 gap-md">
		<SelectInput
			label="Type"
			name="type"
			:value="data.type"
			:items="data.type_choices"
			@update:value="updateValue"
		/>
		<TextInput
			label="Nom"
			placeholder="Basketball"
			name="name"
			:value="data.name"
			@update:value="updateValue"
		/>
	</div>
	<TextInput
		label="Durée"
		placeholder="Depuis 2015"
		name="duration"
		:value="data.duration"
		@update:value="updateValue"
	/>
	<QuillEditor
		label="Détails"
		name="details"
		:value="data.details"
		@update:value="updateValue"
	/>
	<AlertBox classColor="alert-info">
		<p>Les détails de vos centres d'intérêt doivent être obligatoirement à l'indicatif</p>
	</AlertBox>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import apiClient from '@/services/api.js';
import CardTitle from '../global/CardTitle.vue';
import TextInput from '../input/TextInput.vue';
import AlertBox from '../global/AlertBox.vue';
import ExitDetailButton from '../button/ExitDetailButton.vue';
import SelectInput from '../input/SelectInput.vue';
import QuillEditor from '../input/QuillEditor.vue';

const data = reactive({});

const props = defineProps({
	item_id: Number
});

const emit = defineEmits(['close']);
const handleClick = () => {
	emit('close');
};

const updateValue = async ({name, value}) => {
	try {
		let sendData = {[name]: value,}
		if (name === 'company') {
			data.company = value;
		}
		await apiClient.put(`/cv_hobbie/update/${props.item_id}/`, sendData);
	} catch (error) {
		console.error('Error updating item data:', error);
	}
};

const fetchLangData = async () => {
	try {
		const response = await apiClient.get(`/cv_hobbie/item/${props.item_id}/`);
		Object.assign(data, response.data);
	} catch (error) {
		console.error('Error fetching item data:', error);
	}
};

onMounted(() => {
	fetchLangData();
});
</script>