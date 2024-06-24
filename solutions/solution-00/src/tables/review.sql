CREATE TABLE User (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(120) UNIQUE NOT NULL,
    comment VARCHAR(500),
    rating FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);