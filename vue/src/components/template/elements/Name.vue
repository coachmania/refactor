<template>
	<template v-if="props.splited">
		<h1 class="text-tpTitle">{{ cvData.personnal.first_name }}</h1>
		<h1 class="text-tpTitle">{{ cvData.personnal.name }}</h1>
	</template>
	<template v-else>
		<h1 class="text-tpTitle">{{ cvData.personnal.first_name }} {{ cvData.personnal.name }}</h1>
	</template>
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