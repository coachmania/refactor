<template>
	<h2>{{ displayName }}</h2>
	<div class="grid grid-cols-8 gap-2">
		<button v-for="color in colors">
			<div
				class="btn btn-ghost btn-block h-12 border border-base-content/15"
				:style="{ backgroundColor: color }"
			></div>
			<p class="text-center">•</p>
		</button>
	</div>
</template>

<script setup>
import { computed } from 'vue';

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
</script>