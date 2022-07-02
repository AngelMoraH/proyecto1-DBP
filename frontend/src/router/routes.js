import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/Home.vue";
import About from "../components/About.vue";
import MovieDetail from "../components/MovieDetails.vue";
const routes = [
    { path: "/", component: Home },
    { path: "/about", component: About },
    { path: "/movie/:id", component: MovieDetail, props:true }
];

const history = createWebHistory();

const router = createRouter({
    history,
    routes,
});

export default router;