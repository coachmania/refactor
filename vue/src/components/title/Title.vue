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
			<AlertBox
				v-if="type === 'Emploi'"
				text="Pour un emploi, utilisez le titre de l'offre si vous répondez à une annonce. Pour une candidature spontanée, indiquez clairement le poste que vous visez."
				classColor="alert-info"
			/>
			<AlertBox 
				v-else-if="type === 'Alternance'"
				text="Pour une alternance, mentionnez le poste ainsi que le rythme et la durée de l'alternance. Par exemple : 'Alternant Développeur Web - 3 jours école / 2 jours entreprise - 12 mois'."
				classColor="alert-info"
			/>
			<AlertBox
				v-else-if="type === 'Stage'"
				text="Pour un stage, précisez le titre du poste et, si possible, la durée du stage. Exemple : 'Stagiaire en Marketing Digital - 6 mois'."
				classColor="alert-info"
			/>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import TextInput from '../global/TextInput.vue';
import QuillEditor from '../global/QuillEditor.vue';
import AlertBox from '../global/AlertBox.vue';

const title = ref('');

const props = defineProps({
    type: String,
});

const fetchInitialData = async () => {
	try {
		const response = { data: { title: 'Développeur Full Stack' } };
		title.value = response.data.title;
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