<template>
	<h1><slot></slot></h1>
	<p>{{ cvData.personnal.phone }}</p>
	<p>{{ cvData.personnal.email }}</p>
	<a class="block" :href="cvData.title.linkedin_url">Linkedin</a>
	<a class="block" :href="cvData.title.other_url">{{ cvData.title.other_url }}</a>
	<a class="block" :href="cvData.title.trimoji_url">Trimoji</a>
</template>

<script setup>
import { useCvDataStore } from '@/store/cvDataStore';
const cvDataStore = useCvDataStore();
const cvData = cvDataStore.cvData;
</script>