CREATE TABLE IF NOT EXISTS metric (
    dev_id TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    cpu_temp NUMBER NOT NULL,
    gps_location TEXT,
    FOREIGN KEY (dev_id) REFERENCES device(mac)
);