<template>
	<div>
		<Header/>
		<h1>Login Page</h1>
		<LoginForm />
	</div>
</template>

<script>
import Header from '../header/Header.vue';
import LoginForm from './LoginForm.vue';

export default {
	name: 'LoginPage',
	components: {
		Header,
		LoginForm
	}
};
</script>