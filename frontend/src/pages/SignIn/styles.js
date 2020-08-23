import styled from 'styled-components'

import SignInBackground from '../../assets/img/sign-in-background.png'

export const Container = styled.div`
    height: 100%;
    width: 100%;
    display: flex;

    background-color: #fff;
    align-items: stretch;
`

export const Content = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    width: 100%;
    max-width: 700px;


    form {
        margin: 80px 0;
        width: 340px;
        text-align: center;

        button + button {
            margin: 0 0 16px 0;
        }
    }

    a {
            color: #0579FA;
            text-decoration: none;
            font-size: 16px;

            svg {
                margin-right: 10px;
            }
        }
`

export const Background = styled.div`
    display: flex;
    flex: 1;
    background: url(${SignInBackground}) no-repeat center;
    background-size: cover;
`
