import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import './axios'
import './assets/css/style.css'
import { store } from './storage'
// window.axios = axios

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUsers, faUserPlus, faGlobe, faClipboardCheck, faChevronRight, faChevronLeft, faTrash } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faUsers, faUserPlus, faGlobe, faClipboardCheck, faChevronRight, faChevronLeft, faTrash )


/* add font awesome icon component */
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false



new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
