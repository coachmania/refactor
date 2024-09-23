<template>
	<div v-if="props.splited">
		<h1>{{ cvData.personnal.first_name }}</h1>
		<h1>{{ cvData.personnal.name }}</h1>
	</div>
	<div v-else>
		<h1>{{ cvData.personnal.first_name }} {{ cvData.personnal.name }}</h1>
	</div>
</template>

<script setup>
import { useCvDataStore } from '@/store/cvDataStore';
const cvDataStore = useCvDataStore();
const cvData = cvDataStore.cvData;

const props = defineProps({
	splited: {
		type: Boolean,
		default: false
	}
});
</script>