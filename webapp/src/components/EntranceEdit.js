import React from 'react';
import {Edit,SimpleForm, TextInput,DateInput,BooleanInput} from 'react-admin';

const EntranceEdit= (props)=>{
    return(
        <Edit title = 'Edit Event'{...props}>
            <SimpleForm>
                <TextInput source='id' disabled/>
                <TextInput source='name'/>
                <TextInput source='course'/>
                <TextInput source='url'/>
                <DateInput label = 'Date and Time' source='date'/>
            </SimpleForm>
        </Edit>


    )
}

export default EntranceEdit
