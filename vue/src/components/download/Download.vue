<template>
	<CardLayout>
		<CardTitle>Télécharger en PDF</CardTitle>
		<p>Téléchargez votre CV en PDF afin de conserver la mise en page et de faciliter son traitement par les systèmes de recrutement (ATS) utilisés par les recruteurs.</p>
		<TextButton text="Télécharger">
			<svg class="h-icon w-icon fill-current" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="m12 16 4-5h-3V4h-2v7H8z"></path><path d="M20 18H4v-7H2v7c0 1.103.897 2 2 2h16c1.103 0 2-.897 2-2v-7h-2v7z"></path></svg>
		</TextButton>
	</CardLayout>
</template>

<script setup>
import CardLayout from '../layout/CardLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import TextButton from '../button/TextButton.vue';
</script>