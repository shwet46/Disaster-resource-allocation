// src/pages/Dashboard.jsx (with Plotly)
import React, { useEffect, useState } from 'react';
import Plot from 'react-plotly.js';
import { fetchResourceAllocation } from '../apis/resourceAllocation';

const Dashboard = () => {
  const [allocationData, setAllocationData] = useState([]);

  useEffect(() => {
    const getAllocationData = async () => {
      const data = await fetchResourceAllocation();
      setAllocationData(data.best_allocation);
    };
    getAllocationData();
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold mb-4">Resource Allocation</h2>
      <Plot
        data={[
          {
            x: ['Zone 1', 'Zone 2', 'Zone 3'],
            y: allocationData,
            type: 'bar',
            marker: { color: 'blue' },
          },
        ]}
        layout={{ title: 'Disaster Resource Allocation' }}
      />
    </div>
  );
};

export default Dashboard;
