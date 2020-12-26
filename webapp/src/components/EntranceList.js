import React from 'react';
import {List,Datagrid, TextField,DateField, EditButton, DeleteButton } from 'react-admin';

const EntranceList= (props)=>{
    return(
        <List {...props}>
            <Datagrid>

                <TextField source='name'/>
                <TextField source='course'/>
                <TextField source='url'/>
                <DateField source='date'/>
                <EditButton basePath='entrances'/>
                <DeleteButton basePath='entrances'/>
            </Datagrid>
        </List>

    )
}

export default EntranceList