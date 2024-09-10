<template>
	<div class="card bg-base-200 border border-base-300">
		<div class="grid p-card gap-md">
			<h1 class="card-title">Titre du CV</h1>
			<TextInput
				text="Titre du poste recherché"
				placeholder="Ex: Développeur Web"
				name="title"
				:value="title"
				@update:value="handleValueChange"
			/>
			<QuillEditor/>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import TextInput from '../global/TextInput.vue';
import QuillEditor from '../global/QuillEditor.vue';

const title = ref('');

const fetchInitialData = async () => {
	try {
		const response = { data: { title: 'Développeur Full Stack' } };
		title.value = response.data.title;
		console.log('Initial data loaded:', title.value);
	} catch (error) {
		console.error('Erreur lors du chargement initial :', error);
	}
};

const handleValueChange = ({ name, value }) => {
	console.log(`${name}, ${value}`);
	// title.value = value;
};

onMounted(() => {
	fetchInitialData();
});
</script>