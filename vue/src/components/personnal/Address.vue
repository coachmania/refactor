<template>
	<SubSectionLayout>
		<CardTitle>Adresse</CardTitle>
		<div class="grid grid-cols-3 gap-md">
			<TextInput
				class="col-span-2"
				label="Complément d'adresse"
				placeholder="Arrêt de bus, étage, etc."
				name="additional"
				:value="data.additional"
				@update:value="updateValue"
			/>
			<!-- TODO change to char because of 01260 for ex -->
			<NumberInput
				label="Code postal"
				placeholder="69006"
				name="postal_code"
				:value="data.postal_code"
				@update:value="updateValue"
				:min=0
				:max=99999
			/>
		</div>
		<AlertBox classColor="alert-info">
			Dans un CV, on ne met pas l'adresse complète. Le complément d'adresse sert ici à indiquer un arrêt de bus, de métro, etc.
		</AlertBox>
		<div class="grid grid-cols-2 gap-md">
			<TextInput
				label="Ville"
				placeholder="Lyon"
				name="city"
				:value="data.city"
				@update:value="updateValue"
			/>
			<!-- TODO change to select country input champs hybrid libre ou parmis un liste (autocompletion) -->
			<TextInput
				label="Pays"
				placeholder="France"
				name="country"
				:value="data.country"
				@update:value="updateValue"
			/>
		</div>
	</SubSectionLayout>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import apiClient from '@/services/api';
import SubSectionLayout from '../layout/SubSectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import AlertBox from '../global/AlertBox.vue';
import TextInput from '../input/TextInput.vue';
import NumberInput from '../input/NumberInput.vue';

const data = reactive({});

const updateValue = async ({name, value}) => {
	try {
		let sendData = {[name]: value,}
		await apiClient.put('/cv_personnal/update/', sendData);
	} catch (error) {
		console.error('Erreur lors de la mise à jour de l\'adresse :');
	}
};

const fetchData = async () => {
	try {
		const response = await apiClient.get('/cv_personnal/address/');
		Object.assign(data, response.data);
	} catch (error) {
		console.error('Erreur lors de la récupération de l\'adresse :');
	}
};

onMounted(() => {
	fetchData();
});
</script>