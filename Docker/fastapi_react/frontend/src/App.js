import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchEmployees = async () => {
      try {
        const response = await axios.get('http://localhost:8000/employee_sample/');
        setEmployees(response.data.employees);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching employees:', error);
        setError('Error fetching employees. Please try again later.');
        setLoading(false);
      }
    };

    fetchEmployees();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h1>Employee List</h1>
      <ul>
        {employees.map(employee => (
          <li key={employee.id}>
            {employee.first_name} {employee.last_name} - {employee.department} - ${employee.salary}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
