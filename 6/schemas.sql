CREATE TABLE IF NOT EXISTS [Accounts] (
    [account_id] CHAR(20) PRIMARY KEY NOT NULL,
    [owner] TEXT NOT NULL,
    [balance] NUMBER NOT NULL,
    [city] TEXT NOT NULL
);

.import --csv --skip 1 accounts.csv Accounts

CREATE TABLE IF NOT EXISTS [Fruits] (
    -- _id INTEGER PRIMARY KEY AUTOINCREMENT,
    [fruit] TEXT NOT NULL,
    [vitamin] TEXT NOT NULL,
    [value] NUMBER NOT NULL,
    PRIMARY KEY ([fruit], [vitamin])
);

.import --csv --skip 1 fruits.csv Fruits

CREATE TABLE IF NOT EXISTS Students(
    [id] CHAR(8) PRIMARY KEY NOT NULL,
    [group_id] CHAR(8) NOT NULL,
    [name] TEXT NOT NULL,
    [yob] INTEGER NOT NULL, -- YOB - Year Of Birth
    [ects] INGERER NOT NULL -- European Credit Transfer System
);

.import --csv --skip 1 students.csv Students

