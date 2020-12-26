import React from 'react';
import {Create,SimpleForm, TextInput,DateTimeInput,BooleanInput,AutocompleteInput} from 'react-admin';

const EntranceCreate= (props)=>{
    return(
        <Create title = 'Create New Event'{...props}>
            <SimpleForm>
                <TextInput source='name'/>
                <AutocompleteInput source='course' label='Name of the course' choices={[
                    {'id':'Btech','name':"Bachelors of Technology (B.Tech)"}
                ]}/>
                <TextInput source='url' label='URL of the circular'/>
                <DateTimeInput source='date'/>

            </SimpleForm>
        </Create>


    )
}

export default EntranceCreate



