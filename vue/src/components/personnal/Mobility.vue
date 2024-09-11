<template>
	<CardLayout>
		<CardTitle>Mobilité</CardTitle>
		<AlertBox classColor="alert-info">
			La mobilité indique votre rayon de déplacement (ex : département, région, etc.).
		</AlertBox>
	</CardLayout>
</template>

<script setup>
import CardLayout from '../layout/CardLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import AlertBox from '../global/AlertBox.vue';
import TextInput from '../input/TextInput.vue';
</script>