import Vue from 'vue'
import Vuex from 'vuex'
import jwt_decode from 'jwt-decode'
import { obtainToken, verifyToken } from '@/api/shortcuts'
import createPersistedState from "vuex-persistedstate";
Vue.use(Vuex)

const KEY_PREFIX = 'ijra';



export default new Vuex.Store({
  state: {
    validToken: null,
    accessToken: null,
    user: null,
    usersActions: [],
    backlogArray: [],
    todoActionsArray: [],
    almostThereActionsArray: [],
    doneActionsArray: [],
    reviewActionsArray: [],
    refactorActionsArray: [],
  },
  getters: {
    currentUser(state) {
      return state.user
    },
    usersActions(state) {
      return state.usersActions
    },
    backlog(state) {
      return state.backlogArray
    },
    todoActions(state) {
      return state.todoActionsArray
    },
    almostThere(state) {
      return state.almostThereActionsArray
    },
    doneActions(state) {
      return state.doneActionsArray
    },
    reviewActions(state) {
      return state.reviewActionsArray
    },
    refactorActionsArray(state) {
      return state.refactorActionsArray
    }
  },
  mutations: {
    setAccessToken(state, token) {
      // console.log(token)
      localStorage.setItem('ijra_accessToken', token)
      state.accessToken = token
      state.validToken = true

    },
    isTokenValid(state, valid) {
      state.validToken = valid
    },
    authorizeUser(state) {
      const decodedToken = jwt_decode(localStorage.getItem('ijra_accessToken'))
      state.user = { "id": decodedToken.user_id, "username": decodedToken.username }
    },
    logout(state) {
      state.user = null
      state.accessToken = null
      localStorage.removeItem('ijra_accessToken')
    },
    setUsersActions(state, array) {
      state.usersActions = array
    },
    setBacklog(state, array) {
      state.backlogArray = array
    },
    setTodoActions(state, array) {
      state.todoActionsArray = array
    },
    setAlmostThere(state, array) {
      state.almostThereActionsArray = array
    },
    setDoneActions(state, array) {
      state.doneActionsArray = array
    },
    setReviewActions(state, array) {
      state.reviewActionsArray = array
    },
    setRefactorActionsArray(state, array) {
      state.refactorActionsArray = array
    }
  },
  actions: {
    getAccessToken({ commit }, payload) {
      return obtainToken(payload['username'], payload['password']).then((response) => {
        if (response.status === 200) {
          commit('setAccessToken', response.data["access_token"])
          commit('authorizeUser')
        }
      })
    },
    isTokenValid({ commit }) {
      return verifyToken(localStorage.getItem('ijra_accessToken')).then((response) => {
        console.log(response.status)
        if (response.status === 200) {
          commit('isTokenValid', true)
        }
      })
    },


  },
  plugins: [
    createPersistedState({
      storage: {
        getItem: (key) => localStorage.getItem(KEY_PREFIX + key),
        setItem: (key, value) => localStorage.setItem(KEY_PREFIX + key, value),
        removeItem: (key) => localStorage.removeItem(KEY_PREFIX + key),
      },
    }),
  ],
})
