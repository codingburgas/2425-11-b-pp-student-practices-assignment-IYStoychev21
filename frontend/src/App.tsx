import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from "@tanstack/react-query"

import Protected from './components/Protected'

import Login from './routes/Login'
import Signup from './routes/Signup'
import Predictions from './routes/Predictions'
import Account from './routes/Account'
import UserManagment from './routes/UserManagment'

import { SidebarProvider } from "@/components/ui/sidebar"

import { Toaster } from "@/components/ui/sonner"

const queryClient = new QueryClient()

function App() {
    const BrowserRouter = createBrowserRouter([
        { path: '/', element: <Login /> },
        { path: '/signup', element: <Signup /> },
        { path: '/predictions', element: <Protected><Predictions /></Protected> },
        { path: '/account', element: <Protected><Account /></Protected> },
        { path: '/users', element: <Protected><UserManagment /></Protected> },
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
