import React from 'react';
import { FaChartBar, FaUser, FaSearch, FaUniversity, FaClock, FaRegCheckSquare, FaUserAltSlash } from 'react-icons/fa'

import { Container, MenuBlock, ComponentBlock } from './styles'

export default function Home(){
    return (
        <Container >
            <h1>Home</h1>
            <hr />
            <MenuBlock>
                <ComponentBlock>
                    <div>
                        <FaChartBar size={48}/>
                        <span>Dashboard</span>
                    </div>
                    <span>
                        Gráficos detalhados referente aos funcionários e desempenho dos mesmos.
                    </span>
                </ComponentBlock>
                <ComponentBlock>
                    <div>
                        <FaUser size={48}/>
                        <span>Funcionários</span>
                    </div>
                    <span>
                        Adicione, altere ou remova dados de funcionários.
                    </span>
                </ComponentBlock>
                <ComponentBlock>
                    <div>
                        <FaSearch size={48}/>
                        <span>Recutamento</span>
                    </div>
                    <span>
                        Busque por candidatos.
                    </span>
                </ComponentBlock>
                <ComponentBlock>
                    <div>
                        <FaUniversity size={48}/>
                        <span>Treinamento</span>
                    </div>
                    <span>
                        Agende e organize treinamentos.
                    </span>
                </ComponentBlock>
            </MenuBlock>
            <MenuBlock>
            <ComponentBlock>
                    <div>
                        <FaClock size={48}/>
                        <span>Gestão de Horas</span>
                    </div>
                    <span>
                        Controle de horas.
                    </span>
                </ComponentBlock>
                <ComponentBlock>
                    <div>
                        <FaRegCheckSquare size={48}/>
                        <span>Performance</span>
                    </div>
                    <span>
                        Dados detalhados em relação a performance dos funcionários
                    </span>
                </ComponentBlock>
                <ComponentBlock>
                    <div>
                        <FaUserAltSlash size={48}/>
                        <span>Desligamento</span>
                    </div>
                    <span>
                        Histórico de desligamentos
                    </span>
                </ComponentBlock>
            </MenuBlock>
        </Container>
    )
}











































// import React, { Component } from 'react';
// import CustomersService from './CustomersService';

// const customersService = new CustomersService();

// class CustomerCreateUpdate extends Component {

//     constructor(props) {
//         super(props);
//         this.handleSubmit = this.handleSubmit.bind(this);
//     }

//     componentDidMount() {
//         const { match: { params } } = this.props;
//         if (params && params.pk) {
//             customersService.getCustomer(params.pk).then((c) => {
//                 this.refs.firstName.value = c.first_name;
//                 this.refs.lastName.value = c.last_name;
//                 this.refs.email.value = c.email;
//                 this.refs.phone.value = c.phone;
//                 this.refs.address.value = c.address;
//                 this.refs.description.value = c.description;
//             })
//         }
//     }

//     handleCreate() {
//         customersService.createCustomer(
//             {
//                 "first_name": this.refs.firstName.value,
//                 "last_name": this.refs.lastName.value,
//                 "email": this.refs.email.value,
//                 "phone": this.refs.phone.value,
//                 "address": this.refs.address.value,
//                 "description": this.refs.description.value
//             }).then((result) => {
//                 alert("Customer created!");
//             }).catch(() => {
//                 alert('There was an error! Please re-check your form.');
//             });
//     }

//     handleUpdate(pk) {
//         customersService.updateCustomer(
//             {
//                 "pk": pk,
//                 "first_name": this.refs.firstName.value,
//                 "last_name": this.refs.lastName.value,
//                 "email": this.refs.email.value,
//                 "phone": this.refs.phone.value,
//                 "address": this.refs.address.value,
//                 "description": this.refs.description.value
//             }
//         ).then((result) => {

//             alert("Customer updated!");
//         }).catch(() => {
//             alert('There was an error! Please re-check your form.');
//         });
//     }

//     handleSubmit(event) {
//         const { match: { params } } = this.props;
//         if (params && params.pk) {
//             this.handleUpdate(params.pk);
//         }
//         else {
//             this.handleCreate();
//         }
//         event.preventDefault();
//     }


//     render() {
//         return (
//             <form onSubmit={this.handleSubmit}>
//                 <div className="form-group">
//                     <label>
//                         First Name:</label>
//                     <input className="form-control" type="text" ref='firstName' />

//                     <label>
//                         Last Name:</label>
//                     <input className="form-control" type="text" ref='lastName' />

//                     <label>
//                         Phone:</label>
//                     <input className="form-control" type="text" ref='phone' />

//                     <label>
//                         Email:</label>
//                     <input className="form-control" type="text" ref='email' />

//                     <label>
//                         Address:</label>
//                     <input className="form-control" type="text" ref='address' />

//                     <label>
//                         Description:</label>
//                     <textarea className="form-control" ref='description' ></textarea>


//                     <input className="btn btn-primary" type="submit" value="Submit" />
//                 </div>
//             </form>
//         );
//     }

// }
// export default CustomerCreateUpdate;