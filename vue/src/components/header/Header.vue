<template>
	<nav class="navbar px-8 border-b border-base-300 bg-base-200">
		<div class="navbar-start">
			<a class="btn btn-ghost text-xl" href="#">
				<svg class="h-icon fill-primary" version="1.1" viewBox="0 0 191 191" xml:space="preserve" xmlns="http://www.w3.org/2000/svg"><g transform="translate(-211.91 10.824)"><path d="m291.75 179.16c-24.559-4.221-46.205-17.383-60.718-36.92-21.871-29.442-25.251-68.204-8.7828-100.74 14.614-28.876 42.302-48.048 74.751-51.762 29.173-3.3388 60.737 8.3728 80.35 29.814 34.108 37.287 34.066 93.026-0.0987 130.38-11.425 12.49-29.849 23.311-47.003 27.606-10.959 2.7445-27.85 3.4592-38.498 1.6292zm-1.8902-20.247c-9.1272-25.367-11.095-34.733-11.083-52.751 0.0116-17.362 1.5355-22.859 8.5422-30.812 5.9328-6.7341 12.592-9.5871 25.078-10.744 11.925-1.1048 14.108-1.6251 13.579-3.2369-0.51527-1.5701-8.1963-3.4428-19.869-4.8441-22.292-2.6764-39.694 3.9544-44.248 16.86-2.1299 6.0355-2.9682 21.393-1.7034 31.208 2.0887 16.211 8.6553 33.419 18.525 48.548 6.0606 9.2896 13.805 18.251 14.352 16.608 0.19195-0.57532-1.2364-5.4522-3.174-10.837zm38.704-46.736c17.901-3.7896 23.682-12.977 23.682-37.634 0-15.981-3.8779-31.625-11.718-47.271-6.7684-13.508-18.285-29.837-19.903-28.22-0.28747 0.28722 1.501 6.7461 3.9743 14.353 6.551 20.148 8.8306 31.039 9.3776 44.802 0.75176 18.916-2.5663 29.575-11.801 37.911-6.5004 5.8676-11.38 7.5479-24.468 8.4254-6.3304 0.42444-11.978 1.2389-12.549 1.81-1.4477 1.4464 4.737 3.7601 14.09 5.2712 4.1247 0.66638 8.1745 1.3437 8.9994 1.5052 4.125 0.80749 14.243 0.33324 20.315-0.95221z" stroke-width=".9995"/></g></svg>
				CVMania
			</a>
		</div>
		<div class="navbar-end">
				<!-- <form method="post" action="{% url 'logout' %}"> -->
					<!-- {% csrf_token %} -->
					<!-- <button type="submit" class="btn btn-ghost text-md">Se déconnecter</button> -->
				<!-- </form> -->
				<!-- <a href="{% url 'pageProfile' %}" class="btn btn-ghost text-md">Mes CV</a> -->

			<AuthButton/>
			<ToggleDarkModeButton/>
		</div>
	</nav>
</template>

<script>
import AuthButton from '@/components/auth/AuthButton.vue';
import ToggleDarkModeButton from './ToggleDarkModeButton.vue';

export default {
	name: 'Header',
	components: {
		AuthButton,
		ToggleDarkModeButton,
	},
};
</script>