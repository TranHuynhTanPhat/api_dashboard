import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:8000/'
axios.defaults.headers.common = { 'Authorization': `Bearer ${localStorage.getItem("access_token")}` }


export const REGISTER = 'user/register'
export const LOGIN = 'user/login'
export const CHART_DATA = "chart-data"
export const TODAY_USERS = "today-users"
export const NEW_CLIENTS = "new-clients"
export const STATE_OK = "status-success"
export const TOTAL_CHECK_TIME = "total-check-times"
export const GET_INSPECTION = "get-inspection"
export const GET_OH_STATISTIC = "id_statistic"
export const GET_PREDICT_STATISTIC ="predict_result_statistic"
export const GET_INSPECTION_DETAIL = "get-inspection-detail"
export const GET_INSPECTION_ALL_DETAILS = "get-inspection-all-details"
export const GET_USER = "users"
export const UPDATE_DELETE_USER = "user"
export const EXPORT_EXCEL_API = "download_api_data"
