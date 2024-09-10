<template>
	<div class="card bg-base-200 border border-base-300">
		<div class="grid p-card gap-md">
			<h1 class="card-title">Type de poste recherché</h1>
	
			<div class="join grid grid-cols-3">
				<button 
					v-for="(item, index) in typeChoices" 
					:key="index" 
                    :class="['btn join-item no-animation', {
						'btn-primary': item === type,
						'bg-base-100 border-base-content/15': item !== type
					}]"
					@click="updateType(item)"
				>
					{{ item }}
				</button>
			</div>

			<p class="text-base-content">Elias</p>
			
			<!-- <div role="alert" class="alert alert-info rounded-btn">
				{% if title.item.type == 'Emploi' %}
					{% include 'utils/alertBox.html' with text="Pour un emploi, utilisez le titre de l'offre si vous répondez à une annonce. Pour une candidature spontanée, indiquez clairement le poste que vous visez." %}
				{% elif title.item.type == 'Alternance' %}
					{% include 'utils/alertBox.html' with text="Pour une alternance, mentionnez le poste ainsi que le rythme et la durée de l'alternance. Par exemple : 'Alternant Développeur Web - 3 jours école / 2 jours entreprise - 12 mois'." %}
				{% elif title.item.type == 'Stage' %}
					{% include 'utils/alertBox.html' with text="Pour un stage, précisez le titre du poste et, si possible, la durée du stage. Exemple : 'Stagiaire en Marketing Digital - 6 mois'." %}
				{% endif %}
			</div> -->
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '@/services/api';

const typeChoices = ref([]);
const type = ref('');

const fetchTitleTypes = async () => {
	try {
		const response = await apiClient.get('/cv_title/type/');
		typeChoices.value = response.data.type_choices;
		type.value = response.data.type;
	} catch (error) {
		console.error('Error fetching title types:', error);
	}
};

const updateType = async (selectedType) => {
	type.value = selectedType;
	try {
		await apiClient.put('/cv_title/type/', {type: type.value});
	} catch (error) {
		console.error('Error updating title type:', error);
	}
};

onMounted(() => {
	fetchTitleTypes();
});
</script>