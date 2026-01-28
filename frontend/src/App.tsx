import React, { useEffect, useState } from "react";
import UserTable, { User } from "./components/UserTable";
import LoadingError from "./components/LoadingError";

const API_URL = process.env.REACT_APP_API_URL!;

function App() {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`${API_URL}/users`, {
      credentials: "include",
    })
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP error: ${res.status}`);
        return res.json();
      })
      .then((data) => {
        setUsers(data);
        setError(null);
      })
      .catch((err) => {
        if (err.name === "TypeError" && err.message.includes("Failed to fetch")) {
          setError("Could not connect to backend API. Check your backend server and CORS settings.");
        } else {
          setError(err.message || "Failed to fetch users");
        }
        setUsers([]);
      })
      .finally(() => setLoading(false));
  }, []);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>User Directory</h1>
      <LoadingError loading={loading} error={error} />
      {!loading && !error && <UserTable users={users} />}
    </div>
  );
}

export default App;
