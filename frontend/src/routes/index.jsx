import React from 'react';
import { BrowserRouter, Switch } from 'react-router-dom';

import Route from './Route'

import Home from '../pages/Home';
import Employee from '../pages/Employee';
import Evaluation from '../pages/Evaluation';
import SignIn from '../pages/SignIn'
import SignUp from '../pages/SignUp'

export default function Routes(){
    return (
        <BrowserRouter>
        <Switch>
        <Route path="/" exact component={ SignIn } isSign /> 
        <Route path="/signup" component={ SignUp } isSign /> 
        <Route path="/home" component={ Home }/> 
        <Route path="/funcionario" component={ Employee } /> 
        <Route path="/desempenho" component={ Evaluation } /> 
        </Switch>
        </BrowserRouter>   
    )
}