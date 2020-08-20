import React from 'react'
import { Route as ReactDOMRoute } from 'react-router-dom'

import Aside from '../components/Aside'
import Header from '../components/Header'

import { Container, AsideSpace, ContentSpace, HeaderSpace, Content } from './styles'

export default function Route( { isSign = false, component: Component,...rest } ) {

  return (
    <ReactDOMRoute
      {...rest}
      render={() => {
        return isSign ? (
          <Component />
        )
        :
        (
            <Container>
                <AsideSpace>
                    <Aside />
                </AsideSpace>
                <ContentSpace>
                    <HeaderSpace>
                        <Header />
                    </HeaderSpace>
                    <Content>
                        <Component />
                    </Content>
                </ContentSpace>
            </Container>
        )
      }}
    />
  )
}