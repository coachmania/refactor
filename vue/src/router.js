import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '@/store/authStore';
import HomePage from './components/home/HomePage.vue';
import LoginPage from './components/auth/LoginPage.vue';
import LogoutPage from './components/auth/LogoutPage.vue';
import ProfilePage from './components/auth/ProfilePage.vue';

const routes = [
	{
		path: '/',
		component: HomePage,
	},
	{
		path: '/login',
		component: LoginPage
	},
	{
		path: '/logout',
		component: LogoutPage,
	},
	{
		path: '/profile',
		component: ProfilePage,
	}
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default router;