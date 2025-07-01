import { useState } from "react"

import { useNavigate } from "react-router-dom"
import { useMutation } from "@tanstack/react-query"

import { authAPI } from "@/apis/authAPI"
import { type SignInType } from "@/types/authTypes"
import { type ErrorType } from "@/types/errorTypes"

import { Button } from "@/components/ui/button"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { toast } from "sonner"

import { BarLoader } from 'react-spinners';

export default function Login() {
    const navigate = useNavigate()
    const [signInData, setSignInData] = useState<SignInType | undefined>(undefined)

    const handleSignInData = (e: React.ChangeEvent<HTMLInputElement>): void => {
        setSignInData(prev => ({
            ...prev!,
            [e.target.name]: e.target.value
        }))
    }

    const signInMutation = useMutation({
        mutationFn: authAPI.logIn,
        onSuccess: (data) => {
            localStorage.setItem("token", data.token)
            window.location.href = '/predictions'
        },
        onError: (error: ErrorType) => {
            toast.error(error.response.data.detail)
        }
    })

    const handleSignIn = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault()

        if (!signInData) {
            toast.error("Please fill in all fields")
            return
        }

        signInMutation.mutate(signInData)
    }

    return (
        <>
            {
                signInMutation.isPending ?
                    <div className="absolute top-0 left-0 right-0 bottom-0 z-30 bg-[#00000080] flex justify-center items-center">
                        <BarLoader
                            height="80"
                            width="80"
                            color="#fff"
                        />
                    </div> : null
            }
            <div className="min-w-screen min-h-screen flex justify-center items-center bg-background">
                <div className="flex flex-col justify-center items-center gap-10 w-1/2">
                    <div className="flex flex-col justify-center items-center">
                        <h1 className="text-3xl">Welcome</h1>
                        <span className="flex justify-center items-center text-sm">
                            <p>Don't have an account?</p>
                            <Button onClick={() => { navigate("/signup") }} variant="link" className="underline cursor-pointer">Sign up</Button>
                        </span>
                    </div>

                    <form onSubmit={handleSignIn} className="flex flex-col gap-5 w-1/2">
                        <div className="flex flex-col gap-2 w-full">
                            <Label htmlFor="username">Username</Label>
                            <Input onChange={handleSignInData} className="w-full" id="username" placeholder="Username" name="username" />
                        </div>

                        <div className="flex flex-col gap-2 w-full">
                            <Label htmlFor="password">Password</Label>
                            <Input onChange={handleSignInData} className="w-full" id="password" placeholder="Password" name="password" type="password" />
                        </div>

                        <Button type="submit">Login</Button>
                    </form>
                </div>
            </div>
        </>
    )
}
