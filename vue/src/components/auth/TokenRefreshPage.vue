<template>
	<div>
		<p v-if="authStore.isLogged">Vous êtes connecté en tant que {{ authStore.username }}</p>
		<p v-else>REFRESH</p>
		<p>OKK</p>
	</div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useAuthStore } from '@/store/authStore';

const authStore = useAuthStore();

onMounted(async () => {
	await authStore.tokenRefresh();
});
</script>