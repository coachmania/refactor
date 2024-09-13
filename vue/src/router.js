import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '@/store/authStore';

import HomePage from './components/home/HomePage.vue';
import PersonnalPage from './components/personnal/PersonnalPage.vue';
import CustomizePage from './components/customize/CustomizePage.vue';
import LangPage from './components/lang/LangPage.vue';
import ExperiencePage from './components/experience/ExperiencePage.vue';
import FormationPage from './components/formation/FormationPage.vue';
import TitlePage from './components/title/TitlePage.vue';
import LoginPage from './components/auth/LoginPage.vue';
import LogoutPage from './components/auth/LogoutPage.vue';
import ProfilePage from './components/auth/ProfilePage.vue';
import TokenRefreshPage from './components/auth/TokenRefreshPage.vue';

const routes = [
	{
		path: '/',
		component: HomePage,
	},
	{
		path: '/personnal',
		component: PersonnalPage,
	},
	{
		path: '/customize',
		component: CustomizePage,
	},
	{
		path: '/lang',
		component: LangPage,
	},
	{
		path: '/experience',
		component: ExperiencePage,
	},
	{
		path: '/formation',
		component: FormationPage,
	},
	{
		path: '/title',
		component: TitlePage,
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
	},
	{
		path: '/refresh',
		component: TokenRefreshPage,
	}
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default router;