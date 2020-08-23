import styled, { css } from 'styled-components'

export const Container = styled.div`
    margin: 26px 0 20px 0;
    width: 100%;
    border: 2px solid #bdbdbd;
    border-radius: 10px;
    height: 60px;
    border-color: #BDBDBD;
    color: #BDBDBD;
    
    display: flex;
    align-items: center;
    padding: 0 10px;

    ${props => props.isFocused && css`
        border-color: #192D3E;
        color: #192D3E;
    `}

    ${props => props.isFilled && css`
        color: #192D3E;
    `}
`

export const Input = styled.input`
    margin-left: 10px;
    font-size: 14px;
    box-sizing: border-box;
    border: 0;
    height: 56px;
`