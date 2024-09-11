<template>
	<Header/>
	<EditorLayout>
		<SectionLayout>
			<Picture/>
			<Infos/>
		</SectionLayout>
	</EditorLayout>
</template>

<script setup>
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';
import Picture from './Picture.vue';
import Infos from './Infos.vue';
</script>