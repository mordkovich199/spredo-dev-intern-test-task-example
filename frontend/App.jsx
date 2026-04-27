import { useEffect, useState } from "react";

export default function App() {
  const [projects, setProjects] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetch("http://localhost:5000/projects")
      .then(res => res.json())
      .then(data => setProjects(data));
  }, []);

  const filtered = projects.filter(p =>
    p.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div style={{ padding: "20px" }}>
      <h1>Crypto Projects</h1>

      <input
        placeholder="Search project"
        value={search}
        onChange={e => setSearch(e.target.value)}
      />

      <table border="1" cellPadding="8" style={{ marginTop: "20px" }}>
        <thead>
          <tr>
            <th>Name</th>
            <th>Market Cap</th>
            <th>FDV</th>
            <th>24h Volume</th>
          </tr>
        </thead>
        <tbody>
          {filtered.map((p, i) => (
            <tr key={i}>
              <td>{p.name}</td>
              <td>{p.mcap}</td>
              <td>{p.fdv}</td>
              <td>{p.volume_24h}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
