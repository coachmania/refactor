<template>
	<div v-if="!isLoading && cvData" class="box-border overflow-hidden w-full h-full grid grid-cols-[80mm,1fr] bg-tpPrimary text-tpBody">
		<aside class="p-10 rayClass">
			<div class="bg-tpLight h-full">
				<pre>{{ cvData }}</pre>
			</div>
		</aside>
	</div>
	<div v-else-if="isLoading">
		<p>Chargement des données du CV...</p>
	</div>
	<div v-else>
		<p>Erreur lors du chargement des données du CV</p>
	</div>
</template>

<script setup>
import { computed } from 'vue';
import { useCvDataStore } from '@/store/cvDataStore';

const cvDataStore = useCvDataStore();
const cvData = computed(() => cvDataStore.cvData);
const isLoading = computed(() => cvDataStore.isLoading);
</script>

<style scoped>
.rayClass {
	background: linear-gradient(-45deg, transparent 22.5%, #ffffff55 22.5%, #ffffff55 27.5%, transparent 27.5%, transparent 72.5%, #ffffff55 72.5%, #ffffff55 77.5%, transparent 77.5%);
	background-size: 20px 20px;
}
</style>