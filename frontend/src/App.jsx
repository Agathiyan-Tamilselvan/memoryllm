import { useState } from 'react'
import Chat from './components/Chat.jsx'
import MemoryList from './components/MemoryList.jsx'
import './App.css'

function App() {
  const [activeTab, setActiveTab] = useState('chat')

  return (
    <div className="app">
      <h1>MemoryPal</h1>
      <div className="tabs">
        <button onClick={() => setActiveTab('chat')}>Chat</button>
        <button onClick={() => setActiveTab('memories')}>Memories</button>
      </div>
      {activeTab === 'chat' && <Chat />}
      {activeTab === 'memories' && <MemoryList />}
    </div>
  )
}

export default App