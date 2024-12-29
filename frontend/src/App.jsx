import { useState } from 'react'
import Header from './components/Header'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Header/>
      <div className='text-center text-2xl'>Hi, welcome to our portfolio</div>
    



    </>
  )
}

export default App
