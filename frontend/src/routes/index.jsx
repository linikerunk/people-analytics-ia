import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

import Home from '../pages/Home';
import Employee from '../pages/Employee';
import Evaluation from '../pages/Evaluation';

export default function Routes(){
    return (
        <BrowserRouter>
        <Switch>
        <Route path="/" exact component={ Home }/> 
        <Route path="/funcionario" component={Employee} /> 
        <Route path="/desempenho" component={Evaluation} /> 
        </Switch>
        </BrowserRouter>   
    )
}