import React from 'react';
import {Edit,SimpleForm, TextInput,DateInput,BooleanInput} from 'react-admin';

const EventEdit= (props)=>{
    return(
        <Edit title = 'Edit Event'{...props}>
            <SimpleForm>
                <TextInput source='id' disabled/>
                <TextInput source='name'/>
                <TextInput source='department'/>
                <TextInput source='faculty'/>
                <TextInput source='description'/>
                <DateInput label = 'Starting date' source='start_date'/>
                <DateInput source='end_date'/>
                <BooleanInput source='online' />
            </SimpleForm>
        </Edit>


    )
}

export default EventEdit
