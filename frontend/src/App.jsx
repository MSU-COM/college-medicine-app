import React from 'react'
import {Route, createBrowserRouter, createRoutesFromElements, RouterProvider} from 'react-router-dom'

// Styles
import './styles/App.sass'

// Layouts
import MainLayout from './layouts/MainLayout'
import DetailLayout from './layouts/DetailLayout'

// Pages
import Home from './pages/Home'
import Admission from './pages/Admission'
import Simulation from './pages/Simulation'
import Faculty from './pages/Faculty'
import Alumni from './pages/Alumni'
import About from './pages/About'

// Detail Pages
import EventDetail from './components/EventDetail'
import AnnouncementDetail from './components/AnnouncementDetail'
import PublicationDetail from './components/PublicationDetail'

const router = createBrowserRouter(
  createRoutesFromElements(
    <>
      <Route path='/' element={<MainLayout />}>
        <Route index element={<Home />} />
        <Route path='/Admission' element={<Admission />} />
        <Route path='/Simulation' element={<Simulation />} />
        <Route path='/Faculty' element={<Faculty />} />
        <Route path='/Alumni' element={<Alumni />} />
        <Route path='/About' element={<About />} />
      </Route>
      <Route path='/' element={<DetailLayout />}>
        <Route path="/Events/:id" element={<EventDetail />} />
        <Route path="/Announcements/:id" element={<AnnouncementDetail />} />
        <Route path="/Publications/:id" element={<PublicationDetail />} />
      </Route>    
    </>
  )
);
const App = () => {
  return <RouterProvider router={router} />
}

export default App
