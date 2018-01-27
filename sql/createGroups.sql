-- Table: public.groups

-- DROP TABLE public.groups;

CREATE TABLE groups
(
    id integer NOT NULL DEFAULT nextval('groups_id_seq'::regclass),
    group_name text COLLATE pg_catalog."default",
    CONSTRAINT groups_pkey PRIMARY KEY (id)
)
