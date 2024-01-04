// import { createRouter, createWebHistory} from 'vue-router'


// import Home from '../components/home.vue'
// import login from '../components/login.vue'
// import register from '../components/register.vue'
// import work from '../components/work.vue'
// import factory from '../components/factory_work.vue'
// import globalSearch from '../components/global_factory.vue'
// import localSearch from '../components/factory_Search_local.vue'
// import war from '../components/war.vue'
// import total from '../components/total_war.vue'
// import Fight from '../components/fight.vue'
// import menu from '../components/menu.vue'
// import profile from '../components/profile.vue'
// import region from '../components/region.vue'
// import map from '../components/map.vue'
// import state from '../components/state.vue'
// import test_storage from '../components/test_storage.vue'
// import config_factory from '../components/config_factory.vue'

// const routes = [
//     {
//         path: '/',
//         component : Home
//     },
//     {
//         path: '/menu',
//         component : menu
//     },
//     {
//         path: '/login',
//         component : login
//     },
//     {
//         path: '/register',
//         component : register
//     },
//     {
//         path: '/work',
//         component : work
//     },
//     {
//         path: '/work/factory',
//         component : factory
//     },
//     {
//         path: '/work/factory/global/search',
//         component : globalSearch
//     },,
//     {
//         path: '/work/factory/local/search',
//         component : localSearch
//     },
//     {
//         path: '/war',
//         component : war
//     },
//     {
//         path: '/war/total',
//         component : total
//     },
//     {
//         path: '/war/total/fight',
//         component : Fight
//     },
//     {
//         path: '/profile/:id',
//         name: 'profile',
//         component : profile
//     },
//     {
//         path: '/map',
//         name: 'map',
//         component : map
//     },
//     {
//         path: '/region/:id',
//         name: 'region',
//         component : region
//     },
//     {
//         path: '/state',
//         name: 'state',
//         component : state
//     },
//     {
//         path: '/test',
//         name: 'test',
//         component : test_storage
//     },
//     {
//         path: '/edit/factory',
//         name: 'config_factory',
//         component : config_factory
//     },
// ]

// const basePath = window.location.pathname;

// const router = createRouter({
//     history: createWebHistory(basePath),
//     routes
// })

// export default router

import { createRouter, createWebHistory } from 'vue-router';

// Import your components
import Home from '../components/home.vue';
import login from '../components/login.vue';
import register from '../components/register.vue';
import work from '../components/work.vue';
import factory from '../components/factory_work.vue';
import globalSearch from '../components/global_factory.vue';
import localSearch from '../components/factory_Search_local.vue';
import war from '../components/war.vue';
import total from '../components/total_war.vue';
import Fight from '../components/fight.vue';
import menu from '../components/menu.vue';
import profile from '../components/profile.vue';
import region from '../components/region.vue';
import map from '../components/map.vue';
import state from '../components/state.vue';
import test_storage from '../components/test_storage.vue';
import config_factory from '../components/config_factory.vue';
import party from '../components/party.vue';
import party_region from '../components/regional_party.vue';
import parlament_election from '../components/parlament_election.vue';

// Dynamically detect the base path
const basePath = window.location.pathname;

const routes = [
  {
    path: '/',
    component: Home,
  },
  {
    path: `${basePath}/menu`,
    component: menu,
  },
  {
    path: `${basePath}/login`,
    component: login,
  },
  {
    path: `${basePath}/register`,
    component: register,
  },
  {
    path: `${basePath}/work`,
    component: work,
  },
  {
    path: `${basePath}/work/factory`,
    component: factory,
  },
  {
    path: `${basePath}/work/factory/global/search`,
    component: globalSearch,
  },
  {
    path: `${basePath}/work/factory/local/search`,
    component: localSearch,
  },
  {
    path: `${basePath}/war`,
    component: war,
  },
  {
    path: `${basePath}/war/total`,
    component: total,
  },
  {
    path: `${basePath}/war/total/fight`,
    component: Fight,
  },
  {
    path: `${basePath}/profile/:id`,
    name: 'profile',
    component: profile,
  },
  {
    path: `${basePath}/map`,
    name: 'map',
    component: map,
  },
  {
    path: `${basePath}/region/:id`,
    name: 'region',
    component: region,
  },
  {
    path: `${basePath}/state`,
    name: 'state',
    component: state,
  },
  {
    path: `${basePath}/test`,
    name: 'test',
    component: test_storage,
  },
  {
    path: `${basePath}/edit/factory`,
    name: 'config_factory',
    component: config_factory,
  },
  {
    path: `${basePath}/state/:id`,
    name: 'state',
    component: state,
  },
  {
    path: '/party/:id',
    name: 'party',
    component: party
  },
  {
    path: '/party/region/:id',
    name: 'party_region',
    component: party_region
  },
  {
    path: '/parlament/election/:id',
    name: 'parlament_election',
    component: parlament_election
  }
];


const router = createRouter({
  history: createWebHistory(basePath),
  routes,
});


export default router;
