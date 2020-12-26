import React from 'react';
import {Create,SimpleForm, TextInput,DateTimeInput,BooleanInput,UrlField} from 'react-admin';

const HolidayCreate= (props)=>{
    return(
        <Create title = 'Create New Holiday'{...props}>
            <SimpleForm>
                <TextInput source='name'/>
                <DateTimeInput source='start_date'/>
                <DateTimeInput source='end_date'/>

            </SimpleForm>
        </Create>


    )
}

export default HolidayCreate

