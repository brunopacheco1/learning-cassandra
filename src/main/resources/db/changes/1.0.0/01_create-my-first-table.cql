CREATE TABLE linkedin.my_first_table (
    id uuid,
    name text,
    age int,
    email text,
    created_at timestamp,
    updated_at timestamp,
    PRIMARY KEY ((id), name, created_at)
);
