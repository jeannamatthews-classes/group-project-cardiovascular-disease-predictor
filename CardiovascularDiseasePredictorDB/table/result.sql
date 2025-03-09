CREATE TABLE result (
        id              varchar(200) NOT NULL,
        profiler_id     varchar(200),
        patient_id      varchar(200),
        result_rundate  datetime,
        result_value    varchar(200),
        PRIMARY KEY (id),
	FOREIGN KEY (profiler_id) REFERENCES profiler(id),
	FOREIGN KEY (patient_id) REFERENCES patient(id)
);
