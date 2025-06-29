import axios from "axios";
import { axiosConfig } from "./config/axiosConfig";
import { type PredictionType, type PredictionInputType } from "@/types/predictionTypes";

export const predictionAPI = {
    createPrediction: async (predictionData: PredictionInputType) => {
        return (await axios.post<PredictionType>(`/api/predictions/predict`, predictionData, axiosConfig)).data
    },
    getCurrentUserPredictions: async () => {
        return (await axios.get<PredictionType[]>(`/api/predictions/get/all`, axiosConfig)).data
    },
    getUserPredictions: async (userId: number) => {
        return (await axios.get<PredictionType[]>(`/api/predictions/get/all/${userId}`, axiosConfig)).data
    },
    getPrediction: async (predictionId: number) => {
        return (await axios.get<PredictionType>(`/api/predictions/get/${predictionId}`, axiosConfig)).data
    },
    deletePrediction: async (predictionId: number) => {
        return (await axios.delete<PredictionType>(`/api/predictions/delete/${predictionId}`, axiosConfig)).data
    }
}
