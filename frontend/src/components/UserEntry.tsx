import { useState, useEffect } from "react";
import { type UserType } from "@/types/userTypes";
import { Avatar, AvatarImage } from "./ui/avatar";
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
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select"
import { useQuery } from "@tanstack/react-query";
import { useNavigate } from "react-router-dom";


import { userAPI } from "@/apis/userAPI";
import { useMutation, useQueryClient } from "@tanstack/react-query";


import { toast } from "sonner";
import { type ErrorType } from "@/types/errorTypes";


export default function UserEntry({ user }: { user: UserType }) {
    const [isDeleting, setIsDeleting] = useState(false);
    const [isChangeRole, setIsChangeRole] = useState(false);
    const queryClient = useQueryClient()
    const navigate = useNavigate()

    const deleteUserMutation = useMutation({
        mutationFn: userAPI.deleteUser,
        onSuccess: () => {
            toast.success("User has been deleted")
            queryClient.invalidateQueries({ queryKey: ['usersAll'] })
        },
        onError: (error: ErrorType) => {
            toast.error(error.response.data.detail);
        },
    });

    const [selectedRole, setSelectedRole] = useState(`${user.role.id}`)

    const changeRoleMutation = useMutation({
        mutationFn: (roleId: string) => userAPI.updateUserRole(user.id, roleId),
        onSuccess: () => {
            toast.success("User role has been successfully updated")
            queryClient.invalidateQueries({ queryKey: ['usersAll'] })
        },
        onError: (error: ErrorType) => {
            toast.error(error.response.data.detail);
        },
    })

    const { data: currentUser, error: errorCurrentUser } = useQuery({
        queryKey: ['user'],
        queryFn: userAPI.getCurrentUser,
    })

    useEffect(() => {
        if (errorCurrentUser) {
            // @ts-expect-error The error the I return includes .response always
            if (errorUser.response.status === 401) {
                localStorage.removeItem('token')
                navigate('/')
            }
        }
    }, [errorCurrentUser, navigate, currentUser])

    return (
        <>
            <div className="flex items-center">
                <div className="flex w-full items-center grow">
                    <Avatar className="h-8 rounded-full w-8 mr-8">
                        <AvatarImage className="rounded-full" src={`https://ui-avatars.com/api/?name=${user.first_name + ' ' + user.last_name}&size=128&background=60494d&color=fff&bold=true`} alt={user.username} />
                    </Avatar>
                    <p className="grow w-[1%] gap-2">{user.first_name}</p>
                    <p className="grow w-[1%] gap-2">{user.last_name}</p>
                    <p className="grow w-[1%] gap-2">{user.username}</p>
                </div>

                <div className="flex w-full items-center gap-8 justify-end">
                    <Button className="cursor-pointer" variant="secondary" onClick={() => { navigate(`/users/${user.id}`) }}>View</Button>
                    {
                        currentUser != undefined ?
                            currentUser.role.id === 2 && <Button className="cursor-pointer" variant="secondary" onClick={() => { setIsChangeRole(true) }}>Change Role</Button>
                            : null
                    }
                    {
                        currentUser != undefined ?
                            currentUser.role.id === 2 && <Button className="cursor-pointer" variant="destructive" onClick={() => { setIsDeleting(true) }}>Delete</Button>
                            : null
                    }
                </div>
            </div>
            <AlertDialog open={isDeleting} onOpenChange={setIsDeleting}>
                <AlertDialogContent>
                    <AlertDialogHeader>
                        <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
                        <AlertDialogDescription>
                            This action cannot be undone. This will permanently delete this
                            account and remove your data from our servers.
                        </AlertDialogDescription>
                    </AlertDialogHeader>
                    <AlertDialogFooter>
                        <AlertDialogCancel>Cancel</AlertDialogCancel>
                        <AlertDialogAction onClick={() => { deleteUserMutation.mutate(user.id) }}>Continue</AlertDialogAction>
                    </AlertDialogFooter>
                </AlertDialogContent>
            </AlertDialog>

            <AlertDialog open={isChangeRole} onOpenChange={setIsChangeRole}>
                <AlertDialogContent>
                    <AlertDialogHeader>
                        <AlertDialogTitle>Change Role</AlertDialogTitle>
                    </AlertDialogHeader>

                    <Select defaultValue={`${user.role.id}`} onValueChange={setSelectedRole}>
                        <SelectTrigger className="w-[180px]">
                            <SelectValue />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem value="1">User</SelectItem>
                            <SelectItem value="2">Admin</SelectItem>
                        </SelectContent>
                    </Select>

                    <AlertDialogFooter>
                        <AlertDialogCancel>Cancel</AlertDialogCancel>
                        <AlertDialogAction onClick={() => { changeRoleMutation.mutate(selectedRole) }}>Continue</AlertDialogAction>
                    </AlertDialogFooter>
                </AlertDialogContent>
            </AlertDialog>
        </>
    )
}
