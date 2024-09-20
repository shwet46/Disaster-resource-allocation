import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Plot from 'react-plotly.js';

const Dashboard = () => {
  const [allocationData, setAllocationData] = useState({});
  const [responseTime, setResponseTime] = useState(0);
  const [remainingResources, setRemainingResources] = useState({});

  useEffect(() => {
    axios.post(`${import.meta.env.VITE_API_URL}/allocate_resources`, {
      disaster_zone: 'Zone A',
      population: 1000,
      earthquake_magnitude: 7.5,  // New earthquake parameter
      resources: { water: 200, food: 500, medical_supplies: 100 }
    })
    .then((response) => {
      setAllocationData(response.data.allocation);
      setResponseTime(response.data.response_time);
      setRemainingResources(response.data.remaining_resources);
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
  }, []);

  return (
    <div>
      <h1>Earthquake Resource Allocation Dashboard</h1>
      <h2>Response Time: {responseTime} units</h2>
      
      <Plot
        data={[
          {
            type: 'bar',
            x: Object.keys(allocationData),
            y: Object.values(allocationData),
            name: 'Allocated Resources'
          },
          {
            type: 'bar',
            x: Object.keys(remainingResources),
            y: Object.values(remainingResources),
            name: 'Remaining Resources'
          }
        ]}
        layout={{ title: 'Resource Allocation and Remaining Resources' }}
      />
    </div>
  );
};

export default Dashboard;
