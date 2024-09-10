<template>
	<div class="card bg-base-200 border border-base-300">
		<div class="grid p-card gap-md">
			<h1 class="card-title">Type de poste recherché</h1>
	
			<div class="join grid grid-cols-3">
				<!-- {% for type in title.types %} -->
					<button typeButton name="type" class="btn join-item no-animation btn-primary">{{ type }}</button>
					<button typeButton name="type" class="btn join-item no-animation bg-base-100 border-base-content/15">{{ type }}</button>
					<button typeButton name="type" class="btn join-item no-animation bg-base-100 border-base-content/15">{{ type }}</button>
				<!-- {% endfor %} -->
			</div>
			
			<!-- <div role="alert" class="alert alert-info rounded-btn">
				{% if title.item.type == 'Emploi' %}
					{% include 'utils/alertBox.html' with text="Pour un emploi, utilisez le titre de l'offre si vous répondez à une annonce. Pour une candidature spontanée, indiquez clairement le poste que vous visez." %}
				{% elif title.item.type == 'Alternance' %}
					{% include 'utils/alertBox.html' with text="Pour une alternance, mentionnez le poste ainsi que le rythme et la durée de l'alternance. Par exemple : 'Alternant Développeur Web - 3 jours école / 2 jours entreprise - 12 mois'." %}
				{% elif title.item.type == 'Stage' %}
					{% include 'utils/alertBox.html' with text="Pour un stage, précisez le titre du poste et, si possible, la durée du stage. Exemple : 'Stagiaire en Marketing Digital - 6 mois'." %}
				{% endif %}
			</div> -->
		</div>
	</div>
</template>

<script>
export default {
	name: 'Type',
};
</script>