<template>
	<div>
		<h1 v-if="cvData.personnal.license !== 'Aucun'">
			{{ cvData.personnal.license }}
			<template v-if="cvData.personnal.has_vehicle"> - Véhicule</template>
		</h1>
		<p v-if="cvData.personnal.range">Mobilité : {{ cvData.personnal.range }}</p>
	</div>
</template>

<script setup>
import { useCvDataStore } from '@/store/cvDataStore';
const cvDataStore = useCvDataStore();
const cvData = cvDataStore.cvData;
</script>