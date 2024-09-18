<template>
	<SubSectionLayout>
		<CardTitle>Photo</CardTitle>
		<div class="grid gap-md grid-cols-[auto,1fr]">
			<div class="h-full flex flex-col items-center gap-md">
				<PictureDisplay :data="data"/>
				<HideButton
					:data="data"
					@click="updateValue"
				/>
			</div>
			<DropZone @dropped="fetchData"/>
		</div>
	</SubSectionLayout>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import apiClient from '@/services/api';
import CardTitle from '../global/CardTitle.vue';
import PictureDisplay from './PictureDisplay.vue';
import HideButton from './HideButton.vue';
import DropZone from './DropZone.vue';
import SubSectionLayout from '../layout/SubSectionLayout.vue';

const data = reactive({});

const updateValue = async () => {
	try {
		await apiClient.put('/cv_personnal/update/', {
			is_hidden: !data.is_hidden,
		});
		data.is_hidden = !data.is_hidden;
	} catch (error) {
		console.error('Erreur lors de la mise à jour de la visibilité de la photo');
	}
};

const fetchData = async () => {
	try {
		const response = await apiClient.get('/cv_personnal/picture/');
		Object.assign(data, response.data);
	} catch (error) {
		console.error('Erreur lors de la récupération de l\'image');
	}
};

onMounted(() => {
	fetchData();
});
</script>