<template>
	<div v-if="!isLogged">
		<button @click="handleAuthAction" class="btn btn-ghost">
			Se connecter
		</button>
	</div>
</template>

<script>
import { defineComponent, computed } from 'vue';
import { useAuthStore } from '@/store/authStore';

// TODO voir la gestion de l'etat de connexion
export default defineComponent({
	name: 'AuthButton',
	setup() {
		const authStore = useAuthStore();
		const isLogged = computed(() => authStore.isLogged);

		function handleAuthAction() {
			if (!isLogged.value) {
				this.$router.push('/login');
			}
		};

		return {
			isLogged,
			handleAuthAction
		};
	}
});
</script>