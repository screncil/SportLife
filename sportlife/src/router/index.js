import { createRouter, createWebHistory } from 'vue-router'

import HomeView from "@/views/HomeView.vue";
import SettingsView from "@/views/SettingsView.vue";
import LoginView from "@/views/LoginView.vue";
import ClientsView from "@/views/ClientsView.vue";
import AddClientView from "@/views/AddClientView.vue"


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
    },
    {
      name: "Clients",
      path: "/clients",
      component: ClientsView
    },
    {
      name: "Add Client",
      path: "/addclient",
      component: AddClientView
    }
  ]
})

export default router
