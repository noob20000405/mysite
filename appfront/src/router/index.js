import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Log from '@/components/Log'
import LogList from '@/components/LogList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
      children: [
        {
          path: ':id',
          name: 'LogList',
          component: LogList,
          props: true
        }
      ]
    },
  ]
})
