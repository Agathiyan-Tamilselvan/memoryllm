import { useState } from 'react'
import axios from 'axios'

function Chat() {
  const [message, setMessage] = useState('')
  const [responses, setResponses] = useState([])

  const sendMessage = async () => {
    if (!message) return
    const res = await axios.post('/api/chat', { message })
    setResponses([...responses, { user: message, ai: res.data.response }])
    setMessage('')
  }

  return (
    <div>
      <div className="chat-history">
        {responses.map((r, i) => (
          <div key={i}>
            <p><strong>You:</strong> {r.user}</p>
            <p><strong>AI:</strong> {r.ai}</p>
          </div>
        ))}
      </div>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
        placeholder="Type your message..."
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  )
}

export default Chat