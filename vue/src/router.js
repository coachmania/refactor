import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './components/home/HomePage.vue';
import LoginPage from './components/auth/LoginPage.vue';
import LogoutPage from './components/auth/LogoutPage.vue';

const routes = [
	{
		path: '/',
		name: 'Home',
		component: HomePage
	},
	{
		path: '/login',
		name: 'Login',
		component: LoginPage
	},
	{
		path: '/logout',
		name: 'Logout',
		component: LogoutPage
	}
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default router;