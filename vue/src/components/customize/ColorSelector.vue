<template>
	<h2>{{ displayName }}</h2>
	<div class="grid grid-cols-8 gap-2">
		<div v-for="color in colors">
			<button
				class="btn btn-ghost btn-block h-12 border border-base-content/15"
				:style="{ backgroundColor: color }"
				@click="handleClick(color)"
			></button>
			<p class="text-center">•</p>
		</div>
	</div>
</template>

<script setup>
import { computed } from 'vue';
import { useTemplateStore } from '@/store/templateStore';

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

const displayName = computed(() => names[props.name] || props.name);
const store = useTemplateStore();

const handleClick = (color) => {
	try {
		console.log(color);
		store.setColor(props.name, color);
		// TODO add update color call API
	} catch (error) {
		console.error(error);
	}
}
</script>