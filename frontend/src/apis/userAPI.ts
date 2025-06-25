import axios from "axios";
import { axiosConfig } from "./config/axiosConfig";
import { type UserType, type UpdateUserType } from "@/types/userTypes";

export const userAPI = {
    getCurrentUser: async () => {
        return (await axios.get<UserType>('/api/users/get', axiosConfig)).data
    },
    deleteUser: async (id: number) => {
        return (await axios.delete<UserType>(`/api/users/delete/${id}`, axiosConfig)).data
    },
    deleteCurrentUser: async () => {
        return (await axios.delete<UserType>(`/api/users/delete`, axiosConfig)).data
    },
    updateCurrentUser: async (data: UpdateUserType) => {
        return (await axios.put<UserType>(`/api/users/update`, data, axiosConfig)).data
    },
    updateUser: async (id: number, data: UpdateUserType) => {
        return (await axios.put<UserType>(`/api/users/update/${id}`, data, axiosConfig)).data
    },
    getUsersAll: async () => {
        return (await axios.get<UserType[]>('/api/users/get/all', axiosConfig)).data
    },
    getUser: async (id: number) => {
        return (await axios.get<UserType>(`/api/users/get/${id}`, axiosConfig)).data
    },
    updateUserRole: async (userId: number, roleId: number) => {
        return (await axios.put<UserType>(`/api/users/update/role/${userId}/${roleId}`, {}, axiosConfig)).data
    },
}
