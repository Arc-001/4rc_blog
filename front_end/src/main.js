import { createApp } from 'vue'
import App from './App.vue'
import HomeCustom from './components/Home.vue'
import BlogCustom from './components/Blog.vue'
import ContactCustom from './components/Contact.vue'
import { createRouter, createMemoryHistory } from 'vue-router'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
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