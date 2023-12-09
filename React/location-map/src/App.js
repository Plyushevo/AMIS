import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import { Icon } from 'leaflet'
import 'leaflet/dist/leaflet.css'


function App() {
  const markers = [
    {
      geocode: [60.266948016513695, 24.8596057444373],
      popUp: 'Varia Myyrmäki'
    },
    {
      geocode: [60.30148855410818, 24.969056748527468],
      popUp: 'Varia Rälssitie 13, 01530 Vantaa'
    },
    {
      geocode: [60.31875866640034, 25.04607447390271],
      popUp: 'Varia Talvikkitie 119, 01360 Vantaa'
    },
    {
      geocode: [60.30037587630058, 25.051401488309242],
      popUp: 'Varia Tennistie 1, 01370 Vantaa'
    }
  ]

  const positionIcon = new Icon({
    iconUrl: require('./img/position_icon.png'),
    iconSize: [40,40]
  })

  return (
    <MapContainer center={[60.266948016513695, 24.8596057444373]} zoom={12} scrollWheelZoom={true}>
    <TileLayer
      attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
    />

    {markers.map(marker => (
      <Marker position={marker.geocode} icon={positionIcon}>
        <Popup>
        <div className='popup'>
          <h2 className='name'>{marker.popUp}</h2>
          <h2 className='position'>Latitude and longitude [{marker.geocode[0].toFixed(6)}, {marker.geocode[1].toFixed(6)}]</h2>
        </div>
        </Popup>
      </Marker>
    ))}
     </MapContainer>
  );
}

export default App;
