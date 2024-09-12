<template>
	<CardLayout>
		<CardTitle>Mobilité</CardTitle>
		<div class="col-span-full grid grid-cols-2 gap-md">
			<SelectInput
				label="Permis"
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
		<AlertBox classColor="alert-info">
			La mobilité indique votre rayon de déplacement (ex : département, région, etc.).
		</AlertBox>
	</CardLayout>
</template>

<script setup>
import apiClient from '@/services/api';
import CardLayout from '../layout/CardLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import AlertBox from '../global/AlertBox.vue';
import TextInput from '../input/TextInput.vue';
import SelectInput from '../input/SelectInput.vue';
import CheckBoxInput from '../input/CheckBoxInput.vue';

const props = defineProps({
	data: Object,
});

const emit = defineEmits(['update-data']);
const updateValue = async ({name, value}) => {
	try {
		let sendData = {[name]: value}
		await apiClient.put('/cv_personnal/fields/', sendData);
		props.data[name] = value;
		emit('update-data', props.data);
	} catch (error) {
		console.error(error);
	}
};
</script>