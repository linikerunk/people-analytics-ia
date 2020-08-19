import React from 'react'
import { FiLogIn } from 'react-icons/fi'

import { Container, Content, Background } from './styles'

export default function SignIn() {

    return (
        <Container>
            <Content>
                <h1>Faça seu login</h1>

                <form>
                <input placeholder="E-mail"/>
                <input placeholder="Senha"/>
                
                <button type="submit">Entrar</button>

                <a href="/">Esqueci minha senha</a>
                
                </form>

                <a href="/">
                    <FiLogIn />
                    Criar conta
                </a>
            </Content>

            <Background />
        </Container>
    )
}