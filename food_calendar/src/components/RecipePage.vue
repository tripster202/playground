<!-- RecipePage.vue -->
<template>
  <div class="recipe-page" :style="{ backgroundColor: pastelColors[recipe.id % 5] }">
    <h1>{{ recipe.title }}</h1>
    <div class="media-section">
      <img v-if="recipe.image" :src="recipe.image" alt="Recipe image">
      <iframe 
        v-if="recipe.videoId"
        :src="`https://www.youtube.com/embed/${recipe.videoId}`"
        frameborder="0"
        allowfullscreen
      ></iframe>
    </div>
    <div class="ingredients">
      <h2>Ingredients</h2>
      <ul>
        <li v-for="(ingredient, index) in recipe.ingredients" :key="index">
          {{ ingredient }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  props: ['id'],
  data() {
    return {
      pastelColors: ['#FFD1DC', '#C7F0D2', '#D4C4FB', '#FFE5B4', '#B5EAD7'],
      recipe: {} // Load actual recipe data based on ID
    }
  }
}
</script>