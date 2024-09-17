<template>
	<div class="h-36 w-36 min-h-36 min-w-36 flex items-center justify-center rounded-xl overflow-hidden shadow-sm bg-base-200">
		<template v-if="isHidden">
			<svg class="fill-current h-12 w-12" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 19c.946 0 1.81-.103 2.598-.281l-1.757-1.757c-.273.021-.55.038-.841.038-5.351 0-7.424-3.846-7.926-5a8.642 8.642 0 0 1 1.508-2.297L4.184 8.305c-1.538 1.667-2.121 3.346-2.132 3.379a.994.994 0 0 0 0 .633C2.073 12.383 4.367 19 12 19zm0-14c-1.837 0-3.346.396-4.604.981L3.707 2.293 2.293 3.707l18 18 1.414-1.414-3.319-3.319c2.614-1.951 3.547-4.615 3.561-4.657a.994.994 0 0 0 0-.633C21.927 11.617 19.633 5 12 5zm4.972 10.558-2.28-2.28c.19-.39.308-.819.308-1.278 0-1.641-1.359-3-3-3-.459 0-.888.118-1.277.309L8.915 7.501A9.26 9.26 0 0 1 12 7c5.351 0 7.424 3.846 7.926 5-.302.692-1.166 2.342-2.954 3.558z"></path></svg>
		</template>
		<template v-else-if="profilePicture">
			<img class="w-full h-full object-cover object-center" :src="picture_url"/>
		</template>
		<template v-else>
			<svg class="fill-current h-12 w-12" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 2a5 5 0 1 0 5 5 5 5 0 0 0-5-5zm0 8a3 3 0 1 1 3-3 3 3 0 0 1-3 3zm9 11v-1a7 7 0 0 0-7-7h-4a7 7 0 0 0-7 7v1h2v-1a5 5 0 0 1 5-5h4a5 5 0 0 1 5 5v1z"></path></svg>
		</template>
	</div>
</template>

<script setup>
// TODO call api et voir pour mettre l'url en props
const profilePicture = true;
const picture_url = 'https://plus.unsplash.com/premium_photo-1698081929827-28c48d81b890?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cGljdHVyZXxlbnwwfHwwfHx8MA%3D%3D';

const props = defineProps({
	isHidden: Boolean,
});
</script>