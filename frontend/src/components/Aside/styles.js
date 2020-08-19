import styled, { css } from 'styled-components'

export const Container = styled.div`
    width: 20%;
    height: 100%;
    display: flex;

    background-color: #343A40;
    flex-direction: column;

    padding: 0 10px;
`

export const Logo = styled.div`
    display: flex;
    width: 100%;
    height: 60px;

    align-items: center;
    justify-content: center;

    margin-bottom: 10px;
    border-bottom: 1px solid #fff;
`

export const User = styled.div`
    display: flex;
    width: 100%;
    height: 80px;

    align-items: center;
    justify-content: center;

    margin-bottom: 20px;
    border-bottom: 1px solid #fff;

    span {
        color: #fff;
        margin-left: 10px;
        font-size: 18px;
        font-weight: 500;
    }
`

export const Menu = styled.div`
    display: flex;
    flex: 1;
    flex-direction: column;
    align-items: center;
`

export const MenuButton = styled.button`
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 45px;

    align-items: center;
    padding-left: 10px;

    border-radius: 8px;
    border: none;

    background-color: inherit;
    padding: 0 20px;

    transition: background-color 1s;

    span {
        color: #fff;
        font-size: 18px;
        font-weight: 500;
        margin-left: 10px;
    }

    ${props => props.isChecked ? css`
        background-color: #fff;

        span {
            color: #000;
        }
    ` :
    css `
        &:hover {
        background-color: #0579FA;
    }
    `
    }
`

export const Avatar = styled.img`
    height: 3.5rem;
    width: 3.5rem;
    border-radius: 50%;

    margin-bottom: 5px;
`