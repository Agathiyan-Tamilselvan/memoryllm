import { useState, useEffect } from 'react'
import axios from 'axios'

function MemoryList() {
  const [memories, setMemories] = useState([])
  const [query, setQuery] = useState('')

  useEffect(() => {
    fetchMemories()
  }, [])

  const fetchMemories = async () => {
    const res = await axios.get('/api/memories')
    setMemories(res.data)
  }

  const searchMemories = async () => {
    if (!query) return fetchMemories()
    const res = await axios.get(`/api/memories/search?query=${query}`)
    setMemories(res.data)
  }

  return (
    <div>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search memories..."
      />
      <button onClick={searchMemories}>Search</button>
      <ul>
        {memories.map((m) => (
          <li key={m.id}>
            <p>{m.conversation}</p>
            {m.summary && <p><em>Summary: {m.summary}</em></p>}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default MemoryList