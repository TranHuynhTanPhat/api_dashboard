import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000/'



export const REGISTER = 'user/register'
export const LOGIN = 'user/login'
export const CHART_DATA = "chart-data"
export const TODAY_USERS = "today-users"