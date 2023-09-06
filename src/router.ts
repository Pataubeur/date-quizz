import { createRouter, createWebHistory } from 'vue-router'
import Homepage from "./components/Home.vue";
import Index from "./components/Quiz.vue";
import Score from "./components/Score.vue";

export default createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: Homepage,
        },
        {
            path: '/quiz',
            component: Index,
        },
        {
            path: '/score',
            component: Score
        }
    ],
})