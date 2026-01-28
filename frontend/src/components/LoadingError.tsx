import React from "react";

interface LoadingErrorProps {
  loading: boolean;
  error: string | null;
}

const LoadingError: React.FC<LoadingErrorProps> = ({ loading, error }) => {
  if (loading) return <p>Loading users...</p>;
  if (error) return <p style={{ color: "red" }}>Error: {error}</p>;
  return null;
};

export default LoadingError;