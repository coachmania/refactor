<template>
	<CardLayout>
		<CardTitle>Mobilité</CardTitle>
		<AlertBox classColor="alert-info">
			La mobilité indique votre rayon de déplacement (ex : département, région, etc.).
		</AlertBox>
	</CardLayout>
</template>

<script setup>
import { onMounted } from 'vue';
import CardLayout from '../layout/CardLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import AlertBox from '../global/AlertBox.vue';
import TextInput from '../input/TextInput.vue';

const fetchInitialData = async () => {
	try {
		const response = {data: {mobility: 'mobility', licenses: ['Aucun', 'BSR', 'Permis A', 'Permis B', 'Autre']}};
	} catch (error) {
		console.error('Erreur lors du chargement initial :', error);
	}
};

onMounted(() => {
	fetchInitialData();
});
</script>