import axios from 'axios';

const API_URL = "http://localhost:8000";

export const fetchResourceAllocation = async () => {
  try {
    const response = await axios.get(`${API_URL}/allocate_resources/`);
    return response.data;
  } catch (error) {
    console.error("Error fetching resource allocation:", error);
    throw error;
  }
};