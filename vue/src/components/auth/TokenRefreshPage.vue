<template>
	<div>
		<p v-if="authStore.isLogged">Vous êtes connecté en tant que {{ authStore.username }}</p>
		<p v-else>REFRESH</p>
		<p>OKK</p>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useAuthStore } from '@/store/authStore';

const authStore = useAuthStore();
const errorMessage = ref(null);

onMounted(async () => {
    try {
        await authStore.tokenRefresh();
    } catch (error) {
        errorMessage.value = 'Token refresh failed';
        console.error('Token refresh failed:', error.response ? error.response.data : error);
    }
});
</script>