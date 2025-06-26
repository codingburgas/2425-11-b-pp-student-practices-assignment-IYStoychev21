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

export default function ModelView() {
    const { id } = useParams();
    const navigate = useNavigate();

    const queryClient = useQueryClient()

    if (id === undefined) {
        navigate("/users")
    }

    const { data: user, error: errorUser, isLoading: isLoadingUser } = useQuery({
        queryKey: [`user-${id}`],
        queryFn: () => userAPI.getUser(+id!),
    })

    useEffect(() => {
        if (errorUser) {
            // @ts-expect-error The error the I return includes .response always
            if (errorUser.response.status === 401) {
                localStorage.removeItem('token')
                navigate('/users')
            }
        }
    }, [errorUser, navigate, user])

    useEffect(() => {
        setUserDataCopy(user)
    }, [user])

    const { data: currentUser, error: errorCurrentUser } = useQuery({
        queryKey: ['user'],
        queryFn: userAPI.getCurrentUser,
    })

    useEffect(() => {
        if (errorCurrentUser) {
            // @ts-expect-error The error the I return includes .response always
            if (errorCurrentUser.response.status === 401) {
                localStorage.removeItem('token')
                navigate('/')
            }
        }

    }, [errorCurrentUser, navigate, currentUser])

    const [userDataCopy, setUserDataCopy] = useState<UserType | undefined>(undefined)

    const handleUpdateUserData = (e: React.ChangeEvent<HTMLInputElement>): void => {
        setUserDataCopy(prev => ({
            ...prev!,
            [e.target.name]: e.target.value
        }))
    }

    const updateUserMutation = useMutation({
        mutationFn: (data: UpdateUserType) => userAPI.updateUser(user!.id, data),
        onSuccess: () => {
            toast.success(`${user!.username}'s account data has been updated`)
            queryClient.invalidateQueries({ queryKey: [`user-${id}`] })
        },
        onError: (error: ErrorType) => {
            toast.error(error.response.data.detail)
        }
    })

    const handleUpdateUser = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault()

        if (!userDataCopy) {
            toast.error("Please fill in all fields")
            return
        }

        const data = {
            first_name: userDataCopy.first_name,
            last_name: userDataCopy.last_name
        }

        updateUserMutation.mutate(data)
    }

    return (
        <>
            <AppSidebar />
            <SidebarInset className="overflow-x-hidden">
                <header className="flex h-16 shrink-0 items-center gap-2 border-b px-4 py-4">
                    <Breadcrumb>
                        <BreadcrumbList>
                            <BreadcrumbItem>
                                <BreadcrumbLink className="cursor-pointer" onClick={() => navigate('/users')}>Users</BreadcrumbLink>
                            </BreadcrumbItem>
                            <BreadcrumbSeparator>
                                <Slash />
                            </BreadcrumbSeparator>
                            <BreadcrumbItem>
                                {
                                    isLoadingUser ? <Skeleton className="w-24 h-4" /> :
                                        <BreadcrumbPage>{`${user!.first_name} ${user!.last_name}`}</BreadcrumbPage>
                                }
                            </BreadcrumbItem>
                        </BreadcrumbList>
                    </Breadcrumb>
                </header>

                {
                    currentUser != undefined ?
                        currentUser?.role.id === 2 &&
                        <div className="flex flex-col gap-5 p-6">
                            <form onSubmit={handleUpdateUser} className="flex flex-col gap-5 w-1/3">
                                {
                                    !userDataCopy ?
                                        <Skeleton className="h-10 w-full" /> :
                                        <div className="flex flex-col gap-2 w-full">
                                            <Label htmlFor="username">Username</Label>
                                            <Input value={userDataCopy.username} disabled className="w-full" id="username" placeholder="Username" name="username" />
                                        </div>
                                }
                                {
                                    !userDataCopy ?
                                        <Skeleton className="h-10 w-full" /> :
                                        <div className="flex flex-col gap-2 w-full">
                                            <Label htmlFor="first_name">First Name</Label>
                                            <Input onChange={handleUpdateUserData} value={userDataCopy.first_name} className="w-full" id="first_name" placeholder="First Name" name="first_name" />
                                        </div>
                                }
                                {
                                    !userDataCopy ?
                                        <Skeleton className="h-10 w-full" /> :
                                        <div className="flex flex-col gap-2 w-full">
                                            <Label htmlFor="last_name">Last Name</Label>
                                            <Input onChange={handleUpdateUserData} value={userDataCopy.last_name} className="w-full" id="last_name" placeholder="Last Name" name="last_name" />
                                        </div>
                                }

                                <Button type="submit">Save</Button>
                            </form>
                        </div> : null
                }

                {

                    isLoadingUser ? <Skeleton className="w-24 h-4" /> :
                        <h1 className="text-2xl m-4 mt-10">{`${user!.first_name} ${user!.last_name}'s predictions`}</h1>
                }
            </SidebarInset>
        </>
    )
}
