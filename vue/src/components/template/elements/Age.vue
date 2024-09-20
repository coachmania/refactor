<template>
	<h1 class="text-tpTitle">
        <span v-if="cvData.personnal.age">
            {{ cvData.personnal.age }} ans
        </span>
        <span v-if="cvData.personnal.birthdate">
			({{ cvData.personnal.birthdate }})
		</span>
	</h1>
</template>

<script setup>
import { useCvDataStore } from '@/store/cvDataStore';
const cvDataStore = useCvDataStore();
const cvData = cvDataStore.cvData;
</script>