CREATE TABLE Place (
    id VARCHAR(36) PRIMARY KEY,
    description VARCHAR(500),
    address VARCHAR(128) UNIQUE NOT NULL,
    latitude FLOAT,
    longitude FLOAT,
    host_id VARCHAR(128) NOT NULL,
    city_id VARCHAR(128) NOT NULL,
    price_per_night INT,
    number_of_rooms INT,
    number_of_bathrooms INT,
    max_guests INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);