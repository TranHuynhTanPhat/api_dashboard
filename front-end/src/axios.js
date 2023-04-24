import axios from 'axios'

axios.defaults.baseURL = 'http://0.0.0.0:8000/'
// axios.defaults.headers.common = {
//     "X-Requested-With": "XMLHttpRequest",
//     "X-CSRFToken": "example-of-custom-header",
//     "accept": "application/json",
//     "Content-Type": "application/json",
//     "Access-Control-Allow-Origin": "*"
// };

export const REGISTER = 'user/register'
export const LOGIN = 'user/login'
export const CHART_DATA = "chart-data"
export const TODAY_USERS = "today-users"
export const NEW_CLIENTS = "new-clients"
export const STATE_OK = "status-success"
export const TOTAL_CHECK_TIME = "total-check-times"
export const GET_INSPECTION = "get-inspection"
export const GET_INSPECTION_DETAIL = "get-inspection-detail"
export const GET_INSPECTION_ALL_DETAILS = "get-inspection-all-details"
export const GET_USER = "users"
