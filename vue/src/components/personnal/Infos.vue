<template>
	<SubSectionLayout>
		<CardTitle>Informations personnelles</CardTitle>
		<div class="grid grid-cols-2 gap-md">
			<TextInput
				label="Prénom"
				placeholder="Jean"
				name="first_name"
				:value="data.first_name"
				@update:value="updateValue"
			/>
			<TextInput
				label="Nom"
				placeholder="Dupont"
				name="name"
				:value="data.name"
				@update:value="updateValue"
			/>
			<TextInput
				label="Téléphone"
				placeholder="06 12 34 56 78"
				name="phone"
				:value="data.phone"
				@update:value="updateValue"
			/>
			<TextInput
				label="Email"
				placeholder="jean@jobmania.fr"
				name="email"
				:value="data.email"
				@update:value="updateValue"
			/>
			<NumberInput
				label="Âge"
				placeholder="20"
				name="age"
				:value=data.age
				@update:value="updateValue"
				:min=0
				:max=150
			/>
			<!-- TODO replace by dateInput -->
			<TextInput
				label="Date de naissance"
				placeholder="01/01/2000"
				name="birthdate"
				:value="data.birthdate"
				@update:value="updateValue"
			/>
		</div>
	</SubSectionLayout>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import apiClient from '@/services/api';
import CardTitle from '../global/CardTitle.vue';
import TextInput from '../input/TextInput.vue';
import NumberInput from '../input/NumberInput.vue';
import SubSectionLayout from '../layout/SubSectionLayout.vue';

const data = reactive({});

const updateValue = async ({name, value}) => {
	try {
		let sendData = {[name]: value,}
		await apiClient.put('/cv_personnal/fields/', sendData);
	} catch (error) {
		console.error('Erreur lors de la mise à jour des informations personnelles :');
	}
};

const fetchData = async () => {
	try {
		const response = await apiClient.get('/cv_personnal/infos/');
		Object.assign(data, response.data);
	} catch (error) {
		console.error('Erreur lors de la récupération des informations personnelles :');
	}
};

onMounted(() => {
	fetchData();
});
</script>