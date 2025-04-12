CREATE TABLE result (
    "id"    INTEGER  ,
    "profiler_id"     INTEGER,
    "sample_id"       INTEGER,
    "record_added"  varchar(20),
    "result"  varchar(200),
    PRIMARY KEY("id"),
    FOREIGN KEY (profiler_id) REFERENCES profiler(id),
    FOREIGN KEY (sample_id) REFERENCES sample(id)
);

