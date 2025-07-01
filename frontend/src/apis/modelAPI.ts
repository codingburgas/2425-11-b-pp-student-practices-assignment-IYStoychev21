import axios from "axios";
import { axiosConfig } from "./config/axiosConfig";
import { type ModelType } from "@/types/modelTypes";

export const modelAPI = {
    getModelMetrics: async () => {
        return (await axios.get<ModelType>(`/api/models/get`, axiosConfig)).data
    }
}
