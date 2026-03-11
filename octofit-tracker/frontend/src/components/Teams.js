import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Teams endpoint:', endpoint);
        console.log('Fetched teams:', data);
        setTeams(Array.isArray(data) ? data : data.results || []);
      })
      .catch(err => console.error('Error fetching teams:', err));
  }, [endpoint]);

  return (
    <div className="card">
      <div className="card-body">
        <h2 className="card-title display-6 mb-4">Teams</h2>
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead className="table-dark">
              <tr>
                <th>#</th>
                <th>Name</th>
                <th>Members</th>
                <th>Created At</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {teams.map((team, idx) => (
                <tr key={idx}>
                  <td>{idx + 1}</td>
                  <td>{team.name || '-'}</td>
                  <td>{Array.isArray(team.members) ? team.members.join(', ') : '-'}</td>
                  <td>{team.created_at ? new Date(team.created_at).toLocaleString() : '-'}</td>
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

export default Teams;
