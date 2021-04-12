import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Fighter from '../views/Fighter.vue';
import FightCreator from '../views/FightCreator.vue';
import Lightweight_Rank from '../views/LightweightRank.vue';
import Heavyweight_Rank from '../views/HeavyweightRank.vue';
import Titan from '../views/TitanRank.vue';
import Event_List from '../views/Events.vue';


Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/fighter/:first_name", //Can be any name so long as it takes the prop name as seen here. 
    name: "fighter", //Can be any name
    component: Fighter, //Name of imported comp
    props: true //Required for this to work.
  },
  {
    path: "/createfighter",
    name: "FightCreator",
    component: FightCreator 
  },
  {
    path: '/lightweight',
    name: 'Lightweight_Rank',
    component: Lightweight_Rank
  },
  {
    path: '/heavyweight',
    name: 'Heavyweight_Rank',
    component: Heavyweight_Rank
  },
  {
    path: '/titan',
    name: 'Titan',
    component: Titan
  }, 
  {
    path: '/events',
    name: 'Event_List',
    component: Event_List
  },   

];

const router = new VueRouter({
  mode: "history",
  //base: process.env.BASE_URL,
  routes
});

export default router;
