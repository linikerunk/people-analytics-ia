import React, { useState } from 'react'
import { FaChartBar, FaUser, FaSearch, FaUniversity, FaClock, FaRegCheckSquare, FaUserAltSlash } from 'react-icons/fa'

import Image from '../../assets/img/pupununu.jpg'

import { Container, Logo, User, Menu, MenuButton, Avatar } from './styles'


export default function Aside() {
    const [checked, setChecked] = useState(0)

    
    return (
        <Container>
           <Logo>
               <h1>Logo</h1>
           </Logo>
           <User>
               <Avatar src={Image} />
               <span>Funcionário NASA</span>
           </User>
           <Menu>
                <MenuButton  onClick={() => setChecked(1)} isChecked={checked === 1 ? true : false}>
                    <FaChartBar size={18} color={checked === 1 ? '#000' : '#fff' } />
                    <span>Dashboard</span>
                </MenuButton>
                <MenuButton  onClick={() => setChecked(2)} isChecked={checked === 2 ? true : false}>
                    <FaUser size={18} color={checked === 2 ? '#000' : '#fff' } />
                    <span>Funcionários</span>
                </MenuButton>
                <MenuButton  onClick={() => setChecked(3)} isChecked={checked === 3 ? true : false}>
                    <FaSearch size={18} color={checked === 3 ? '#000' : '#fff' } />
                    <span>Recrutamento</span>
                </MenuButton>
                <MenuButton  onClick={() => setChecked(4)} isChecked={checked === 4 ? true : false}>
                    <FaUniversity size={18} color={checked === 4 ? '#000' : '#fff' } />
                    <span>Treinamento</span>
                </MenuButton>
                <MenuButton  onClick={() => setChecked(5)} isChecked={checked === 5 ? true : false}>
                    <FaClock size={18} color={checked === 5 ? '#000' : '#fff' } />
                    <span>Gestão de horas</span>
                </MenuButton>
                <MenuButton  onClick={() => setChecked(6)} isChecked={checked === 6 ? true : false}>
                    <FaRegCheckSquare size={18} color={checked === 6 ? '#000' : '#fff' } />
                    <span>Performance</span>
                </MenuButton>
                <MenuButton  onClick={() => setChecked(7)} isChecked={checked === 7 ? true : false}>
                    <FaUserAltSlash size={18} color={checked === 7 ? '#000' : '#fff'} />
                    <span>Desligamento</span>
                </MenuButton>
           </Menu>
        </Container>
    )
}