import AppSidebar from "@/components/Sidebar";
import { SidebarInset } from "@/components/ui/sidebar";
import {
    Breadcrumb,
    BreadcrumbItem,
    BreadcrumbList,
    BreadcrumbPage,
} from "@/components/ui/breadcrumb"
import { Button } from "@/components/ui/button";
import { useNavigate } from "react-router-dom";
import { Skeleton } from "@/components/ui/skeleton";

export default function Predictions() {
    const navigate = useNavigate()

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
            </SidebarInset>
        </>
    );
}
