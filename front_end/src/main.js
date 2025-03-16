import { createApp } from 'vue'
import App from './App.vue'
import HomeCustom from './components/Home.vue'
import BlogCustom from './components/Blog.vue'
import ContactCustom from './components/Contact.vue'
import { createRouter, createMemoryHistory } from 'vue-router'

const routes = [
    {path:'/', component: HomeCustom},
    {path:'/blog',component: BlogCustom},
    {path:'/contact',component: ContactCustom}
  ]
  
const router = createRouter({
history: createMemoryHistory(),
routes
})

const app = createApp(App)
app.use(router)
app.mount('#app')