import { createRouter, createWebHistory } from 'vue-router'

import HomeView from "@/views/HomeView.vue";
import SettingsView from "@/views/SettingsView.vue";
import LoginView from "@/views/LoginView.vue";


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      name: "Home",
      path: "/",
      component: HomeView
    },
    {
      name: "Settings",
      path: "/settings",
      component: SettingsView
    },
    {
      name: "Login",
      path: "/login",
      component: LoginView
    }
  ]
})

export default router
