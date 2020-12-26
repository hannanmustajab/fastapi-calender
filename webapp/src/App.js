import React from 'react';
import {Admin, Resource} from 'react-admin'
import restProvider from 'ra-data-simple-rest'
import EventList from './components/EventList'
import EventCreate from './components/EventCreate'
import EventEdit from './components/EventEdit'
import HolidayList from './components/HolidayList'
import HolidayCreate from './components/HolidayCreate'
import HolidayEdit from './components/HolidayEdit'
import EntranceList from './components/EntranceList'
import EntranceCreate from "./components/EntranceCreate";
import EntranceEdit from "./components/EntranceEdit";
import NotificationsList from "./components/NotificationsList";
import NotificationsCreate from "./components/NotificationsCreate";
import NotificationsEdit from "./components/NotificationsEdit";
import ExamsList from "./components/ExamsList";

const dataProvider = simpleRestProvider('http://controllerexams.herokuapp.com/api/v1/calender');


function App() {
    return (
      <Admin dataProvider={dataProvider}>
           <Resource name='events' list={EventList} create = {EventCreate} edit={EventEdit}/>
           <Resource name='holidays' list={HolidayList} create = {HolidayCreate} edit={HolidayEdit} />
           <Resource name='entrances' list={EntranceList}  create={EntranceCreate} edit={EntranceEdit}/>
           <Resource name='notifications' list={NotificationsList} create={NotificationsCreate} edit={NotificationsEdit}/>
           <Resource name='exams' list={ExamsList}/>
           <Resource name='results/entrance'/>
           <Resource name='results/general'/>
      </Admin>

  );
}

export default App;
