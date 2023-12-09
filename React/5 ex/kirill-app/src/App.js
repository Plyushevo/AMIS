import { BrowserRouter, Routes, Route, Link } from "react-router-dom"
import Home from './pages/Home'
import School from './pages/School'
import About from './pages/About'
import Header from './pages/Header'
import './App.css';

function App() {
  return (
  <BrowserRouter>
    <div>
      <Header />
      <Routes>
        <Route path="/" element={< Home />} />
        <Route path="/school" element={<School />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </div>
  </BrowserRouter>
  );
}

export default App;
