import AppSidebar from "@/components/Sidebar";
import { SidebarInset } from "@/components/ui/sidebar";
import {
    Breadcrumb,
    BreadcrumbItem,
    BreadcrumbLink,
    BreadcrumbList,
    BreadcrumbPage,
    BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { Slash } from "lucide-react";
import { useNavigate, useParams } from "react-router-dom";
import { useEffect } from "react";
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { toast } from "sonner";
import { Skeleton } from "@/components/ui/skeleton";
import { Button } from "@/components/ui/button";
import { useState } from "react";
import { userAPI } from "@/apis/userAPI";
import type { UserType, UpdateUserType } from "@/types/userTypes";
import { type ErrorType } from "@/types/errorTypes";
import { predictionAPI } from "@/apis/predictionAPI";
import { DateTime } from "luxon";
import { Badge } from "@/components/ui/badge"
import {
    AlertDialog,
    AlertDialogAction,
    AlertDialogCancel,
    AlertDialogContent,
    AlertDialogDescription,
    AlertDialogFooter,
    AlertDialogHeader,
    AlertDialogTitle,
} from "@/components/ui/alert-dialog"

export default function PredictionView() {
    const { id } = useParams();
    const navigate = useNavigate();

    const [isDeleting, setIsDeleting] = useState(false);

    const queryClient = useQueryClient()

    if (id === undefined) {
        navigate("/users")
    }


    const { data: user, isLoading: isLoadingUser, error: errorUser } = useQuery({
        queryKey: ['user'],
        queryFn: userAPI.getCurrentUser,
    })

    useEffect(() => {
        if (errorUser) {
            // @ts-expect-error The error the I return includes .response always
            if (errorUser.response.status === 401) {
                localStorage.removeItem('token')
                navigate('/')
            }
        }
    }, [errorUser, navigate])


    const { data: prediction, isLoading: isLoadingPrediction } = useQuery({
        queryKey: [`prediction-${id}`],
        queryFn: () => predictionAPI.getPrediction(+id!),
    })

    const numberFormat = new Intl.NumberFormat('fr-FR')

    const deletePredictionMutation = useMutation({
        mutationFn: predictionAPI.deletePrediction,
        onSuccess: () => {
            toast.success("Prediction has been deleted")
            queryClient.invalidateQueries({ queryKey: ['predictionsAll'] })
            navigate('/predictions')
        },
        onError: (error: ErrorType) => {
            toast.error(error.response.data.detail);
        },
    });

    return (
        <>
            <AppSidebar />
            <SidebarInset className="overflow-x-hidden">
                <header className="flex h-16 shrink-0 items-center gap-2 border-b px-4 py-4">
                    <Breadcrumb>
                        <BreadcrumbList>
                            <BreadcrumbItem>
                                <BreadcrumbLink className="cursor-pointer" onClick={() => navigate('/predictions')}>Predictions</BreadcrumbLink>
                            </BreadcrumbItem>
                            <BreadcrumbSeparator>
                                <Slash />
                            </BreadcrumbSeparator>
                            <BreadcrumbItem>
                                {
                                    isLoadingPrediction ? <Skeleton className="w-24 h-4" /> :
                                        <BreadcrumbPage>{prediction?.title}</BreadcrumbPage>
                                }
                            </BreadcrumbItem>
                        </BreadcrumbList>
                    </Breadcrumb>
                </header>
                {
                    prediction &&
                    <>
                        {
                            user ?
                                user.id === prediction.user.id &&
                                <div className="flex m-6 gap-6">
                                    <Button variant="destructive" onClick={() => { setIsDeleting(true) }} className="w-fit px-6 py-4 cursor-pointer">Delete</Button>
                                </div> : null
                        }

                        <div className="flex flex-col gap-5 p-6">
                            <h1>About the Prediction</h1>
                            <div className="flex flex-col gap-3 p-6 pt-0">
                                <p>Title: {prediction?.title}</p>
                                <p>Created At: {DateTime.fromISO(prediction?.created_at).toFormat("HH:mm:ss dd-MM-yyyy")}</p>
                                <div className="flex gap-2 items-center">
                                    <p>Prediction: </p>
                                    {
                                        prediction?.prediction ? <Badge className="px-4 py-2">Approaved</Badge> : <Badge className="px-4 py-2" variant="destructive">Rejected</Badge>
                                    }
                                </div>
                            </div>
                            <h1>Inputs</h1>
                            <div className="flex flex-col gap-3 p-6 pt-0">
                                <p>Number of Dependents: {prediction?.prediction_inputs.no_of_dependents}</p>
                                <p>Education: {prediction?.prediction_inputs.education ? "True" : "False"}</p>
                                <p>Self Employeed: {prediction?.prediction_inputs.self_employed ? "True" : "False"}</p>
                                <p>Income Amount: {numberFormat.format(prediction?.prediction_inputs.income_amount)}</p>
                                <p>Loan Amount: {numberFormat.format(prediction?.prediction_inputs.loan_amont)}</p>
                                <p>Loan Term: {prediction?.prediction_inputs.loan_amont_term} months</p>
                                <p>Credit Score: {prediction?.prediction_inputs.cibil_score}</p>
                                <p>Residential Assets Value: {numberFormat.format(prediction?.prediction_inputs.residential_assets_value)}</p>
                                <p>Commercial Assets Value: {numberFormat.format(prediction?.prediction_inputs.commercial_assets_value)}</p>
                                <p>Luxury Assets Value: {numberFormat.format(prediction?.prediction_inputs.luxury_assets_value)}</p>
                                <p>Bank Assets Value: {numberFormat.format(prediction?.prediction_inputs.bank_asset_value)}</p>
                            </div>
                        </div>

                    </>
                }
            </SidebarInset>

            <AlertDialog open={isDeleting} onOpenChange={setIsDeleting}>
                <AlertDialogContent>
                    <AlertDialogHeader>
                        <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
                        <AlertDialogDescription>
                            This action cannot be undone. This will permanently delete this
                            prediction
                        </AlertDialogDescription>
                    </AlertDialogHeader>
                    <AlertDialogFooter>
                        <AlertDialogCancel>Cancel</AlertDialogCancel>
                        <AlertDialogAction onClick={() => { deletePredictionMutation.mutate(prediction?.id!) }}>Continue</AlertDialogAction>
                    </AlertDialogFooter>
                </AlertDialogContent>
            </AlertDialog>
        </>
    )
}
