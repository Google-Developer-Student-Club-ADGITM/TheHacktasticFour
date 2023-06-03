import { useState } from 'react'
import MainChat from './components/MainChat'
import { BrowserRouter, Route, Routes } from 'react-router-dom'

function App() {

	return (
			<BrowserRouter>
                <Routes>
                    <Route index element={<MainChat />} />
                    {/* <Route path="register" element={<Register />} />
                    <Route path="app" element={<MainApp />} /> */}
                </Routes>
            </BrowserRouter>
	)
}

export default App
