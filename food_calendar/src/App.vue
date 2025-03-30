<!-- App.vue -->
<template>
  <div class="app-container">
    <div class="meal-grid">
      <div 
        v-for="day in mealPlan" 
        :key="day.id"
        class="meal-card"
        :style="{ backgroundColor: pastelColors[day.id % 5] }"
      >
        <h3>{{ day.title }}</h3>
        <ul class="ingredient-list">
          <li v-for="(ingredient, index) in day.ingredients" :key="index">
            {{ ingredient }}
          </li>
        </ul>
        <router-link 
          :to="`/recipe/${day.id}`" 
          class="recipe-link"
        >
          View Recipe →
        </router-link>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pastelColors: ['#FFD1DC', '#C7F0D2', '#D4C4FB', '#FFE5B4', '#B5EAD7'],
      mealPlan: [
        {
          id: 1,
          title: 'Rainbow Veggie Stir-Fry',
          ingredients: ['Bell peppers', 'Broccoli', 'Carrots', 'Snap peas', 'Soy sauce']
        },
        // Add 6 more meal objects...
      ]
    }
  }
}
</script>

<style>
.app-container {
  padding: 2rem;
  min-height: 100vh;
  background: #f8f9fa;
}

.meal-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.meal-card {
  padding: 1.5rem;
  border-radius: 15px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
}

.meal-card:hover {
  transform: translateY(-5px);
}

.ingredient-list {
  list-style: none;
  padding: 0;
  margin: 1rem 0;
}

.ingredient-list li {
  padding: 0.5rem 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.3);
}

.recipe-link {
  display: inline-block;
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  background: white;
  border-radius: 20px;
  text-decoration: none;
  color: #2c3e50;
  font-weight: 500;
}
</style>