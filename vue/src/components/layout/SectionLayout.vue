<template>
	<section class="border-r border-base-300 p-md flex flex-col gap-md overflow-auto h-full">
		<slot name="cards"></slot>
	</section>
</template>

<script>
export default {
    name: 'SectionLayout',
};
</script>