import React from 'react';
import { IconBox,
Container,
UserBox,
Avatar
} from './styles';

import { FiUser,
FiMessageSquare,
FiMail,
FiClipboard,
FiSearch,
FiBell
} from 'react-icons/fi';

import Image from '../../assets/img/pupununu.jpg'

export default function Header() {
    return (
        <Container>
        <IconBox> 
            <ul>
                <li><FiMail size={20}/> &nbsp;Email</li>
                <li><FiUser size={20}/> &nbsp;Profile</li>
                <li><FiMessageSquare size={20}/> &nbsp;ChatBot</li>
            </ul>
        </IconBox>
        <UserBox>
                <ul>
                    <li><FiSearch size={20} /></li>
                    <li><FiBell size={20} /></li>
                    <li><FiClipboard size={20} /></li>
                    <li><Avatar src={Image} /></li>
                </ul>
        </UserBox>
        
        </Container>        
    )
}

