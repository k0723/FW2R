import { useState,useEffect } from 'react'
import './App.css'

function App() {
  const [message, setMessage] = useState("로딩 중...");

  useEffect(() => {
    fetch("http://localhost:8000/")
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(() => setMessage("백엔드 연결 실패"));
  }, []);

  return <h1>{message}</h1>;
}

export default App
