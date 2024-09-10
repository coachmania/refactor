<template>
	<p>Déconnexion en cours...</p>
</template>

<script>
import { defineComponent, onMounted } from 'vue';
import { useAuthStore } from '@/store/authStore';
import { useRouter } from 'vue-router';

export default defineComponent({
	name: 'LogoutPage',
	setup() {
		const authStore = useAuthStore();
		const router = useRouter();

		onMounted(() => {
			authStore.logout();
			router.push('/login');
		});

		return {};
	}
});
</script>