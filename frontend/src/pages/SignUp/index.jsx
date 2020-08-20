import React from 'react'
import { Link } from 'react-router-dom'
import { FiArrowLeft } from 'react-icons/fi'

import { Container, Content, Background } from './styles'

export default function SignUp() {

    return (
        <Container>
            <Background />
            <Content>
                <h1>Faça seu cadastro</h1>

                <form>
                <input placeholder="Nome"/>
                <input placeholder="E-mail"/>
                <input placeholder="Senha"/>
                
                <button type="submit">Cadastrar</button>
                
                </form>

                <Link to="/">
                    <FiArrowLeft />
                    Voltar ao Login
                </Link>
            </Content>
        </Container>
    )
}