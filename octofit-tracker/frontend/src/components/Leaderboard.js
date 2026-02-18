import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [data, setData] = useState([]);
  const endpoint = `${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
  const url = `https://${endpoint}`;

  useEffect(() => {
    console.log('Fetching Leaderboard from:', url);
    fetch(url)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Leaderboard data:', results);
      })
      .catch(err => console.error('Error fetching Leaderboard:', err));
  }, [url]);

  return (
    <div>
      <h2>Leaderboard</h2>
      <ul>
        {data.map((item, idx) => (
          <li key={item.id || idx}>{JSON.stringify(item)}</li>
        ))}
      </ul>
    </div>
  );
};

export default Leaderboard;
