import { useNavigate } from "react-router-dom";

import { type UserType } from "@/types/userTypes";

import {
    BadgeCheck,
    ChevronsUpDown,
    LogOut,
} from "lucide-react"

import {
    Avatar,
    AvatarImage,
} from "@/components/ui/avatar"
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuGroup,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import {
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
} from "@/components/ui/sidebar"
import { Button } from "@/components/ui/button"
import { Skeleton } from "./ui/skeleton";

export default function NavUser({ user, className }: { user: UserType, className?: string }) {
    const navigate = useNavigate();

    if (!user) {
        return (
            <div className="w-full flex gap-5 items-center">
                <Skeleton className="h-8 w-8 rounded-lg" />
                <div className="flex flex-col gap-3">
                    <Skeleton className="h-4 w-24" />
                    <Skeleton className="h-4 w-16" />
                </div>
            </div>
        )
    }

    return (
        <SidebarMenu className={className}>
            <SidebarMenuItem>
                <DropdownMenu>
                    <DropdownMenuTrigger asChild>
                        <SidebarMenuButton
                            size="lg"
                            className="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground"
                        >
                            <Avatar className="h-8 w-8 rounded-lg">
                                <AvatarImage src={`https://ui-avatars.com/api/?name=${user.first_name + ' ' + user.last_name}&size=128&background=60494d&color=fff&bold=true`} alt={user.username} />
                            </Avatar>
                            <div className="grid flex-1 text-left text-sm leading-tight">
                                <span className="truncate font-semibold">{user.first_name + ' ' + user.last_name}</span>
                                <span className="truncate text-xs">{user.username}</span>
                            </div>
                            <ChevronsUpDown className="ml-auto size-4" />
                        </SidebarMenuButton>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent
                        className="w-[--radix-dropdown-menu-trigger-width] min-w-56 rounded-lg"
                        side="right"
                        align="end"
                        sideOffset={4}
                    >
                        <DropdownMenuLabel className="p-0 font-normal">
                            <div className="flex items-center gap-2 px-1 py-1.5 text-left text-sm">
                                <Avatar className="h-8 w-8 rounded-lg">
                                    <AvatarImage src={`https://ui-avatars.com/api/?name=${user.first_name + ' ' + user.last_name}&size=128&background=60494d&color=fff&bold=true`} />
                                </Avatar>
                                <div className="grid flex-1 text-left text-sm leading-tight">
                                    <span className="truncate font-semibold">{user.first_name + ' ' + user.last_name}</span>
                                    <span className="truncate text-xs">{user.username}</span>
                                </div>
                            </div>
                        </DropdownMenuLabel>
                        <DropdownMenuSeparator />
                        <DropdownMenuGroup>
                            <DropdownMenuItem>
                                <BadgeCheck />
                                <Button onClick={() => { navigate("/account") }} variant="ghost" className="w-full justify-start cursor-pointer">
                                    Account
                                </Button>
                            </DropdownMenuItem>
                            <DropdownMenuItem>
                                <LogOut />

                                <Button onClick={() => { localStorage.removeItem("token"); navigate("/") }} variant="ghost" className="w-full justify-start cursor-pointer">
                                    Log Out
                                </Button>
                            </DropdownMenuItem>
                        </DropdownMenuGroup>
                    </DropdownMenuContent>
                </DropdownMenu>
            </SidebarMenuItem>
        </SidebarMenu>
    );
}
