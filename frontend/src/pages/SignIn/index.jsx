import React, { useCallBack } from 'react'
import { Link, useHistory } from 'react-router-dom'
import { FiLogIn } from 'react-icons/fi'

import { Container, Content, Background } from './styles'

export default function SignIn() {
    const history = useHistory()

    function navigateToHome() {
        history.push('/home')
    }

    return (
        <Container>
            <Content>
                <h1>Faça seu login</h1>

                <form>
                <input placeholder="E-mail"/>
                <input placeholder="Senha"/>
                
                <button type="submit" onClick={navigateToHome}>Entrar</button>

                <a href="/">Esqueci minha senha</a>
                
                </form>

                <Link to="/signup">
                    <FiLogIn />
                    Criar conta
                </Link>
            </Content>

            <Background />
        </Container>
    )
}