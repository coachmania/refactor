import { defineStore } from 'pinia';

export const useThemeStore = defineStore('theme', {
	state: () => ({
		isDarkMode: localStorage.getItem('theme') === 'dark',
	}),
	actions: {
		toggleDarkMode() {
			this.isDarkMode = !this.isDarkMode;
			this.applyTheme();
		},
		applyTheme() {
			if (this.isDarkMode) {
				document.documentElement.setAttribute('data-theme', 'dark');
				localStorage.setItem('theme', 'dark');
			} else {
				document.documentElement.setAttribute('data-theme', 'light');
				localStorage.setItem('theme', 'light');
			}
		},
	},
});