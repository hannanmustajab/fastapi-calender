import React from 'react';
import {Edit,SimpleForm, TextInput,DateTimeInput,BooleanInput} from 'react-admin';

const NotificationsEdit= (props)=>{
    return(
        <Edit title = 'Edit Notifications'{...props}>
            <SimpleForm>
                <TextInput source='id' disabled/>
                <TextInput source='name'/>
                <DateTimeInput source='start_date'/>
                <DateTimeInput source='end_date'/>
                <TextInput source='url'/>
            </SimpleForm>
        </Edit>


    )
}

export default NotificationsEdit
