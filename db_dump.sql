--
-- PostgreSQL database dump
--

-- Dumped from database version 11.7
-- Dumped by pg_dump version 11.7

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: progetto; Type: SCHEMA; Schema: -; Owner: marco_cavallari
--

CREATE SCHEMA progetto;


ALTER SCHEMA progetto OWNER TO federico_pozzoli;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: table_reservation; Type: TABLE; Schema: progetto; Owner: marco_cavallari
--

CREATE TABLE progetto.table_reservation (
    table_number integer NOT NULL,
    name character varying(20),
    phone character varying(10),
    n_guests integer,
    max_capacity integer
);


ALTER TABLE progetto.table_reservation OWNER TO federico_pozzoli;

--
-- Name: table_reservation_table_number_seq; Type: SEQUENCE; Schema: progetto; Owner: marco_cavallari
--

CREATE SEQUENCE progetto.table_reservation_table_number_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE progetto.table_reservation_table_number_seq OWNER TO federico_pozzoli;

--
-- Name: table_reservation_table_number_seq; Type: SEQUENCE OWNED BY; Schema: progetto; Owner: marco_cavallari
--

ALTER SEQUENCE progetto.table_reservation_table_number_seq OWNED BY progetto.table_reservation.table_number;


--
-- Name: table_reservation table_number; Type: DEFAULT; Schema: progetto; Owner: marco_cavallari
--

ALTER TABLE ONLY progetto.table_reservation ALTER COLUMN table_number SET DEFAULT nextval('progetto.table_reservation_table_number_seq'::regclass);


--
-- Data for Name: table_reservation; Type: TABLE DATA; Schema: progetto; Owner: marco_cavallari
--

COPY progetto.table_reservation (table_number, name, phone, n_guests, max_capacity) FROM stdin;
2	\N	\N	0	2
4	\N	\N	0	4
5	\N	\N	0	4
6	\N	\N	0	4
7	\N	\N	0	6
8	\N	\N	0	6
9	\N	\N	0	8
10	\N	\N	0	8
1	\N	\N	0	2
3	\N	\N	0	4
\.


--
-- Name: table_reservation_table_number_seq; Type: SEQUENCE SET; Schema: progetto; Owner: marco_cavallari
--

SELECT pg_catalog.setval('progetto.table_reservation_table_number_seq', 10, true);


--
-- Name: table_reservation table_reservation_name_key; Type: CONSTRAINT; Schema: progetto; Owner: marco_cavallari
--

ALTER TABLE ONLY progetto.table_reservation
    ADD CONSTRAINT table_reservation_name_key UNIQUE (name);


--
-- Name: table_reservation table_reservation_phone_key; Type: CONSTRAINT; Schema: progetto; Owner: marco_cavallari
--

ALTER TABLE ONLY progetto.table_reservation
    ADD CONSTRAINT table_reservation_phone_key UNIQUE (phone);


--
-- Name: table_reservation table_reservation_pkey; Type: CONSTRAINT; Schema: progetto; Owner: marco_cavallari
--

ALTER TABLE ONLY progetto.table_reservation
    ADD CONSTRAINT table_reservation_pkey PRIMARY KEY (table_number);


--
-- PostgreSQL database dump complete
--
