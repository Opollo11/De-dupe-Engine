import React from 'react'
import Slider from "./Slider";

const INIT_SETTINGS = {
    "mrn":0,
    "phone_number":0,
    "first_name":0,
    "last_name":0,
    "specialization":0,
}
function ConfigureWeight() {
    const [settings, setSettings] = React.useState(INIT_SETTINGS);
    console.log(settings)
    return (
        <div>
            {
                Object.keys(settings).map(item=><Slider name={item} setSettings={setSettings} />)
            }
        </div>
    )
}

export default ConfigureWeight
