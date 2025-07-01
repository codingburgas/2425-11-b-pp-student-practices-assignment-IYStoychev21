import AppSidebar from "@/components/Sidebar";
import { SidebarInset } from "@/components/ui/sidebar";
import {
    Breadcrumb,
    BreadcrumbItem,
    BreadcrumbList,
    BreadcrumbPage,
} from "@/components/ui/breadcrumb"
import { modelAPI } from "@/apis/modelAPI";
import { useQuery } from "@tanstack/react-query";
import ConfusionMatrix from "@/components/ConfusionMatrix";

export default function AboutTheModel() {

    const { data: model, isLoading: isLoadingModel } = useQuery({
        queryKey: ['model'],
        queryFn: modelAPI.getModelMetrics,
    })

    return (
        <>
            <AppSidebar />
            <SidebarInset className="overflow-x-hidden">
                <header className="flex h-16 shrink-0 items-center gap-2 border-b px-4 py-4">
                    <Breadcrumb>
                        <BreadcrumbList>
                            <BreadcrumbItem>
                                <BreadcrumbPage>About the Model</BreadcrumbPage>
                            </BreadcrumbItem>
                        </BreadcrumbList>
                    </Breadcrumb>
                </header>

                {
                    !isLoadingModel &&
                    <>
                        <div className="flex flex-col gap-5 p-6">
                            <h1>Model Metrics</h1>
                            <div className="flex flex-col gap-3 p-6 pt-0">
                                <p>Accuracy: {Math.round(model?.model_metrics.accuracy * 100) / 100}</p>
                                <p>Precision: {Math.round(model?.model_metrics.precision * 100) / 100}</p>
                                <p>F1 Score: {Math.round(model?.model_metrics.f1_score * 100) / 100}</p>
                                <p>Recall: {Math.round(model?.model_metrics.recall * 100) / 100}</p>
                                <div className="flex flex-col gap-2">
                                    <p>Confusion Matrix</p>
                                    <ConfusionMatrix matrix={model?.model_metrics.confusion_matrix!} labels={['Approaved', 'Rejected']} />
                                </div>
                            </div>
                            <h1>Test Train Split</h1>
                            <div className="flex flex-col gap-3 p-6 pt-0">
                                <p>Testing: {model?.test_train_split.testing! * 100}%</p>
                                <p>Training: {model?.test_train_split.training! * 100}%</p>
                            </div>
                            <h1>Hyper Parameters</h1>
                            <div className="flex flex-col gap-3 p-6 pt-0">
                                <p>Epochs: {model?.hyper_params.epochs}</p>
                                <p>Learning Rate: {model?.hyper_params.learning_rate}</p>
                            </div>
                        </div>
                    </>
                }

            </SidebarInset>
        </>
    )
}
