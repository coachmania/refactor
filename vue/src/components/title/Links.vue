<template>
	<CardLayout>
		<template v-slot:content>
			<CardTitle title="Liens"/>
			<UrlInput
				label="LinkedIn"
				placeholder="https://linkedin.com/in/coachmania"
				name="linkedin_url"
				:value="linkedin"
				@update:value="updateValue"
			/>
			<div class="grid grid-cols-2 gap-md">
				<UrlInput
					label="Autre site"
					placeholder="https://github.com/"
					name="other_url"
					:value="other"
					@update:value="updateValue"
				/>
				<UrlInput
					label="Trimoji"
					placeholder="https://trimoji.fr/"
					name="trimoji_url"
					:value="trimoji"
					@update:value="updateValue"
				/>
			</div>
		</template>
	</CardLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import CardLayout from '../layout/CardLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import UrlInput from '../input/UrlInput.vue';

const linkedin = ref('');
const other = ref('');
const trimoji = ref('');

const fetchInitialData = async () => {
	try {
		const response = { data: { linkedin: 'linke' } };
		linkedin.value = response.data.linkedin;
		other.value = response.data.other;
		trimoji.value = response.data.trimoji;
	} catch (error) {
		console.error('Erreur lors du chargement initial :', error);
	}
};

const updateValue = ({ name, value }) => {
	console.log(`${name}, ${value}`);
};

onMounted(() => {
	fetchInitialData();
});
</script>