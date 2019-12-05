import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../components/Home.vue";
import test from "../components/test.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/test',
    name: 'test',
    component: test,
  },
];

const router = new VueRouter({
  routes
});

export default router;
