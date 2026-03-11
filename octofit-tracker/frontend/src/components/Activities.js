import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Activities endpoint:', endpoint);
        console.log('Fetched activities:', data);
        setActivities(Array.isArray(data) ? data : data.results || []);
      })
      .catch(err => console.error('Error fetching activities:', err));
  }, [endpoint]);

  return (
    <div className="card">
      <div className="card-body">
        <h2 className="card-title display-6 mb-4">Activities</h2>
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead className="table-dark">
              <tr>
                <th>#</th>
                <th>User</th>
                <th>Type</th>
                <th>Duration (min)</th>
                <th>Calories</th>
                <th>Date</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {activities.map((activity, idx) => (
                <tr key={idx}>
                  <td>{idx + 1}</td>
                  <td>{activity.user || '-'}</td>
                  <td>{activity.type || '-'}</td>
                  <td>{activity.duration || '-'}</td>
                  <td>{activity.calories || '-'}</td>
                  <td>{activity.date ? new Date(activity.date).toLocaleString() : '-'}</td>
                  <td>
                    <button className="btn btn-sm btn-primary me-2">View</button>
                    <button className="btn btn-sm btn-secondary">Edit</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Activities;
