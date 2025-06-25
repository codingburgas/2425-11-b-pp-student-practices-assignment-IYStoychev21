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
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { userAPI } from "@/apis/userAPI";
import { useEffect } from "react";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { useState } from "react";
import type { UserType } from "@/types/userTypes";
import { type ErrorType } from "@/types/errorTypes";
import { toast } from "sonner"
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

export default function Account() {

    const navigate = useNavigate()
    const queryClient = useQueryClient()

    const [userDataCopy, setUserDataCopy] = useState<UserType | undefined>(undefined)

    const { data: user, error: errorUser } = useQuery({
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

        setUserDataCopy(user)
    }, [errorUser, navigate, user])


    const [isDeleting, setIsDeleting] = useState(false);

    const handleUpdateUserData = (e: React.ChangeEvent<HTMLInputElement>): void => {
        setUserDataCopy(prev => ({
            ...prev!,
            [e.target.name]: e.target.value
        }))
    }

    const updateUserMutation = useMutation({
        mutationFn: userAPI.updateCurrentUser,
        onSuccess: () => {
            toast.success("You account data has been updated")
            queryClient.invalidateQueries({ queryKey: ['user', 'users'] })
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

    const deleteUserMutation = useMutation({
        mutationFn: userAPI.deleteCurrentUser,
        onSuccess: () => {
            toast.success("You account has been deleted")
            localStorage.removeItem("token")
            navigate('/')
        },
        onError: (error: ErrorType) => {
            toast.error(error.response.data.detail)
        }
    })

    return (
        <>
            <AppSidebar />

            <SidebarInset>
                <header className="flex h-16 shrink-0 items-center gap-2 border-b px-4 py-4">
                    <Breadcrumb>
                        <BreadcrumbList>
                            <BreadcrumbItem>
                                <BreadcrumbPage>Account</BreadcrumbPage>
                            </BreadcrumbItem>
                        </BreadcrumbList>
                    </Breadcrumb>
                </header>

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

                    <Button onClick={() => { setIsDeleting(true) }} variant="destructive" className="w-1/3">Delete Account</Button>
                </div>
            </SidebarInset >

            <AlertDialog open={isDeleting} onOpenChange={setIsDeleting}>
                <AlertDialogContent>
                    <AlertDialogHeader>
                        <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
                        <AlertDialogDescription>
                            This action cannot be undone. This will permanently delete your account from our servers.
                        </AlertDialogDescription>
                    </AlertDialogHeader>
                    <AlertDialogFooter>
                        <AlertDialogCancel>Cancel</AlertDialogCancel>
                        <AlertDialogAction onClick={() => { deleteUserMutation.mutate() }}>Continue</AlertDialogAction>
                    </AlertDialogFooter>
                </AlertDialogContent>
            </AlertDialog>
        </>
    )
}
