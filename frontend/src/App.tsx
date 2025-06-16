import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from "@tanstack/react-query"

const queryClient = new QueryClient()

import Login from './routes/Login'

import { SidebarProvider } from "@/components/ui/sidebar"

import { Toaster } from "@/components/ui/sonner"

function App() {
    const BrowserRouter = createBrowserRouter([
        { path: '/', element: <Login /> },
    ])

    return (
        <SidebarProvider>
            <QueryClientProvider client={queryClient}>
                <RouterProvider router={BrowserRouter} />
                <Toaster />
            </QueryClientProvider>
        </SidebarProvider>
    )
}

export default App
