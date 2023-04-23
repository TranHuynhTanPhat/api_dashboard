import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../components/layout/MainPage.vue'),
    children: [
      {
        path: '/dashboard',
        name: 'Dashboard',
        component: () => import('../components/views/Home/Dashboard.vue')
      },
      {
        path: '/changepassword',
        name: 'ChangePassword',
        component: () => import('../components/views/Authentication/ChangePassword.vue')
      },
      {
        path: '/profile',
        name: 'Profile',
        component: () => import('../components/views/Home/ProfilePage.vue')
      },
      {
        path: '/setting',
        name: 'Setting',
        component: () => import('../components/views/Home/SettingPage.vue')
      },
      {
        path: '/statistic',
        name: 'Statistic',
        component: () => import('../components/views/Home/StatisticPage.vue')
      },
      {
        path: '/table',
        name: 'Table',
        component: () => import('../components/views/Home/TablePage.vue')
      },

    ]
  },
  {
    path: '/auth',
    name: 'Auth',
    component: () => import('../components/layout/FullPage.vue'),
    children: [
      {
        path: 'login',
        name: 'Signin',
        component: () => import('../components/views/Authentication/LoginPage.vue')
      },
      {
        path: 'register',
        name: 'Signup',
        component: () => import('../components/views/Authentication/RegisterPage.vue')
      },
      {
        path: 'forgotpassword',
        name: 'ForgotPassword',
        component: () => import('../components/views/Authentication/ForgotPassword.vue')
      },

    ]
  }, {
    path: '/intro',
    name: 'Introduction',
    component: () => import('../components/views/Home/IntroPage.vue')
  },
  { path: '*', component: () => import('../components/views/errors/404.vue') }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
