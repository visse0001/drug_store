PRAGMA foreign_keys = ON;

    DROP TABLE IF EXISTS medicines;

    CREATE TABLE medicines (
        "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        "name"	TEXT NOT NULL,
        "active_substance" TEXT NOT NULL,
        "price"	REAL NOT NULL,
        "dosage_form"	TEXT NOT NULL,
        "capacity" REAL NOT NULL,
        "quantity"	REAL NOT NULL
    );

INSERT INTO "medicines"
VALUES (NULL, 'Apap', 'paracetamol', 8.89 , 'pills', 24, 100);
INSERT INTO "medicines"
VALUES (NULL, 'Allertec WZF', 'cetirizine dihydrochloride', 3.95, 'pills', 7, 50);
INSERT INTO "medicines"
VALUES (NULL, 'Xylorin', 'xylometazolini hydrochloridum', 10.46  , 'aerosol', 18, 30);
INSERT INTO "medicines"
VALUES (NULL, 'Alugastrin', 'dihydroxyaluminium sodium carbonate', 14.29  , 'mixture', 250, 80);


    DROP TABLE IF EXISTS "users";

    CREATE TABLE "users"
    (
        "user_id"       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        "username" TEXT    NOT NULL,
        "password" TEXT    NOT NULL
    );

INSERT INTO "users"
VALUES (NULL, 'test', 'pbkdf2:sha256:150000$9jm1Btmn$d3b64520d6991498b393e16a41109e7f64dff5e684d82ae3f545cf828b73a72a');


