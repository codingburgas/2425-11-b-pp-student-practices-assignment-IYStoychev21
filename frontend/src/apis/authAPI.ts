import axios from "axios";
import { axiosConfig } from "./config/axiosConfig";
import { type SignInType, type SignUpType } from "@/types/authTypes";

export const authAPI = {
    logIn: async (data: SignInType) => {
        return (await axios.post('/api/auth/login', data, axiosConfig)).data
    },
    signUp: async (data: SignUpType) => {
        return (await axios.post('/api/auth/register', data, axiosConfig)).data
    }
}
