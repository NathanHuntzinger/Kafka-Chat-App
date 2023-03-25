import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// const firebaseConfig = {
//   apiKey: process.env.FIREBASE_API_KEY,
//   authDomain: process.env.FIREBASE_AUTHDOMAIN,
//   projectId: process.env.FIREBASE_PROJECTID,
//   storageBucket: process.env.FIREBASE_STORAGEBUCKET, 
//   messagingSenderId: process.env.FIREBASE_MESSAGINGSENDERID, 
//   appId: process.env.FIREBASE_APPID
// };

const firebaseConfig = {
  apiKey: "AIzaSyAX2O6l9LDVpBsRm6Cm9SR2ZM2cSTZFVFE",
  authDomain: "chat-app-3cbfa.firebaseapp.com",
  projectId: "chat-app-3cbfa",
  storageBucket: "chat-app-3cbfa.appspot.com",
  messagingSenderId: "918539763166",
  appId: "1:918539763166:web:60ea0bb7eea46f43e8714f"
};


// Initialize Firebase
const app = initializeApp(firebaseConfig);


function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://reactjs.org" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {app.name}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </div>
  )
}

export default App
