<template>
	<div id="app">
		<Header/>
		<Home/>
	</div>
</template>

<script>
import Home from './Home.vue';
import Header from '../header/Header.vue';

export default {
	name: 'App',
	components: {
		Home,
		Header,
	},
};
</script>