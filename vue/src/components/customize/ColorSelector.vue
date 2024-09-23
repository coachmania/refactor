<template>
	<h2>{{ displayName }}</h2>
	<div class="grid grid-cols-8 gap-2">
		<div v-for="color in colors">
			<button
				class="btn btn-ghost btn-block h-12 border border-base-content/15"
				:style="{ backgroundColor: color }"
				@click="handleClick(color)"
			></button>
			<p class="text-center" v-if="color === selectedColor">•</p>
		</div>
	</div>
</template>

<script setup>
import { computed } from 'vue';
import { useCvCustomizeStore } from '@/store/cvCustomizeStore';
import apiClient from '@/services/api';

const props = defineProps({
	colors: Object,
	name: String,
});

let names = {
	primary: 'Principale',
	secondary: 'Secondaire',
	third: 'Tertiaire',
	dark: 'Contenu sombre',
	light: 'Contenu clair',
}

const store = useCvCustomizeStore();
const selectedColor = computed(() => store.cvCustomize[props.name]);
const displayName = computed(() => names[props.name] || props.name);

const handleClick = async (color) => {
	try {
		store.cvCustomize[props.name] = color;
		await apiClient.put('/cv_settings/update/', {
			[props.name + '_color']: color
		});
	} catch (error) {
		console.error('Error updating color:', error);
	}
}
</script>