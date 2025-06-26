import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { userAPI } from "@/apis/userAPI";
import { useQuery } from "@tanstack/react-query";

import UserEntry from "@/components/UserEntry";

import AppSidebar from "@/components/Sidebar";
import { SidebarInset } from "@/components/ui/sidebar"
import { Skeleton } from "@/components/ui/skeleton";
import {
    Breadcrumb,
    BreadcrumbItem,
    BreadcrumbList,
    BreadcrumbPage,
} from "@/components/ui/breadcrumb"

export default function UserManagment() {
    const navigate = useNavigate();

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

    const { data: usersAll, isLoading: isLoadingUsersAll } = useQuery({
        queryKey: ['usersAll'],
        queryFn: userAPI.getUsersAll,
    })

    return (
        <>
            <AppSidebar />
            <SidebarInset>
                <header className="flex h-16 shrink-0 items-center gap-2 border-b px-4 py-4">
                    <Breadcrumb>
                        <BreadcrumbList>
                            <BreadcrumbItem>
                                <BreadcrumbPage>User Management</BreadcrumbPage>
                            </BreadcrumbItem>
                        </BreadcrumbList>
                    </Breadcrumb>
                </header>

                {
                    isLoadingUsersAll ?
                        <div>
                            <Skeleton className="h-10 m-4" />
                            <Skeleton className="h-10 m-4" />
                            <Skeleton className="h-10 m-4" />
                            <Skeleton className="h-10 m-4" />
                        </div>
                        :
                        <div className="flex p-6 flex-col gap-5">
                            {
                                usersAll && usersAll.map((user) => {
                                    return (
                                        <UserEntry key={user!.id} user={user!} />
                                    )
                                })
                            }
                        </div>
                }
            </SidebarInset>
        </>
    );
}
