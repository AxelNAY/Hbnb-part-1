CREATE TABLE Country (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(56) NOT NULL,
    code VARCHAR(36) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);