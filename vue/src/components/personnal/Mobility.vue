<template>
	<SubSectionLayout>
		<CardTitle>Mobilité</CardTitle>
		<div class="col-span-full grid grid-cols-2 gap-md">
			<SelectInput
				label="Permis de conduire"
				name="license"
				:value="data.license"
				:items="data.license_choices"
				@update:value="updateValue"
			/>
			<CheckBoxInput
				v-if="data.license !== 'Aucun'"
				label="Véhicule"
				name="has_vehicle"
				:checked="data.has_vehicle"
				@update:value="updateValue"
			/>
		</div>
		<div class="max-w-[400px] grid gap-md">
			<TextInput
				v-if="data.license === 'Autre'"
				label="Autre permis"
				placeholder="Permis"
				name="other_license"
				:value="data.other_license"
				@update:value="updateValue"
			/>
			<TextInput
				label="Champ de mobilité"
				placeholder="Départemental, régional, national, etc."
				name="range"
				:value="data.range"
				@update:value="updateValue"
			/>
		</div>
		<AlertBox classColor="alert-info">
			Le champ de mobilité indique votre rayon de déplacement (ex : département, région, etc.).
		</AlertBox>
	</SubSectionLayout>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import apiClient from '@/services/api';
import SubSectionLayout from '../layout/SubSectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import AlertBox from '../global/AlertBox.vue';
import TextInput from '../input/TextInput.vue';
import SelectInput from '../input/SelectInput.vue';
import CheckBoxInput from '../input/CheckBoxInput.vue';

const data = reactive({});

const updateValue = async ({name, value}) => {
	try {
		let sendData = {[name]: value}
		await apiClient.put('/cv_personnal/fields/', sendData);
		data[name] = value;
	} catch (error) {
		console.error(error);
	}
};

const fetchData = async () => {
	try {
		const response = await apiClient.get('/cv_personnal/mobility/');
		Object.assign(data, response.data);
	} catch (error) {
		console.error('Erreur lors de la récupération des informations de mobilité :');
	}
};

onMounted(() => {
	fetchData();
});
</script>