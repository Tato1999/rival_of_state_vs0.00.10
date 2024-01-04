import { createApp } from 'vue'
import App from './App.vue'
import router from './routers'; // Adjust the path accordingly
// import VueGoogleMaps from 'vue3-google-map'

import VueGoogleMaps from '@fawmi/vue-google-maps'
// use(VueGoogleMaps,{load:{key:'AIzaSyC3G3r10ptVNuk5HPhmHLFNqJoxlp4MZr0'}})

createApp(App).use(VueGoogleMaps, {
    load: {
        key: 'AIzaSyC3G3r10ptVNuk5HPhmHLFNqJoxlp4MZr0',
    }}).use(router).mount('#app')
