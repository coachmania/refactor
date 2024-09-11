<template>
	<div v-if="!isLogged">
		<button @click="handleAuthAction" class="btn btn-ghost">
			Se connecter
		</button>
	</div>
</template>

<script setup>
import { computed } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/store/authStore';

const authStore = useAuthStore();
const isLogged = computed(() => authStore.isLogged);
const router = useRouter();

function handleAuthAction() {
	if (!isLogged.value) {
		router.push('/login');
	}
}
</script>