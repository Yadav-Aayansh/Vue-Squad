import { defineStore } from "pinia";

export const signupStore = defineStore('signup',{
    state: () => ({
        role: 'Student',
        username: '',
        email: '',
        password: '',
        confirm_password: '',
        name: '',
    }),

    actions: {
        changeRole(role) {
            this.role = role
        },
        changeUsername(username) {
            this.username = username
        },
        changeEmail(email) {
            this.email = email
        },
        changePassword(password) {
            this.password = password
        },
        changeConfirmPassword(confirm_password) {
            this.confirm_password = confirm_password
        },
        changeName(name) {
            this.name = name
        },
    
    }
})