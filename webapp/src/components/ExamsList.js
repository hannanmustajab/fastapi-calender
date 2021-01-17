import React from 'react';
import {List,Datagrid, TextField,DateField, EditButton, DeleteButton,UrlField} from 'react-admin';

const ExamsList= (props)=>{
    return(
        <List {...props}>
            <Datagrid>

                <TextField source='name'/>
                <TextField source='faculty'/>
                <TextField source='department'/>
                <TextField source='course_code'/>
                <TextField source='course'/>
                <DateField source='date'/>
                <EditButton basePath='/exams'/>
                <DeleteButton basePath='/exams'/>
            </Datagrid>
        </List>

    )
}

export default ExamsList