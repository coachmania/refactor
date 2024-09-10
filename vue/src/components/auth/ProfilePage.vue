<template>
	<p v-if="authStore.isLogged">Vous êtes connecté en tant que {{ authStore.username }}</p>
	<p v-else>Vous n'êtes pas connecté.</p>
</template>

<script setup>
import { onMounted } from 'vue';
import { useAuthStore } from '@/store/authStore';

const authStore = useAuthStore();

onMounted(async () => {
	await authStore.profile();
});
</script>
