import { useState } from "react"

import { useNavigate } from "react-router-dom"
import { useMutation } from "@tanstack/react-query"

import { type SignUpType } from "@/types/authTypes"
import { type ErrorType } from "@/types/errorTypes"

import { authAPI } from "@/apis/authAPI"

import { Button } from "@/components/ui/button"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { toast } from "sonner"

import { Bars } from 'react-loader-spinner';

export default function Signup() {
    const navigate = useNavigate()

    const [userData, setUserData] = useState<SignUpType | undefined>(undefined)
    const [confirmPassword, setConfirmPassword] = useState<string>("")

    const handleSignUpData = (e: React.ChangeEvent<HTMLInputElement>): void => {
        setUserData(prev => ({
            ...prev!,
            [e.target.name]: e.target.value
        }))
    }

    const signUpMutation = useMutation({
        mutationFn: authAPI.signUp,
        onSuccess: () => {
            navigate('/')
        },
        onError: (error: ErrorType) => {
            toast.error(error.response.data.detail)
        }
    })

    const handleSignUp = (e: React.FormEvent): void => {
        e.preventDefault()

        if (!userData || !confirmPassword) {
            toast.error("Please fill in all fields")
            return
        }

        if (userData.password !== confirmPassword) {
            toast.error("Passwords do not match")
            return
        }

        signUpMutation.mutate(userData)
    }

    return (
        <>
            {
                signUpMutation.isPending ?
                    <div className="absolute top-0 left-0 right-0 bottom-0 z-30 bg-[#00000080] flex justify-center items-center">
                        <Bars
                            height="80"
                            width="80"
                            color="#fff"
                            ariaLabel="bars-loading"
                            wrapperStyle={{}}
                            wrapperClass=""
                            visible={true}
                        />
                    </div> : null
            }
            <div className="min-w-screen min-h-screen flex justify-center items-center bg-background">
                <div className="flex flex-col justify-center items-center gap-10 w-1/2">
                    <div className="flex flex-col justify-center items-center">
                        <h1 className="text-3xl">Welcome</h1>
                        <span className="flex justify-center items-center text-sm">
                            <p>Already have an account?</p>
                            <Button onClick={() => { navigate("/") }} variant="link" className="underline cursor-pointer">Login</Button>
                        </span>
                    </div>

                    <form onSubmit={handleSignUp} className="flex flex-col gap-5 w-1/2">
                        <div className="flex gap-5">
                            <div className="flex flex-col gap-2 w-full">
                                <Label htmlFor="fname">First Name</Label>
                                <Input onChange={handleSignUpData} className="w-full" id="fname" placeholder="First Name" name="first_name" />
                            </div>

                            <div className="flex flex-col gap-2 w-full">
                                <Label htmlFor="fname">Last Name</Label>
                                <Input onChange={handleSignUpData} className="w-full" id="lname" placeholder="Last Name" name="last_name" />
                            </div>
                        </div>

                        <div className="flex flex-col gap-2 w-full">
                            <Label htmlFor="username">Username</Label>
                            <Input onChange={handleSignUpData} className="w-full" id="username" placeholder="Username" name="username" />
                        </div>

                        <div className="flex flex-col gap-2 w-full">
                            <Label htmlFor="password">Password</Label>
                            <Input onChange={handleSignUpData} className="w-full" id="password" placeholder="Password" name="password" type="password" />
                        </div>

                        <div className="flex flex-col gap-2 w-full">
                            <Label htmlFor="confirm_password">Confirm Password</Label>
                            <Input onChange={(e) => { setConfirmPassword(e.target.value) }} className="w-full" id="confirm_password" placeholder="Confirm Password" name="confirm_password" type="password" />
                        </div>

                        <Button type="submit">Signup</Button>
                    </form>
                </div>
            </div>
        </>
    )
}
