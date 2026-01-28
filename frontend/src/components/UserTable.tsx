import React from "react";

export interface User {
  id: number;
  name: string;
  username: string;
  email: string;
  phone: string;
  website: string;
  address: {
    street: string;
    suite: string;
    city: string;
    zipcode: string;
    geo: {
      lat: string;
      lng: string;
    };
  };
  company: {
    name: string;
    catchPhrase: string;
    bs: string;
  };
}

interface UserTableProps {
  users: User[];
}

const UserTable: React.FC<UserTableProps> = ({ users }) => (
  <div style={{ overflowX: "auto" }}>
    <table style={{ borderCollapse: "collapse", width: "100%" }}>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Username</th>
          <th>Email</th>
          <th>Phone</th>
          <th>Website</th>
          <th>Address</th>
          <th>Company</th>
        </tr>
      </thead>
      <tbody>
        {users.map((user) => (
          <tr key={user.id}>
            <td>{user.id}</td>
            <td>{user.name}</td>
            <td>{user.username}</td>
            <td>{user.email}</td>
            <td>{user.phone}</td>
            <td>
              <a href={`http://${user.website}`} target="_blank" rel="noopener noreferrer">
                {user.website}
              </a>
            </td>
            <td>
              {user.address.street}, {user.address.suite}, {user.address.city}, {user.address.zipcode}
              <br />
              <small>
                (Geo: {user.address.geo.lat}, {user.address.geo.lng})
              </small>
            </td>
            <td>
              {user.company.name}
              <br />
              <small>
                {user.company.catchPhrase}
                <br />
                {user.company.bs}
              </small>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
);

export default UserTable;