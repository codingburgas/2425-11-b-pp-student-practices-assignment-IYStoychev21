export const axiosConfig = {
    baseURL: import.meta.env.VITE_BACKEND_URL,
    headers: {
        'Authorization': 'Bearer ' + localStorage.getItem('token')
    }
}
