import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [data, setData] = useState([]);
  const endpoint = `${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
  const url = `https://${endpoint}`;

  useEffect(() => {
    console.log('Fetching Workouts from:', url);
    fetch(url)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Workouts data:', results);
      })
      .catch(err => console.error('Error fetching Workouts:', err));
  }, [url]);

  return (
    <div>
      <h2>Workouts</h2>
      <ul>
        {data.map((item, idx) => (
          <li key={item.id || idx}>{JSON.stringify(item)}</li>
        ))}
      </ul>
    </div>
  );
};

export default Workouts;
