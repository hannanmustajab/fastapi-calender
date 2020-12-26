import React from 'react';
import {List,Datagrid, TextField,DateField, EditButton, DeleteButton,UrlField} from 'react-admin';

const NotificationsList= (props)=>{
    return(
        <List {...props}>
            <Datagrid>

                <TextField source='name'/>
                <DateField source='start_date'/>
                <DateField source='end_date'/>
                <UrlField source='url'/>
                <EditButton basePath='/notifications'/>
                <DeleteButton basePath='/notifications'/>
            </Datagrid>
        </List>

    )
}

export default NotificationsList