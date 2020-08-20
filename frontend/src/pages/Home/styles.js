import styled from 'styled-components';

export const Container = styled.div`
    display: flex;
    height: 100%;
    width: 100%;
    padding: 10px 14px;
    flex-direction: column;

    h1 {
        margin: 0 0 6px 10px;
    }

    hr {
        margin-bottom: 10px;
    }
`
export const MenuBlock = styled.div`
    display: flex;
    flex: 1;
    margin-top: 10px;
`

export const ComponentBlock = styled.div`
    display: flex;
    height: 220px;
    width: 200px;
    border: 2px solid #000;
    border-radius: 6px;
    margin-left: 30px;
    flex-direction: column;
    padding: 10px;

    &:hover {
        border-color: #0579FA;

        div {
            border-color: #0579FA;
            svg, span {
                color: #0579FA;
            }
        }

        span {
            color: #0579FA;
        }
    }

    div {
        display: flex;
        width: 100%;
        height: 70%;
        border-bottom: 2px solid #000;
        flex-direction: column;
        align-items: center;
        justify-content: center;

        span {
            margin-top: 12px;
            font-size: 24px;
        }
    }

    span {
        margin-top: 8px;
        font-size: 12px;
    }
`