DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;
DROP TABLE IF EXISTS cohorts;
DROP SEQUENCE IF EXISTS cohorts_id_seq;

CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  cohort_name VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  student_name VARCHAR(255),
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);

INSERT INTO cohorts (cohort_name) VALUES ('March 2023');
INSERT INTO cohorts (cohort_name) VALUES ('April 2023');
INSERT INTO cohorts (cohort_name) VALUES ('May 2023');
INSERT INTO cohorts (cohort_name) VALUES ('June 2023');

INSERT INTO students (student_name, cohort_id) VALUES ('Joe Blogs', 1);
INSERT INTO students (student_name, cohort_id) VALUES ('Boe Jlogs', 1);
INSERT INTO students (student_name, cohort_id) VALUES ('Mary Jane', 2);
INSERT INTO students (student_name, cohort_id) VALUES ('Jane Mary', 2);
INSERT INTO students (student_name, cohort_id) VALUES ('Bill Ted', 3);
INSERT INTO students (student_name, cohort_id) VALUES ('Ted Bill', 3);
INSERT INTO students (student_name, cohort_id) VALUES ('Tony Stark', 4);
INSERT INTO students (student_name, cohort_id) VALUES ('Stoney Tark', 4);