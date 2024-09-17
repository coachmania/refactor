<template>
	<div class="grid grid-cols-[1fr,auto]">
		<CardTitle>{{ data.company || 'Nouvelle expérience' }}</CardTitle>
		<ExitDetailButton @click="handleClick"/>
	</div>
	<div class="max-w-[300px]">
		<TextInput
			label="Nom de la langue"
			placeholder="Anglais"
			name="name"
			:value="data.name"
			@update:value="updateValue"
		/>
	</div>
	<div class="max-w-[500px]">
		<TextInput
			label="Justification"
			placeholder="Voyage en Angleterre"
			name="justification"
			:value="data.justification"
			@update:value="updateValue"
		/>
	</div>
	<AlertBox classColor="alert-info">
		<p>La justification peut être une expérience à l'étranger ou une certification (ex : TOEIC).</p>
	</AlertBox>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import apiClient from '@/services/api.js';
import CardTitle from '../global/CardTitle.vue';
import TextInput from '../input/TextInput.vue';
import AlertBox from '../global/AlertBox.vue';
import ExitDetailButton from '../button/ExitDetailButton.vue';

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
		await apiClient.put(`/cv_experience/fields/${props.item_id}/`, sendData);
	} catch (error) {
		console.error('Error updating language data:', error);
	}
};

const fetchLangData = async () => {
	try {
		const response = await apiClient.get(`/cv_experience/item/${props.item_id}/`);
		console.log(response.data);
		
		Object.assign(data, response.data);
	} catch (error) {
		console.error('Error fetching language data:', error);
	}
};

onMounted(() => {
	fetchLangData();
});
</script>