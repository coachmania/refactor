<template>
	<CardLayout>
		<CardTitle>Adresse</CardTitle>
		<AlertBox classColor="alert-info">
			Dans un CV, on ne met pas l'adresse complète. Le complément d'adresse sert ici à indiquer un arrêt de bus, de métro, etc.
		</AlertBox>
	</CardLayout>
</template>

<script setup>
import CardLayout from '../layout/CardLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import AlertBox from '../global/AlertBox.vue';
</script>