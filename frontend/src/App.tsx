import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from "@tanstack/react-query"

const queryClient = new QueryClient()

import Login from './routes/Login'
import Signup from './routes/Signup'

import { SidebarProvider } from "@/components/ui/sidebar"

import { Toaster } from "@/components/ui/sonner"

function App() {
    const BrowserRouter = createBrowserRouter([
        { path: '/', element: <Login /> },
        { path: '/signup', element: <Signup /> },
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
