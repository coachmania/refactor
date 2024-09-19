import { defineStore } from 'pinia';

export const useTemplateStore = defineStore('template', {
	state: () => ({
		primary: '',
		secondary: '',
		third: '',
		dark: '',
		light: '',
	}),
	actions: {
        setColor(name, color) {
            if (this[name] !== undefined) {
                this[name] = color;
            } else {
                console.error(`Unknown color type: ${name}`);
            }
        },
	},
});