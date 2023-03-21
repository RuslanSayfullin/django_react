import React from "react";
import { Link } from "react-router-dom";
import RegistrationForm from "../components/authentication/RegistrationForm";

function Registration() {
    return (
        <div className="container">
            <div className="row">
                <div className="col-md-6 d-flex align-items-center">
                <div className="content text-center px-4">
                    <h1 className="text-primary">Welcome to the Postagram!</h1>
                    <p className="content">
                    Это новая социальная сеть, которая позволит вам делиться своими
                    мысли и опыт с друзьями. Зарегистрируйтесь сейчас и начните наслаждаюсь! <br />
                    Или, если у вас уже есть аккаунт, пожалуйста{" "}
                    <Link to="/login/">авторизуйтесь</Link>.
                    </p>
                </div>
                </div>
                <div className="col-md-6 p-5">
                <RegistrationForm />
                </div>
            </div>
        </div>
    );
}

export default Registration;