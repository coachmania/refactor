import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './components/home/HomePage.vue';
import LoginPage from './components/login/LoginPage.vue';

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
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default router;