import React from 'react';
import {List,Datagrid, TextField,DateField, EditButton, DeleteButton,UrlField} from 'react-admin';

const HolidayList= (props)=>{
    return(
        <List {...props}>
            <Datagrid>

                <TextField source='name'/>
                <DateField source='start_date'/>
                <DateField source='end_date'/>
                <UrlField source='url'/>
                <EditButton basePath='/holidays'/>
                <DeleteButton basePath='/holidays'/>
            </Datagrid>
        </List>

    )
}

export default HolidayList