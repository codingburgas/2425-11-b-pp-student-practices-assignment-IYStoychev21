import { useEffect, useState } from 'react';
import { Navigate } from 'react-router-dom';

export default function Protected({ children }: { children: React.ReactNode }) {
    const [isLoggedIn, setIsLoggedIn] = useState(true);

    useEffect(() => {
        if (!localStorage.getItem('token')) {
            setIsLoggedIn(false)
        }
    }, [])

    if (!isLoggedIn)
        return <Navigate to="/" />


    return children
}
