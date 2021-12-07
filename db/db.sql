CREATE DATABASE IF NOT EXISTS figi;
USE figi;
CREATE TABLE IF NOT EXISTS rus_figis
(
    id INT NOT NULL AUTO_INCREMENT,
    ticker VARCHAR(20),
    long_or_short BOOL,
    PRIMARY KEY (id),
    UNIQUE(ticker)
);
CREATE TABLE IF NOT EXISTS usd_figis
(
    id INT NOT NULL AUTO_INCREMENT,
    ticker VARCHAR(20) UNIQUE,
    long_or_short BOOL,
    PRIMARY KEY (id),
    UNIQUE(ticker)
);
CREATE TABLE IF NOT EXISTS subscribed_users
(
    id INT NOT NULL AUTO_INCREMENT,
    user_id VARCHAR(20) UNIQUE,
    PRIMARY KEY (id),
    UNIQUE(user_id)
);