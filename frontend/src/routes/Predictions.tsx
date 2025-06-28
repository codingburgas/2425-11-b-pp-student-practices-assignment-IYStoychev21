import AppSidebar from "@/components/Sidebar";
import { SidebarInset } from "@/components/ui/sidebar";
import {
    Breadcrumb,
    BreadcrumbItem,
    BreadcrumbList,
    BreadcrumbPage,
} from "@/components/ui/breadcrumb"
import { Skeleton } from "@/components/ui/skeleton";
import PredictionEntry from "@/components/PredictionEntry";
import { useQuery } from "@tanstack/react-query";
import { predictionAPI } from "@/apis/predictionAPI";

export default function Predictions() {
    const { data: predictionsAll, isLoading: isLoadingPredictionsAll } = useQuery({
        queryKey: ['predictionsAll'],
        queryFn: predictionAPI.getCurrentUserPredictions,
    })

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

                {
                    isLoadingPredictionsAll ?
                        <div>
                            <Skeleton className="h-10 m-4" />
                            <Skeleton className="h-10 m-4" />
                            <Skeleton className="h-10 m-4" />
                            <Skeleton className="h-10 m-4" />
                        </div>
                        :
                        <div className="flex p-6 flex-col gap-5">
                            <div className="flex items-center">
                                <div className="flex w-full items-center grow">
                                    <p className="grow w-[1%] gap-2">Title</p>
                                    <p className="grow w-[1%] gap-2">Status</p>
                                    <p className="grow w-[1%] gap-2">Time</p>
                                    <p className="grow w-[1%] gap-2">Date</p>
                                </div>

                                <div className="flex w-full items-center gap-8 justify-end"></div>
                            </div>

                            {
                                predictionsAll && predictionsAll.map((prediction) => {
                                    return (
                                        <PredictionEntry key={prediction!.id} prediction={prediction!} />
                                    )
                                })
                            }
                        </div>
                }
            </SidebarInset>
        </>
    );
}
