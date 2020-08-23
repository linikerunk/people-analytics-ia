import React, { useCallback, useRef } from 'react'
import { Link, useHistory } from 'react-router-dom'
import { FiLogIn, FiUser, FiLock } from 'react-icons/fi'
import { Form } from '@unform/web';
import * as Yup from 'yup';

import Input from '../../components/Input'
import Button from '../../components/Button'
import getValidationErrors from '../../utils/getValidationErrors'

import { Container, Content, Background } from './styles'

import Logo from '../../assets/img/logo2.png'

export default function SignIn() {
    const formRef = useRef(null)
    const history = useHistory()

    function navigateToHome() {
        history.push('/home')
    }

    function navigateToSignUp() {
        history.push('/signup')
    }

    const handleSubmit = useCallback(async (data) => {
        try {
            formRef.current.setErrors({})
            const schema = Yup.object().shape({
                email: Yup.string().required('E-mail obrigatório.').email('Digite um e-mail válido.'),
                password: Yup.string().required('Senha obrigatória.')
            })

            await schema.validate(data, {
                abortEarly: false
            })

            history.push('/home')
        } catch(err) {
            if (err instanceof Yup.ValidationError) {
                const errors = getValidationErrors(err)

                formRef.current.setErrors(errors);

                console.log(data)

                return;
            }

            console.log('teste')
        }
    }, [history])

    return (
        <Container>
            <Content>
                <img src={Logo} />

                <Form ref={formRef} onSubmit={handleSubmit}>
                    <Input name="email" message="Login / E-mail" type="text" icon={FiUser}/>

                    <Input name="password" message="Senha" type="password" icon={FiLock} />

                    <Button type="submit">Entrar</Button>

                    <Button onClick={navigateToSignUp}>Registrar</Button>
                </Form>

                <Link to="/">
                    <FiLogIn />
                    Esqueci minha senha
                </Link>
            </Content>

            <Background />
        </Container>
    )
}