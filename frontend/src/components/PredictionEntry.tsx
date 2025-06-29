import { type PredictionType } from "@/types/predictionTypes"
import { useState } from "react";
import { useQueryClient, useMutation } from "@tanstack/react-query";
import { useNavigate } from "react-router-dom";
import { predictionAPI } from "@/apis/predictionAPI";
import { toast } from "sonner";
import { type ErrorType } from "@/types/errorTypes";
import { Button } from "./ui/button";
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
import { DateTime } from 'luxon'
import { Badge } from "@/components/ui/badge"

export default function PredictionEntry({ prediction }: { prediction: PredictionType }) {
    const [isDeleting, setIsDeleting] = useState(false);
    const queryClient = useQueryClient()
    const navigate = useNavigate()

    const deletePredictionMutation = useMutation({
        mutationFn: predictionAPI.deletePrediction,
        onSuccess: () => {
            toast.success("Prediction has been deleted")
            queryClient.invalidateQueries({ queryKey: ['predictionsAll'] })
        },
        onError: (error: ErrorType) => {
            toast.error(error.response.data.detail);
        },
    });

    return (
        <>
            <div className="flex items-center">
                <div className="flex w-full items-center grow">
                    <p className="grow w-[1%] gap-2">{prediction.title}</p>
                    <p className="grow w-[1%] gap-2">{prediction.prediction ? <Badge className="px-4 py-2">Approaved</Badge> : <Badge className="px-4 py-2" variant="destructive">Rejected</Badge>}</p>
                    <p className="grow w-[1%] gap-2">{DateTime.fromISO(prediction.created_at).toFormat("HH:mm:ss")}</p>
                    <p className="grow w-[1%] gap-2">{DateTime.fromISO(prediction.created_at).toFormat("dd-MM-yyyy")}</p>
                </div>

                <div className="flex w-full items-center gap-8 justify-end">
                    <Button className="cursor-pointer" variant="secondary" onClick={() => { navigate(`/predictions/${prediction.id}`) }}>View</Button>
                    <Button className="cursor-pointer" variant="destructive" onClick={() => { setIsDeleting(true) }}>Delete</Button>
                </div>
            </div>
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
                        <AlertDialogAction onClick={() => { deletePredictionMutation.mutate(prediction.id) }}>Continue</AlertDialogAction>
                    </AlertDialogFooter>
                </AlertDialogContent>
            </AlertDialog>
        </>
    )
}
