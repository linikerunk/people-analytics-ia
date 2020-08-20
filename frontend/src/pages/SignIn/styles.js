import styled from 'styled-components'

import SignInBackground from '../../assets/img/SignInPhoto.png'

export const Container = styled.div`
    height: 100%;
    width: 100%;
    display: flex;

    background-color: #343A40;
    align-items: stretch;
`

export const Content = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    width: 100%;
    max-width: 700px;

    h1 {
        font-weight: bold;
        color: #fff;
    }

    form {
        margin: 80px 0;
        width: 340px;
        text-align: center;

        input {
            color: #fff;
            background: #242A30;
            border-radius: 10px;
            border: 2px solid #0579FA;
            padding: 16px;
            width: 100%;

            & + input {
                margin-top: 8px;
            }
        }

        button {
            background: #0579FA;
            border-radius: 10px;
            height: 56px;
            border: 0;
            padding: 0 16px;
            width: 100%;
            color: #fff;
            font-weight: bold;
            margin: 16px 0;
        }

        a {
            color: #fff;
            text-decoration: none;
            font-size: 15px;
            margin-top: 30px;
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
