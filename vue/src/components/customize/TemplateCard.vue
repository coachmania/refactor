<template>
	<button class="relative rounded-btn overflow-hidden border border-base-300">
		<img class="object-cover object-center pointer-events-none" src="{% static 'mainApp/templates/' %}{{ template.name }}.png">
		<div class="pointer-events-none absolute inset-0 {% if customize.settings.template.id == template.id %}bg-primary/25{% endif %}">okkk</div>
	</button>
</template>

<script setup>
</script>