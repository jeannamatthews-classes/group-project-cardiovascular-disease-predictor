CREATE TABLE sample (
        id        varchar(200) NOT NULL,
        firstName varchar(200),
        lastName  varchar(200),
	gender    varchar(1),
        bmi       decimal(10,5),
        age       int,
        height    int,
	smoker    varchar(1),
        PRIMARY KEY (id)
);
