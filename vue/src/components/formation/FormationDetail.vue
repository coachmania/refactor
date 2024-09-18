<template>
	<div class="grid grid-cols-[1fr,auto]">
		<CardTitle>{{ data.location || 'Nouvelle formation' }}</CardTitle>
		<ExitDetailButton @click="handleClick"/>
	</div>
	<div class="grid grid-cols-2 gap-md">
		<TextInput
			label="Établissement"
			placeholder="Université"
			name="location"
			:value="data.location"
			@update:value="updateValue"
		/>
		<TextInput
			label="Diplôme"
			placeholder="Baccalauréat"
			name="title"
			:value="data.title"
			@update:value="updateValue"
		/>
		<TextInput
			label="Ville"
			placeholder="Lyon"
			name="city"
			:value="data.city"
			@update:value="updateValue"
		/>
		<!-- TODO replace by a select with bac+1+2 etc -->
		<TextInput
			label="Niveau d'études"
			placeholder="Bac+5"
			name="level"
			:value="data.level"
			@update:value="updateValue"
		/>
	</div>
	<br>
	<CardTitle>Dates</CardTitle>
	<DateBlock
		:data="data"
		@update:value="updateValue"
	/>
	<br>
	<CardTitle>Détails</CardTitle>
	<div class="grid grid-cols-2 gap-md">
		<QuillEditor
			label="Détails de la formation"
			name="details"
			:value="data.details"
			@update:value="updateValue"
		/>
	</div>
	<AlertBox classColor="alert-info">
		<p>Les détails de vos formations doivent être obligatoirement à l'indicatif</p>
	</AlertBox>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import apiClient from '@/services/api.js';
import CardTitle from '../global/CardTitle.vue';
import TextInput from '../input/TextInput.vue';
import AlertBox from '../global/AlertBox.vue';
import ExitDetailButton from '../button/ExitDetailButton.vue';
import QuillEditor from '../input/QuillEditor.vue';
import DateBlock from '../global/DateBlock.vue';

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
		await apiClient.put(`/cv_formation/update/${props.item_id}/`, sendData);
	} catch (error) {
		console.error('Error updating language data:', error);
	}
};

const fetchLangData = async () => {
	try {
		const response = await apiClient.get(`/cv_formation/item/${props.item_id}/`);
		Object.assign(data, response.data);
	} catch (error) {
		console.error('Error fetching language data:', error);
	}
};

onMounted(() => {
	fetchLangData();
});
</script>