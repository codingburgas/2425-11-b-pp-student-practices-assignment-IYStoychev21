export type RoleType = {
    id: number;
    role_name: string;
};

export type UserType = {
    id: number;
    username: string
    first_name: string
    last_name: string
    role: RoleType;
};

export type UpdateUserType = {
    first_name: string
    last_name: string
}
