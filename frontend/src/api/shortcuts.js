import axios from 'axios'

const httpClient = axios.create({
    baseURL: "http://localhost:5000/",
    headers: {
        "Content-Type": "application/json",
    },
});


const obtainToken = (username, password) => {
    return httpClient.post('/api/v1/login', { username, password },)
}

const verifyToken = (token) => {
    httpClient.defaults.headers.common['Authorization'] = `Bearer ${token}`
    return httpClient.post('/api/v1/verify')
}

const registerUser = (username, password) => {
    return httpClient.post('/api/v1/register', { username, password })
}

const getCategoriesByUser = (currentUser) => {
    return httpClient.get('/api/v1/categories' + `?user=${currentUser}`)
}

const getActionsByUser = (currentUser) => {
    return httpClient.get('/api/v1/actions' + `?user=${currentUser}`)
}

const createActionByUser = (payload) => {
    return httpClient.post('/api/v1/actions', payload)
}

export { obtainToken, verifyToken, registerUser, getCategoriesByUser, getActionsByUser, createActionByUser }