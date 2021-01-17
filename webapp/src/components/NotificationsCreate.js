import React from 'react';
import {Create,SimpleForm, TextInput,DateTimeInput,BooleanInput,AutocompleteInput} from 'react-admin';

const NotificationsCreate= (props)=>{
    return(
        <Create title = 'Create New Event'{...props}>
            <SimpleForm>
                <TextInput source='name'/>
                <TextInput source='url'/>
                <DateTimeInput source='start_date'/>
                <DateTimeInput source='end_date'/>
            </SimpleForm>
        </Create>


    )
}

export default NotificationsCreate



