import { createRouter, createWebHistory } from "vue-router";
import { storeToRefs } from 'pinia';
import {userStore} from '../store/store.js';
import Home from "../views/Home.vue";
import MovieDetail from "../views/MovieDetails.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import AddMovie from "../views/CreateMovie.vue";
import Profile from "../views/Profile.vue";
const routes = [
    { path: "/",name:'Home', component: Home,meta: { requiresAuth: true } },
    { path: "/movie/:id", component: MovieDetail, props:true },
    { path: "/login", component: Login, props:true },
    { path: "/register", component: Register, props:true },
    { path: "/addmovie", component: AddMovie, meta: { requiresAuth: true } },
    {path:"/profile",component:Profile,meta:{requiresAuth:true}}
];

const history = createWebHistory();

const router = createRouter({
    history,
    routes,
});
router.beforeEach((to, from, next) => {
    const {islogged,user} = storeToRefs(userStore());
    if(to.matched.some(route => route.meta.requiresAuth)){
        if(islogged.value && user.value != null){
            next();
        }else{
            next('/login');
        }
    } else if (to.path === '/login' || to.path === '/register') {
        if (islogged.value) {
            next('/');
        } else {
            next();
        }
    }else if (to.path==='/addmovie'){
        if(islogged.value && user.rol=='admin'){
            next();
        }else{
            next('/');
        }
    }
    else{
        next();
    }
})

export default router;