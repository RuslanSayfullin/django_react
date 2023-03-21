import React from "react";
import { Link } from "react-router-dom";
import LoginForm from "../components/authentication/LoginForm";

function Login() {
    return (
        <div className="container">
            <div className="row">
                <div className="col-md-6 d-flex align-items-center">
                    <div className="content text-center px-4">
                        <h1 className="text-primary">Welcome to Postagram!</h1>
                        <p className="content">
                            Войдите сейчас и начните наслаждаться!
                            Или, если у вас нет учетной записи, пожалуйста,{" "}
                            <Link to="/register/">регистрация</Link>.
                        </p>
                    </div>
                </div>
                <div className="col-md-6 p-5">
                    <LoginForm />
                </div>
            </div>
        </div>
    );    
}

export default Login;