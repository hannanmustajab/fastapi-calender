import React from 'react';
import {Edit,SimpleForm, TextInput,DateInput,BooleanInput} from 'react-admin';

const HolidayEdit= (props)=>{
    return(
        <Edit title = 'Edit Holiday'{...props}>
            <SimpleForm>
                <TextInput source='id' disabled/>
                <TextInput source='name'/>
                <TextInput source='url'/>
                <DateInput label = 'Starting date' source='start_date'/>
                <DateInput label = 'Starting date' source='end_date'/>
            </SimpleForm>
        </Edit>


    )
}

export default HolidayEdit
