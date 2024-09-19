import { defineStore } from 'pinia';

export const useTemplateStore = defineStore('template', {
	state: () => ({
		primary: '',
		secondary: '',
		third: '',
		dark: '',
		light: '',
        head: '',
        title: '',
        subtitle: '',
        body: ''
	}),
	actions: {
        setProperty(name, value) {
            if (this[name] !== undefined) {
                this[name] = value;
            } else {
                console.error(`Unknown property: ${name}`);
            }
        },
	},
});