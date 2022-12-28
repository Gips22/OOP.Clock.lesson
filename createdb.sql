CREATE TABLE IF NOT EXISTS public.workss
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    fio character varying(255) COLLATE pg_catalog."default" NOT NULL,
    type character varying(255) COLLATE pg_catalog."default" NOT NULL,
    tema character varying(255) COLLATE pg_catalog."default" NOT NULL,
    part character varying(255) COLLATE pg_catalog."default" NOT NULL,
    element character varying(255) COLLATE pg_catalog."default",
    "time" timestamp without time zone NOT NULL,
    link_start character varying(500) COLLATE pg_catalog."default" NOT NULL,
    comment_start character varying(1000) COLLATE pg_catalog."default",
    CONSTRAINT workss_pkey PRIMARY KEY (id)
)
