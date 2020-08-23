import React, { useCallBack } from 'react'
import { Link, useHistory } from 'react-router-dom'
import { FiArrowLeft, FiMail, FiLock, FiUser } from 'react-icons/fi'
import { BsType } from 'react-icons/bs'

import Input from '../../components/Input'
import Button from '../../components/Button'

import { Container, Content, Background } from './styles'

import Logo from '../../assets/img/logo2.png'

export default function SignUp() {
    const history = useHistory()

    function navigateToHome() {
        history.push('/')
    }

    return (
        <Container>
            <Background />
            <Content>
                <img src={Logo} />

                <form>
                    <Input message="Nome Completo" type="text" icon={BsType}/>

                    <Input message="Login" type="text" icon={FiUser}/>

                    <Input message="E-mail" type="text" icon={FiMail} />

                    <Input message="Senha" type="password" icon={FiLock}/>

                    <Input message="Senha novamente" type="password" icon={FiLock}/>

                    <Button type="submit" onClick={navigateToHome}>Cadastrar</Button>
                </form>

                <Link to="/">
                    <FiArrowLeft />
                    Voltar
                </Link>
            </Content>
        </Container>
    )
}