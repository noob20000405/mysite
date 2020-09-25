import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import LogList from '@/components/LogList'
import Editor from '@/components/Editor'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/home',
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
    {
      path: '/editor',
      name: 'Editor',
      component: Editor
    }
  ]
})
