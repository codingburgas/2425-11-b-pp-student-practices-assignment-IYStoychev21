import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from "@tanstack/react-query"

import Protected from './components/Protected'

import Login from './routes/Login'
import Signup from './routes/Signup'
import Predictions from './routes/Predictions'
import Account from './routes/Account'
import UserManagment from './routes/UserManagment'
import UserView from './routes/UserView'
import PredictionView from './routes/PredictionView'
import NewPrediction from './routes/NewPrediction'
import AboutTheModel from './routes/AboutTheModel'

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
        { path: '/users/:id', element: <Protected><UserView /></Protected> },
        { path: '/predictions/:id', element: <Protected><PredictionView /></Protected> },
        { path: '/predictions/new', element: <Protected><NewPrediction /></Protected> },
        { path: '/model', element: <Protected><AboutTheModel /></Protected> },
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
