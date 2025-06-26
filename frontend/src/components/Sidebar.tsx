import { useEffect } from "react"
import { useNavigate } from "react-router-dom"
import { useQuery } from "@tanstack/react-query"

import { userAPI } from "@/apis/userAPI"

import NavUser from "./NavUser"

import { ChartBar, Users, Bot } from "lucide-react"
import { Skeleton } from "./ui/skeleton"

import {
    Sidebar,
    SidebarContent,
    SidebarFooter,
    SidebarGroup,
    SidebarGroupContent,
    SidebarGroupLabel,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
} from "@/components/ui/sidebar"

export default function AppSidebar() {
    const navigate = useNavigate();

    const data = [
        {
            title: "Application",
            items: [
                {
                    title: "Prediction",
                    url: '/predictions',
                    icon: ChartBar,
                },
                {
                    title: "Users",
                    url: '/users',
                    icon: Users,
                },
                {
                    title: "About The Model",
                    url: '/model',
                    icon: Bot,
                }
            ],
        }
    ]

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

    return (
        <Sidebar>
            <SidebarContent>
                {
                    data.map((group) => {
                        return (
                            <SidebarGroup key={group.title}>
                                <SidebarGroupLabel>{group.title}</SidebarGroupLabel>
                                <SidebarGroupContent>
                                    <SidebarMenu>
                                        {
                                            group.items.map((item) => {
                                                return (
                                                    <SidebarMenuItem onClick={() => navigate(item.url)} className="cursor-pointer" key={item.title}>
                                                        <SidebarMenuButton asChild>
                                                            <div>
                                                                <item.icon />
                                                                <p>{item.title}</p>
                                                            </div>
                                                        </SidebarMenuButton>
                                                    </SidebarMenuItem>
                                                )
                                            })
                                        }
                                    </SidebarMenu>
                                </SidebarGroupContent>
                            </SidebarGroup>
                        )
                    })
                }
            </SidebarContent >
            <SidebarFooter>
                {

                    isLoadingUser ? <Skeleton className="w-24 h-4" /> :
                        <NavUser user={user!} />
                }
            </SidebarFooter>
        </Sidebar>
    )
}
