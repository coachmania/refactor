<template>
	<div>
		<h1><slot>Langues</slot></h1>
        <ul>
            <li v-for="(lang, index) in cvData.langs" :key="index">
				<template v-if="lang.name">{{ lang.name }}</template>
				<template v-if="lang.name && lang.level"> - </template>
				<template v-if="lang.level">{{ lang.level }}</template>
				<template v-if="lang.justification"> ({{ lang.justification }})</template>
            </li>
        </ul>
	</div>
</template>

<script setup>
import { useCvDataStore } from '@/store/cvDataStore';
const cvDataStore = useCvDataStore();
const cvData = cvDataStore.cvData;
</script>