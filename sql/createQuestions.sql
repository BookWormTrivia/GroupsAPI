-- Table: public.questions

-- DROP TABLE public.questions;

CREATE TABLE public.questions
(
    id integer NOT NULL DEFAULT nextval('questions_id_seq'::regclass),
    group_id integer,
    question text COLLATE pg_catalog."default" NOT NULL,
    correct_answer text COLLATE pg_catalog."default" NOT NULL,
    incorrect_answers text[] COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT questions_pkey PRIMARY KEY (id)
)