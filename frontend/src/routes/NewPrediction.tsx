import AppSidebar from "@/components/Sidebar";
import { SidebarInset } from "@/components/ui/sidebar";
import {
    Breadcrumb,
    BreadcrumbItem,
    BreadcrumbList,
    BreadcrumbPage,
} from "@/components/ui/breadcrumb"
import { predictionAPI } from "@/apis/predictionAPI";
import { Button } from "@/components/ui/button";
import { useNavigate } from "react-router-dom";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { useState } from "react";
import { type PredictionInputType } from "@/types/predictionTypes";
import { Checkbox } from "@/components/ui/checkbox";
import { toast } from "sonner";
import { useMutation } from "@tanstack/react-query";
import { type ErrorType } from "@/types/errorTypes";
import { useQueryClient } from "@tanstack/react-query";

export default function NewPrediction() {
    const navigate = useNavigate()
    const queryClient = useQueryClient()

    const [predictionTitle, setPredictionTitle] = useState<string | undefined>(undefined)
    // @ts-ignore
    const [predictionInput, setPredictionInput] = useState<PredictionInputType | undefined>({ education: false, self_employed: false })

    const handlePredictionData = (e: React.ChangeEvent<HTMLInputElement>): void => {
        setPredictionInput(prev => ({
            ...prev!,
            [e.target.name]: e.target.value
        }))
    }

    const newPredictionMutation = useMutation({
        mutationFn: (data: PredictionInputType) => predictionAPI.createPrediction(data, predictionTitle!),
        onSuccess: () => {
            toast.success(`${predictionTitle} has been created`)
            queryClient.invalidateQueries({ queryKey: [`predictionsAll`] })
            navigate("/predictions")
        },
        onError: (error: ErrorType) => {
            toast.error(error.response.data.detail)
        }
    })

    const handleFormSubmition = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault()

        newPredictionMutation.mutate(predictionInput!)
    }

    return (
        <>
            <AppSidebar />

            <SidebarInset>
                <header className="flex h-16 shrink-0 items-center gap-2 border-b px-4 py-4">
                    <Breadcrumb>
                        <BreadcrumbList>
                            <BreadcrumbItem>
                                <BreadcrumbPage>Predictions</BreadcrumbPage>
                            </BreadcrumbItem>
                        </BreadcrumbList>
                    </Breadcrumb>
                </header>

                <h1 className="text-2xl m-4">Make new prediction</h1>

                <form onSubmit={handleFormSubmition} className="m-10 flex flex-col w-1/3 gap-5">
                    <div className="flex flex-col gap-2 w-full">
                        <Label htmlFor="predictionTitle">Prediction Title</Label>
                        <Input required onChange={(e: React.ChangeEvent<HTMLInputElement>) => { setPredictionTitle(e.target.value) }} className="w-full" id="predictionTitle" placeholder="Prediction Title" name="predictionTitle" />
                    </div>
                    <div className="flex flex-col gap-2 w-full">
                        <Label htmlFor="no_of_dependents">Number of Dependents</Label>
                        <Input required onChange={handlePredictionData} type="number" className="w-full" id="no_of_dependents" placeholder="Number of Dependents" name="no_of_dependents" />
                    </div>
                    <div className="flex gap-2 w-full">
                        <Label htmlFor="education">Education</Label>
                        <Checkbox onCheckedChange={(checked) => setPredictionInput((prev) => ({ ...prev!, education: !!checked }))} id="education" name="education" />
                    </div>
                    <div className="flex gap-2 w-full">
                        <Label htmlFor="self_employeed">Self Employeed</Label>
                        <Checkbox onCheckedChange={(checked) => setPredictionInput((prev) => ({ ...prev!, self_employed: !!checked }))} id="self_employeed" name="self_employeed" />
                    </div>
                    <div className="flex flex-col gap-2 w-full">
                        <Label htmlFor="income_amount">Income Amount</Label>
                        <Input required onChange={handlePredictionData} type="number" className="w-full" id="income_amount" placeholder="Income Amount" name="income_amount" />
                    </div>
                    <div className="flex flex-col gap-2 w-full">
                        <Label htmlFor="loan_amont">Loan Amount</Label>
                        <Input required onChange={handlePredictionData} type="number" className="w-full" id="loan_amont" placeholder="Loan Amount" name="loan_amont" />
                    </div>
                    <div className="flex flex-col gap-2 w-full">
                        <Label htmlFor="loan_amont_term">Loan Amont Term</Label>
                        <Input required onChange={handlePredictionData} type="number" className="w-full" id="loan_amont_term" placeholder="Loan Amont Term" name="loan_amont_term" />
                    </div>
                    <div className="flex flex-col gap-2 w-full">
                        <Label htmlFor="cibil_score">Credit Score</Label>
                        <Input required onChange={handlePredictionData} type="number" className="w-full" id="cibil_score" placeholder="Credit Score" name="cibil_score" />
                    </div>
                    <div className="flex flex-col gap-2 w-full">
                        <Label htmlFor="residential_assets_value">Residential Assets Value</Label>
                        <Input required onChange={handlePredictionData} type="number" className="w-full" id="residential_assets_value" placeholder="Residential Assets Value" name="residential_assets_value" />
                    </div>
                    <div className="flex flex-col gap-2 w-full">
                        <Label htmlFor="commercial_assets_value">Commercial Assets Value</Label>
                        <Input required onChange={handlePredictionData} type="number" className="w-full" id="commercial_assets_value" placeholder="Commercial Assets Value" name="commercial_assets_value" />
                    </div>
                    <div className="flex flex-col gap-2 w-full">
                        <Label htmlFor="luxury_assets_value">Luxury Assets Value</Label>
                        <Input required onChange={handlePredictionData} type="number" className="w-full" id="luxury_assets_value" placeholder="Luxury Assets Value" name="luxury_assets_value" />
                    </div>
                    <div className="flex flex-col gap-2 w-full">
                        <Label htmlFor="bank_asset_value">Bank Asset Value</Label>
                        <Input required onChange={handlePredictionData} type="number" className="w-full" id="bank_asset_value" placeholder="Bank Asset Value" name="bank_asset_value" />
                    </div>
                    <Button type="submit" className="cursor-pointer">Predict</Button>
                </form>

            </SidebarInset>
        </>
    )
}
