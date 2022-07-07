import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router/routes.js';

const pinia = createPinia()
pinia.use((context) => {
    const storeId = 'user'
    const serilizer = {
        serialize: JSON.stringify,
        deserialize: JSON.parse
    }
    const fromStorage = serilizer.deserialize(window.localStorage.getItem(storeId))

    if (fromStorage) {
        context.store.$patch(fromStorage)
    }

    context.store.$subscribe((mutation,state) => {
        
        const userState = {
            islogged: state.islogged,
            user: state.user,
            errorUser: state.errorUser,
            loadingUser: state.loadingUser
        }
        window.localStorage.setItem(storeId,serilizer.serialize(userState))
    })
})
createApp(App).use(pinia).use(router).mount('#app')
