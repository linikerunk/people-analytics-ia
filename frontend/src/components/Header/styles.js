import styled from 'styled-components';

export const Container = styled.div`
    width: 1700px;
    height: 60px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    opacity: 0.9;
    background-color: #48D492;
    box-shadow: 5px 0px 5px 0px black;
`

export const IconBox = styled.div`
    ul{
        li{
            margin-left: 15px;
            text-decoration: none;
            list-style: none;
            display: flex;
            align-items: center;
            font-weight: 600;
            
        }

        display: flex;
        flex-direction: row;
        align-items: flex-start;
        justify-content: space-between;
    }    
` 

export const UserBox = styled.div`
    ul{
        li{
            margin-right: 35px;
            text-decoration: none;
            list-style: none;
            display: flex;
        }

        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
    } 
`

export const Avatar = styled.img`
    height: 2.5rem;
    width: 2.5rem;
    border-radius: 50%;
`
