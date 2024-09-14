import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';

const DisasterMap = () => {
  return (
    <MapContainer center={[51.505, -0.09]} zoom={13} className="h-96 w-full">
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <Marker position={[51.505, -0.09]}>
        <Popup>Disaster Zone 1</Popup>
      </Marker>
    </MapContainer>
  );
}

export default DisasterMap;
