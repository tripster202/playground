// main.js
import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: App },
    { path: '/recipe/:id', component: () => import('./components/RecipePage.vue') }
  ]
})

createApp(App).use(router).mount('#app')