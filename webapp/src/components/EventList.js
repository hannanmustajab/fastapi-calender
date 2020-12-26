import React from 'react';
import {List,Datagrid,TextInput, TextField,DateField, EditButton, DeleteButton,Filter, ReferenceInput, SelectInput } from 'react-admin';



const EventFilter = (props) => (
    <Filter {...props}>
        <TextInput label="Search" source="q" alwaysOn />
        <ReferenceInput label="Department" source="/" reference="department" allowEmpty>
            <SelectInput optionText="department" />
        </ReferenceInput>
    </Filter>
);

const EventList= (props)=>{
    return(
        <List filters={<EventFilter />}{...props}>
            <Datagrid>

                <TextField source='name'/>
                <TextField source='faculty'/>
                <TextField source='department'/>
                <DateField source='start_date'/>
                <DateField source='end_date'/>
                <EditButton basePath='/events'/>
                <DeleteButton basePath='/events'/>
            </Datagrid>
        </List>

    )
}

export default EventList