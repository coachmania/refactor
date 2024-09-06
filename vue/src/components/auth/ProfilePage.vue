<template>
	<div>
		<p v-if="authStore.isLogged">Vous êtes connecté en tant que {{ authStore.username }}</p>
		<p v-else>Vous n'êtes pas connecté.</p>
	</div>
</template>

<script setup>
import { useAuthStore } from '@/store/authStore';

const authStore = useAuthStore();

// TODO
console.log(authStore.profile());
</script>
