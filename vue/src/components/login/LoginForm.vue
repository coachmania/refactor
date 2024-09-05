<template>
	<section class="card w-3/5 max-w-lg max-h-4/5 bg-base-200 border border-base-300 p-card gap-md">
		<h1 class="text-3xl">Bienvenue !</h1>
		<p>Connectez-vous pour accéder à vos CV et les modifier.</p>
		<form @submit.prevent="handleSubmit">
			<div>
				<label for="username" class="label label-text">Username</label>
				<div class="input input-bordered flex items-center gap-md">
					<svg class="fill-current pointer-events-none select-none" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M20 4H4c-1.103 0-2 .897-2 2v12c0 1.103.897 2 2 2h16c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2zm0 2v.511l-8 6.223-8-6.222V6h16zM4 18V9.044l7.386 5.745a.994.994 0 0 0 1.228 0L20 9.044 20.002 18H4z"></path></svg>
					<input type="username" id="username" name="username" v-model="username" class="grow" placeholder="jean.dupont@school.fr" required>
				</div>
			</div>
			<div>
				<label for="password" class="label label-text">Mot de passe</label>
				<div class="input input-bordered flex items-center gap-md">
					<svg class="fill-current pointer-events-none select-none" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 2C9.243 2 7 4.243 7 7v2H6c-1.103 0-2 .897-2 2v9c0 1.103.897 2 2 2h12c1.103 0 2-.897 2-2v-9c0-1.103-.897-2-2-2h-1V7c0-2.757-2.243-5-5-5zM9 7c0-1.654 1.346-3 3-3s3 1.346 3 3v2H9V7zm9.002 13H13v-2.278c.595-.347 1-.985 1-1.722 0-1.103-.897-2-2-2s-2 .897-2 2c0 .736.405 1.375 1 1.722V20H6v-9h12l.002 9z"></path></svg>
					<input type="password" id="password" name="password" v-model="password" class="grow" placeholder="••••••••" required>
				</div>
			</div>
			<div class="label">
				<span class="label-text-alt"></span>
				<label for="password" class="label label-text-alt">
					<a class="underline">Mot de passe oublié ?</a>
				</label>
			</div>
			<button type="submit" class="btn btn-primary btn-block">Se connecter</button>
			<p v-if="message">{{ message }}</p>
		</form>
	</section>
</template>

<script>
import { defineComponent } from 'vue';
import { useAuthStore } from '@/store/authStore';

export default defineComponent({
	name: 'LoginForm',
	data() {
		return {
			username: '',
			password: '',
			message: '',
		};
	},
	methods: {
		async handleSubmit() {
			const authStore = useAuthStore();
			try {
				await authStore.login(this.username, this.password);
				this.message = 'Login successful';
			} catch (error) {
				console.error('Login failed:', error.response.data);
				this.message = 'Login failed';
			}
		}
	}
});
</script>