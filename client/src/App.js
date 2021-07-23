import ConfigureWeight from "./components/ConfigureWeight";
import Result from "./components/Result";
import UploadFile from "./components/UploadFile";

function App() {
  return (
    <div className="App">
      <UploadFile/>
      <ConfigureWeight/>
      <Result/>
    </div>
  );
}

export default App;
