import logo from './logo.svg';
import './App.css';
//import Greet from './Components/greet';
import Welcome from './Components/Welcome';
import { Greet } from './Components/greet';
import Hello from './Components/hello';
import Message from './Components/Message';
import county from './Components/county';
import functionclick from './Components/functionclick';
import classclick from './Components/classclick';
import eventbing from './eventbing';

function App() {
  return (
    <div className="App">
      <classclick></classclick>
      <functionclick> </functionclick>
      <Greet name = "Ojas" heroname = "Ironman" />
      <Greet name = "Harsh" heroname = "Spiderman" />
      <Greet name = "Ishan" heroname = "Superman" />
      <Welcome name = "Ojas" heroname = "Ironman" />
      <Welcome name = "Harsh" heroname = "Spiderman" />
      <Welcome name = "Ishan" heroname = "Superman" />
      <Hello />
      <Message />
      <county />
    </div>
  );
}

export default App;
