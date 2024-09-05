<template>
	<div>
		<div class="grid grid-rows-[auto,1fr] h-screen">
			<Header/>
			<div class="grid place-items-center h-full">
				<LoginForm />
			</div>
		</div>
	</div>
</template>

<script>
import { defineComponent } from 'vue';
import Header from '../header/Header.vue';
import LoginForm from './LoginForm.vue';

export default defineComponent({
	name: 'LoginPage',
	components: {
		Header,
		LoginForm
	}
});
</script>