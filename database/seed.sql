CREATE TABLE IF NOT EXISTS resource_allocation (
  id SERIAL PRIMARY KEY,
  zone TEXT NOT NULL,
  resources JSONB NOT NULL,
  response_time NUMERIC,
  remaining_resources JSONB  -- Added to store remaining resources
);
