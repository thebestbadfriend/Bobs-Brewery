--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: addresses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.addresses (
    id integer NOT NULL,
    street_address character varying(200),
    po_box character varying(20),
    city character varying(50),
    state character varying(50),
    zip_code character varying(15),
    is_verified boolean DEFAULT false NOT NULL
);


ALTER TABLE public.addresses OWNER TO postgres;

--
-- Name: addresses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.addresses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.addresses_id_seq OWNER TO postgres;

--
-- Name: addresses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.addresses_id_seq OWNED BY public.addresses.id;


--
-- Name: companies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.companies (
    id integer NOT NULL,
    name character varying(150),
    is_verified boolean DEFAULT false NOT NULL,
    contact_id integer
);


ALTER TABLE public.companies OWNER TO postgres;

--
-- Name: companies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.companies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.companies_id_seq OWNER TO postgres;

--
-- Name: companies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.companies_id_seq OWNED BY public.companies.id;


--
-- Name: contacts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.contacts (
    contact_id integer NOT NULL,
    person_id integer,
    company_id integer,
    status_id integer DEFAULT 1 NOT NULL
);


ALTER TABLE public.contacts OWNER TO postgres;

--
-- Name: contacts_contact_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.contacts_contact_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.contacts_contact_id_seq OWNER TO postgres;

--
-- Name: contacts_contact_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.contacts_contact_id_seq OWNED BY public.contacts.contact_id;


--
-- Name: email_addresses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.email_addresses (
    id integer NOT NULL,
    email_address character varying(75) NOT NULL,
    is_verified boolean DEFAULT false NOT NULL
);


ALTER TABLE public.email_addresses OWNER TO postgres;

--
-- Name: email_addresses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.email_addresses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.email_addresses_id_seq OWNER TO postgres;

--
-- Name: email_addresses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.email_addresses_id_seq OWNED BY public.email_addresses.id;


--
-- Name: fax_numbers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fax_numbers (
    id integer NOT NULL,
    fax_number character varying(15) NOT NULL,
    is_verified boolean DEFAULT false NOT NULL
);


ALTER TABLE public.fax_numbers OWNER TO postgres;

--
-- Name: fax_numbers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fax_numbers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fax_numbers_id_seq OWNER TO postgres;

--
-- Name: fax_numbers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fax_numbers_id_seq OWNED BY public.fax_numbers.id;


--
-- Name: people; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.people (
    id integer NOT NULL,
    first_name character varying(50),
    last_name character varying(50),
    is_verified boolean DEFAULT false NOT NULL,
    contact_id integer
);


ALTER TABLE public.people OWNER TO postgres;

--
-- Name: people_companies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.people_companies (
    person_id integer NOT NULL,
    company_id integer NOT NULL,
    is_verified boolean DEFAULT false NOT NULL
);


ALTER TABLE public.people_companies OWNER TO postgres;

--
-- Name: people_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.people_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.people_id_seq OWNER TO postgres;

--
-- Name: people_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.people_id_seq OWNED BY public.people.id;


--
-- Name: phone_numbers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.phone_numbers (
    id integer NOT NULL,
    phone_number character varying(25) NOT NULL,
    is_verified boolean DEFAULT false NOT NULL
);


ALTER TABLE public.phone_numbers OWNER TO postgres;

--
-- Name: phone_numbers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.phone_numbers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.phone_numbers_id_seq OWNER TO postgres;

--
-- Name: phone_numbers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.phone_numbers_id_seq OWNED BY public.phone_numbers.id;


--
-- Name: status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.status (
    id integer NOT NULL,
    text character varying(100) NOT NULL
);


ALTER TABLE public.status OWNER TO postgres;

--
-- Name: status_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.status_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.status_id_seq OWNER TO postgres;

--
-- Name: status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.status_id_seq OWNED BY public.status.id;


--
-- Name: addresses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.addresses ALTER COLUMN id SET DEFAULT nextval('public.addresses_id_seq'::regclass);


--
-- Name: companies id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.companies ALTER COLUMN id SET DEFAULT nextval('public.companies_id_seq'::regclass);


--
-- Name: contacts contact_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contacts ALTER COLUMN contact_id SET DEFAULT nextval('public.contacts_contact_id_seq'::regclass);


--
-- Name: email_addresses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.email_addresses ALTER COLUMN id SET DEFAULT nextval('public.email_addresses_id_seq'::regclass);


--
-- Name: fax_numbers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fax_numbers ALTER COLUMN id SET DEFAULT nextval('public.fax_numbers_id_seq'::regclass);


--
-- Name: people id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.people ALTER COLUMN id SET DEFAULT nextval('public.people_id_seq'::regclass);


--
-- Name: phone_numbers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.phone_numbers ALTER COLUMN id SET DEFAULT nextval('public.phone_numbers_id_seq'::regclass);


--
-- Name: status id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.status ALTER COLUMN id SET DEFAULT nextval('public.status_id_seq'::regclass);


--
-- Data for Name: addresses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.addresses (id, street_address, po_box, city, state, zip_code, is_verified) FROM stdin;
1	#2 Necessity Ave		Harrison	AR	72601	f
2	#3 Necessity Ave		Harrison	AR	72601	f
3	#8 Lisa Dr		Batesville	AR	72501	f
4	100046 Pete Sims Rd		Harrison	AR	72601	f
5	101 N Olive St		Harrison	AR	72601	f
6	101 Pebble Beach		Harrison	AR	72601	f
7	1010 S Y		Fort Smith	AR	72901	f
8	103 Michael St		Harrison	AR	72601	f
9	103 S Main St		Mountain Home	AR	72653	f
10	103 S Main		Mountain Home	AR	72653	f
11	10338 Devore Dr		Harrison	AR	72601	f
12	104 Bluebird St Ste A		Harrison	AR	72601-1908	f
13	10401 Hwy 65 N		Omaha	AR		f
14	10425 S Hwy 125		Protem	MO	65733	f
15	10500 University Center Drive - Suite 140		Tampa	FL	33612	f
16	107 Oxford St		Harrison	AR	72601	f
17	107 S Pine St		Harrison	AR	72601	f
18	107 W Commercial		Harrison	AR	72601	f
19	10729 Hwy 62		Ash Flat	AR	72513	f
20	1083 Sapsing Hollow Rd		Harrison	AR	72601	f
21	1100 South Hwy 62-65	PO Box 1636	Harrison	AR	72602	f
22	1105 N Main St		Harrison	AR	72601	f
23	1107 So Main		Berryville	AR	72616	f
24	11089 Jones Rd		Everton	AR	72633	f
25	1118 CR 612		Green Forest	AR	72638	f
26	1120 N Willow St		Harrison	AR	72601	f
27	1124 N. Willow		Harrison	AR	72601	f
28	11246 Hwy 125 NW		Peel	AR	72668	f
29	11263 Hickory Ln		Omaha	AR	72662	f
30	113 N Sycamore		Harrison	AR	72601	f
31	11345 Hwy 43 South		Harrison	AR	72601	f
32	11476 Hwy 14		Omaha	AR	72662	f
33	116 N Walnut		Harrison	AR	72601	f
34	11668 Estes Lane		Omaha	AR	72662	f
35	11701 Kinard		North Little Rock	AR	72117	f
36	1200 E 5th		North Little Rock	AR	72114	f
37	12004 Destiny Ln		Lead Hill	AR	72644	f
38	1205 N Spruce St		Harrison	AR	72601	f
39	1207 N Spruce		Harrison	AR	72601	f
40	1207 S Old Missouri Rd	PO Box 282	Springdale	AR	72765-0282	f
41	1208 Speer Dr		Harrison	AR	72601	f
42	12148 Hwy 5 N		Mountain Home	AR	72653	f
43	12181 Hwy 62 E		Harrison	AR	72601	f
44	1227 Lennox		Anderson	IN	46012	f
45	125 Katlyn Ct		Branson	MO	65616	f
46	126 Industrial Park Rd		Harrison	AR	72601	f
47	128 South Street		Mountain Home	AR	72653	f
48	1291 MC 5036		Yellville	AR	72687	f
49	1311 N Spring St		Harrison	AR	72601	f
50	13231 3rd St		Lead Hill	AR	72644	f
51	13401 Hwy 43 S		Harrison	AR	72601	f
52	1347 Marion County 6041		Yellville	AR	72687	f
53	1401 Hwy 112 N		Pocola	OK	74902	f
54	1406 N Main		Harrison	AR	72601	f
55	141 Bellefonte Rd		Harrison	AR	72601	f
56	141 West Van Buren		Eureka Springs	AR	72632	f
57	1412 Hwy 62-65 N		Harrison	AR	72601	f
58	1427 Hwy 62-65 N		Harrison	AR	72601	f
59	14439 Robertson Ln		Omaha	AR	72662	f
60	14445 Hwy 65		St. Joe	AR	72675	f
61	14515 North Outer 40 Drive		Chesterfield	MO	63017-5746	f
62	14515 North Outer Forty Drive - Suite 300		Chesterfield	MO	63017	f
63	1477 Hwy 143		Berryville	AR	72616	f
64	149 MC 6021		Yellville	AR	72687	f
65	1523 MC 7069		Yellville	AR	72687	f
66	15391 N TZ Ranch Dr		Lead Hill	AR	72644	f
67	16023 Swingley Ridge Rd		Chesterfield	MO	63017	f
68	1616 N Spring Rd		Harrison	AR	72601	f
69	165 Mall Road		Hollister	MO	65672	f
70	1650 E Washington		North Little Rock	AR	72114	f
71	1651 S 22nd Ave		Ozark	MO	65721	f
72	1661 CR 933		Alpena	AR	72611	f
73	1709 Union Road		Harrison	AR	72601	f
74	1715 Sierra Ct		Harrison	AR	72601	f
75	1726 Clifty Hwy		Hindsville	AR	72738	f
76	181 A Martin Ct		Harrison	AR	72601	f
77	18131 Hwy 14 N		Yellville	AR	72687	f
78	1835 Bunch Springs Rd		Berryville	AR	72616	f
79	188 Youngblood Dr		Blue Eye	MO	65611	f
80	190 Hines Rd		Branson	MO	65615	f
81	1907 East Bergman		Springfield	MO	65802	f
82	1932 CR 802		Green Forest	AR	72638	f
83	2 Park Drive		Holiday Island	AR	72631	f
84	200 Collins Rd		Branson	MO	65616	f
85	200 South Twin Oaks Drive	PO Box 1335	Tuckerman	AR	72473	f
86	200 West Stephenson		Harrison	AR	72601	f
87	203 N Walnut St ï¿½ Ste A		Harrison	AR	72601-4357	f
88	20434 Old Hwy 65		Omaha	AR	72662	f
89	205 CR 842		Henderson	AR	72544	f
90	205 N Cherry		Harrison	AR	72601	f
91	205 Russell Dr		Harrison	AR	72601	f
92	206 Coy		Harrison	AR	72601	f
93	209 E Wade Ave ï¿½ Suite C		Mountain Home	AR	72653-0004	f
94	209 North Walnut	PO Box 1695	Harrison	AR	72602-1695	f
95	2101 Sulphur Mtn Rd		Harrison	AR	72601-8391	f
96	2104 First National Dr		Harrison	AR	72602-1258	f
97	2104 Taylor St		Searcy	AR	72143	f
98	2119 A Hwy 62-65 S		Harrison	AR	72601	f
99	212 Coy St		Harrison	AR	72601	f
100	212 E Crandale		Harrison	AR	7260	f
101	2131 NC 3320		Harrison	AR	72601	f
102	214 Phillips St		Berryville	AR	72616	f
103	2153 CR 607		Green Forest	AR	72638	f
104	217 N Spring ï¿½ Apt 2		Harrison	AR	72601	f
105	217 Patridge Ave		Harrison	AR	72601	f
106	218 MC 7049		Flippin	AR	72634	f
107	2204 Old Calvert City Rd		Paducah	KY	42001-0000	f
108	222 Cemetery Rd		Harrison	AR	72601	f
109	2221 Country Ln		McKinney	TX	75069	f
110	2237 E Kearney		Springfield	MO	65803	f
111	2255 Cottonwood Rd		Harrison	AR	72601	f
112	2260 Potter		Farmington	AR	72730	f
113	2304 Anvil Dr		Harrison	AR	72601	f
114	2309 CR 420		Berryville	AR	72616	f
115	23370 Divan Rd		Utica	OH	43080	f
116	2385 Winona Dr		Columbus	OH	43235	f
117	24 Quiet Brook Ct		St. Charles	MO	63303	f
118	2401 S Ark	PO Box 490	Russellville	AR	72811	f
119	2437 Lone Oak Dairy Rd		Harrison	AR	72601	f
120	2526 Dustin Lane		Omaha	AR	72662	f
121	2554 Pumpkin Flat Rd		Marshall	AR	72650	f
122	257 Hwy 65 N		Marshall	AR	72650	f
123	2618 Mountain Vista Rd		Harrison	AR	72601	f
124	263 CR 419		Berryville	AR	72616	f
125	266 NC 3690		Harrison	AR	72601	f
126	27 Blacksher Ln		Oakland	AR	72661	f
127	2700 Baughman Cutoff Rd		Harrison	AR	72601	f
128	2700 Salmon Ln		Harrison	AR	72601	f
129	2704 Margie Lane		Metanie	LA		f
130	2711 LBJ Freeway ï¿½ Suite 160		Mabank	TX	75147	f
131	2738 Hwy 7 N		Harrison	AR	72601	f
132	2756 Rock Cliff Dr		Harrison	AR	72601	f
133	2770 Edwards Farm Dr		Harrison	AR	72601	f
134	278 CR 452		Berryville	AR	72616	f
135	2880 McElroy Rd		Harrison	AR	72601	f
136	294 Wilburn Rd		Heber Springs	AR	72543	f
137	2960 Austin Drive		Harrison	AR	72601	f
138	30 Knox Lane		Mountain Home	AR	72653	f
139	301 Peeble Beach Dr		Harrison	AR	72601	f
140	301 S Maple		Harrison	AR	72601	f
141	3016 MC 6014		Yellville	AR	72687	f
142	302 South Main		Mountain Home	AR	72653	f
143	303 North Main ï¿½ Suite 202		Harrison	AR	72601	f
144	3094 MC 3022		Pyatt	AR	72672	f
145	3113 East Washington Ave		N. Little Rock	AR	72114	f
146	312 CR 988		Green Forest	AR	72638	f
147	313 Hodan Dr		Harrison	AR	72601	f
148	317 Industrial Park Rd		Harrison	AR	72601	f
149	319 Shaver St		Berryville	AR	72616	f
150	32 Sheraton Oaks		N Little Rock	AR	72120	f
151	3221 Big Oak Rd		Harrison	AR	72601	f
152	323 Granger Rd		Harrison	AR	72601	f
153	323 Main St		Harrison	AR	72601	f
154	3238 State Hwy 265		Branson	MO	65616	f
155	3252 Hwy 65 N	PO Box 1816	Harrison	AR	72602	f
156	3255 Pinnacle Mtn Rd		Harrison	AR	72601	f
157	331 Coliseum Drive		Newton	MS	39345	f
158	332 South Johnson		Gassville	AR	72635	f
159	3409 MoArk Dr		Harrison	AR	72601	f
160	3443 Hwy 143		Berryville	AR	72616	f
161	3501 US Hwy 160		Walnut Shade	MO	65771	f
162	3530 Crow Mountain Rd		Russellville	AR	72802	f
163	3568 Hwy 221 N		Berryville	AR	72616	f
164	3576 Center Loop		Harrison	AR	72601	f
165	3622 Antique St		Harrison	AR	72601	f
166	3644 Baughman Cutoff Rd		Harrison	AR	72601	f
167	3660 E Sunshine St		Springfield	MO	65809-2820	f
168	3693 Wilkinson Loop		Harrison	AR	72601	f
169	380 Kenzo		St. Joe	AR	72675	f
170	3801 Kelley Street		Springdale	AR	72762-4933	f
171	3864 Black Ranch Rd		Lead Hill	AR	72644	f
172	389 South Fork		Branson	MO	65616	f
173	3892 Railey Creek Rd		Galena	MO	65656	f
174	3969 Black Ranch Rd		Lead Hill	AR	72644	f
175	402 Parkview		Berryville	AR	72616	f
176	4055 East Hwy 76		Kirbyville	MO	65679	f
177	407 Natchez Trace		Harrison	AR	72601	f
178	4078 W Sunset		Springdale	AR	72762-4802	f
179	410 South Hwy 62-65 Bypass		Harrison	AR	72601	f
180	4101 Commercial		Harrison	AR	72601	f
181	4148 Silver Valley Rd		Harrison	AR	72601	f
182	4148 Tracy Ct		Everton	AR	72633	f
183	415 N Rowland		Harrison	AR	72601	f
184	415 S Main		Harrison	AR	72601	f
185	426 Meadow Lake Dr		Harrison	AR	72601	f
186	4304 Mt Rd		Harrison	AR	72601	f
187	4399 Collections Center Dr		Chicago	IL	60693	f
188	44 CR 424		Berryville	AR	72616	f
189	4539 White Oak Rd		Harrison	AR	72601	f
190	4551 Hwy 7 N		Harrison	AR	72601	f
191	4568 MC 5004		Bruno	AR	72682	f
192	4773 N Thompson	PO Box 747	Springdale	AR	72764	f
193	4778 Hwy 65N		Harrison	AR	72601	f
194	4889 Hwy 7 South		Harrison	AR	72601	f
195	4942 Zinc Cutoff Rd		Harrison	AR	72601	f
196	4986 Hwy 43 S		Harrison	AR	72601	f
197	500 S Pine		Harrison	AR	72601	f
198	5003 Wooded Hills Rd		Harrison	AR	72601-8391	f
199	502 Hwy 62-65 Bypass N		Harrison	AR	72601	f
200	5022 Leafdale Blvd		Royal Oak	MI	48073	f
201	504 E Stephenson		Harrison	AR	72601	f
202	5044 Hwy 62 E		Harrison	AR	72601	f
203	5046 MC 5004		Bruno	AR	72682	f
204	509 W Monroe St		Highland	IL	62249	f
205	5109 Hwy 62 E		Harrison	AR	72601	f
206	5154 Hwy 206 E		Harrison	AR	72601	f
207	5240 MC 5004		Bruno	AR	72682	f
208	5301 State Hwy JJ		Hollister	MO	65672	f
209	5316 Huzzan Dr		Harrison	AR	72601	f
210	534 MC 4008		Yellville	AR	72687	f
211	5463 Cottonwood Rd		Harrison	AR	72601	f
212	5467 Fork Creek Rd		Harrison	AR	72601	f
213	5549 Mountain View Dr		Omaha	AR	72662	f
214	5594 Hickory Hills Ln		Harrison	AR	72601	f
215	5597 Castleberry Rd		Harrison	AR	72601	f
216	5608 Scenic Lane		Harrison	AR	72601	f
217	5650 Birch Rd		Harrison	AR	72601	f
218	5743A Hwy 7 N		Harrison	AR	72601	f
219	5779 Marshall Creek Rd		Everton	AR	72633	f
220	5830 Hwy 62	PO Box 547	Eureka Springs	AR	72632	f
221	5997 Parliament Dr		Harrison	AR	72601	f
222	6 Springfield St		Berryville	AR	72616	f
223	601 Hwy 62-65 S		Harrison	AR	72601	f
224	6012 A James Phifer Ln					f
225	605 B Hwy 62-65 N	PO Box 346	Harrison	AR	72601-2200	f
226	605 W Smythe		Harrison	AR	72601	f
227	6170 Sulphur Mtn Rd		Harrison	AR	72601	f
228	618 N Great SW Pkwy		Arlington	TX	76011	f
229	619 Hwy 62/65 N		Harrison	AR	72601	f
230	621 S Sycamore		Harrison	AR	72601	f
231	622 MC 5013		St. Joe	AR	72675	f
232	6247 Dees Rd		Harrison	AR	72601	f
233	625 S Walnut		Harrison	AR	72601	f
234	628 CR 219		Berryville	AR	72616	f
235	650 East South St (Hwy 60)		Marionville	MO	65705	f
236	6512 Saddlebrook Loop		Everton	AR	71633	f
237	6543 Zinc Cutoff Rd		Harrison	AR	72601	f
238	6579 Whispering Pines Rd		Harrison	AR	72601	f
239	6593 Parkwood Ln		Harrison	AR	72601	f
240	67 Timberwolf Circle		Yellville	AR	72687	f
241	6776 Hwy 62		Eureka Springs	AR	72632	f
242	6893 Dick Henry Ln		Harrison	AR	72601	f
243	6904 Parke East Blvd		Tampa	FL	33610	f
244	691 Hwy 206		Everton	AR	72633	f
245	6935 Sulphur Mountain Rd		Harrison	AR	72601	f
246	70 MC 4030		Everton	AR	72633	f
247	7001 Estes Rd		Harrison	AR	72601	f
248	703 N Chestnut		Harrison	AR	72601	f
249	704 Lone Pine Dr		Berryville	AR	72616	f
250	708 West Central		Harrison	AR	72601-8391	f
251	710 Hwy 62/65 S		Harrison	AR	72601	f
252	711 Sunset Ln		Harrison	AR	72602	f
253	715 W Alma		Harrison	AR	72601	f
254	7478 Lotus Ln		Harrison	AR	72601	f
255	7515 Fork Creek Rd		Harrison	AR	72601	f
256	7712 Snowball Creek Rd		Everton	AR	72633	f
257	775 Hwy 201 N ï¿½ Suite A	PO Box 442	Mountain Home	AR	72654-0442	f
258	7923 Hwy 392 W		Harrison	AR	72601	f
259	797 Industrial Park Dr	PO Drawer 391	Waynesboro	MS	39367	f
260	8 Timberwolf Circle		Yellville	AR	72687	f
261	800 S Pine St		Harrison	AR	72601	f
262	8035 Hwy 7 South		Harrison	AR	72601	f
263	805 Gipson Rd		Harrison	AR	72601	f
264	808 East Grand Avenue		Hot Springs	AR	71901	f
265	808 S Oak St		Harrison	AR	72601	f
266	8148 Lost Spur Rd		Harrison	AR	72601-4020	f
267	8358 Eddings Ln		Harrison	AR	72601	f
268	8427 Hwy 62 W		Yellville	AR	72687	f
269	893 Zinc Rd		Harrison	AR	72601	f
270	900 Atlanta		Fort Smith	AR	72901	f
271	900 Pratt Blvd		Elk Grove Village	Il	60007-5119	f
272	9024 Hwy 206 W		Harrison	AR	72601	f
273	906 E Main	PO Box 1390	Green Forest	AR	72638	f
274	9079 Hwy 62 E		Harrison	AR	72601	f
275	908 W Trimble		Berryville	AR	72616	f
276	91 Lark Crest Lane		Harrison	AR	72601	f
277	9109 Hwy 14 S		Yellville	AR	72687	f
278	914 Hwy 62-65 N		Harrison	AR	72601	f
279	915 Olvey Rd		Harrison	AR	72601	f
280	9187 21 N		Berryville	AR	72616	f
281	919 Central Blvd	PO Box 214	Bull Shoals	AR	72619	f
282	920 Hwy 62 & 65 N		Harrison	AR	72601	f
283	921 CR 802		Green Forest	AR	72638	f
284	9224 King Arthur Dr		Dallas	TX	75247	f
285	9238 Sugar Rode		Harrison	AR	72601	f
286	9569 Summit Rd		Harrison	AR	72601	f
287	987 Coley Dr		Mountain Home	AR	72653	f
288	9871 Jackson Ln		Harrison	AR	72601	f
289			Alpena	AR	72611	f
290			Barnsdale	OK	74002	f
291			Bentonville	AR	72712-7155	f
292			Bergman	AR	72615	f
293			Clinton	AR		f
294			Clinton	AR	72031	f
295			Everton	AR	72633	f
296			Evertton	AR		f
297			Harrison	AR		f
298			Harrison	AR	72601	f
299			Harrison	AR	72602	f
300		HC 32 Box 112G	Hasty	AR	72640	f
301		HC 32 Box 168C	Hasty	AR	72640	f
302		HC 33 Box 41	Compton	AR	72624	f
303		HC 37 Box 72	Mount Judea	AR	72655	f
304		HC 62 Box 269	Ozone	AR	72854	f
305		HC 70 Box 311	Jasper	AR	72641	f
306		HC 70 Box 44	Jasper	AR	72641	f
307		HC 72 Box 104D	Jasper	AR	72641	f
308		HC 72 Box 48	Vendor	AR	72683	f
309		HC 73 Box 16B	Marble Falls	AR	72648	f
310	HC 76		Marshall	AR	72650	f
311		HC 79 Box 279	Marshall	AR	72650	f
312		HCR 31 Box 475	Deere	AR	72628	f
313		HCR 70 Box 372	Jasper	AR	72601	f
314		HL 62 Box 2892	Ozone	AR	72854	f
315	Hwy 19 S	PO Box 336	Alton	MO	65606	f
316	Hwy 62-65 N	PO Box 10	Harrison	AR	72601	f
317			Lowell	AR		f
318	Mail Stop 27	PO Box 5087	Portland	OR	97208-5087	f
319			Marshall	AR		f
320			Mountain Home	AR		f
321	North Central Unit	HC 62 Box 300	Calico Rock	AR	72519	f
322			Omaha	AR		f
323			Paragould	AR		f
324		PO Box 10036	Russellville	AR	72812	f
325		PO Box 1031	Harrison	AR	72601	f
326		PO Box 1054	Harrison	AR	72602	f
327		PO Box 1075	Flippin	AR	72634	f
328		PO Box 1078	Harrison	AR	72601	f
329		PO Box 108	Golden	MO	65658	f
330		PO Box 10	Valley Springs	AR	72682	f
331		PO Box 1125	Pine Bluff	AR	71613-1125	f
332	Hwy 62 SW	PO Box 1150	Mountain Home	AR	72654	f
333		PO Box 1155	Harrison	AR	72601	f
334		PO Box 1163	Yellville	AR	72687	f
335		PO Box 1171	Harrison	AR	72602	f
336		PO Box 1191	Harrison	AR	72601	f
337		PO Box 1192	Harrison	AR	72601	f
338		PO Box 123	Summit	AR	72677	f
339		PO Box 1258	Harrison	AR	72602-0159	f
340		PO Box 130	Dennard	AR	72629	f
341		PO Box 132	Deere	AR	72628	f
342		PO Box 136	Golden	MO	65658	f
343		PO Box 1386	Diamond City	AR	72630	f
344		PO Box 138	Mountain Home	AR	72653	f
345		PO Box 1393	Harrison	AR	72601	f
346		PO Box 1393	Harrison	AR	72602	f
347		PO Box 13	Valley Springs	AR	72682	f
348		PO Box 147	Lead Hill	AR	72644	f
349		PO Box 1568	Sherwood	OR	97140	f
350	2020 Hwy 65 S	PO Box 1636	Harrison	AR	72602	f
351		PO Box 16	Alpena	AR	72611	f
352		PO Box 1700	Harrison	AR	72601	f
353		PO Box 1822	Branson	MO	65615	f
354		PO Box 1822	Lead Hill	AR	72644	f
355		PO Box 1899	Harrison	AR	72601	f
356		PO Box 19033	Greensboro	NC	27419-9033	f
357		PO Box 1903	Texarkana	AR	71854	f
358		PO Box 192	Green Forest	AR	72638	f
359		PO Box 1965	Harrison	AR	72602	f
360		PO Box 1991	Harrison	AR	72602	f
361		PO Box 204	Harrison	AR	72602	f
362	6988 Hwy 62 W	PO Box 206	Gassville	AR	72635	f
363		PO Box 207	Harrison	AR	72602	f
364		PO Box 2092	Harrison	AR	72601	f
365		PO Box 214	Lead Hill	AR	72644	f
366		PO Box 2151	Harrison	AR	72601	f
367		PO Box 2155	Harrison	AR	72602	f
368		PO Box 217	Western Grove	AR		f
369		PO Box 2213	Harrison	AR	72601	f
370		PO Box 223	Pyatt	AR	72672	f
371		PO Box 2251	Harrison	AR	72602	f
372		PO Box 2261	Little Rock	AR	72203	f
373		PO Box 2282	Harrison	AR	72602	f
374		PO Box 2306	Harrison	AR	72601	f
375		PO Box 231	Harrison	AR	72602	f
376		PO Box 2334	Harrison	AR	72601	f
377		PO Box 237	Plumerville	AR	72127	f
378		PO Box 2396	Harrison	AR	72602	f
379		PO Box 240	Valley Springs	AR	72682	f
380		PO Box 255	Western Grove	AR	72685	f
381	114 Sisco Ave	PO Box 2568	Harrison	AR	72602	f
382		PO Box 2568	Harrison	AR	72602	f
383		PO Box 2598	Harrison	AR	72601	f
384		PO Box 264	Bergman	AR	72615	f
385		PO Box 278	Chickasha	OK	73023	f
386		PO Box 280055	Tampa	FL	33682-0055	f
387		PO Box 2930	Harrison	AR	72602	f
388		PO Box 293	Harrison	AR	72602	f
389		PO Box 308	Harrison	AR	72602	f
390		PO Box 316	Valley Center	KS	67147	f
391		PO Box 323	Yellville	AR	72687	f
392	81 Jeffries Ln	PO Box 327	Hustonville	KY	40437	f
393		PO Box 336	Lead Hill	AR	72644	f
394		PO Box 344	Green Forest	AR	72638	f
395		PO Box 369	Green Forest	AR	72638	f
396		PO Box 371	Green Forest	AR	72638	f
397		PO Box 375	Alpena	AR	72611	f
398		PO Box 390	Jasper	AR	72641	f
399		PO Box 404	Shell Knob	MO	65747	f
400		PO Box 4067	Fort Smith	AR	72914	f
401		PO Box 413	Lead Hill	AR	72644	f
402		PO Box 433	Lead Hill	AR	72644	f
403		PO Box 447	Middletown	NY	10941	f
404		PO Box 456	Alpena	AR	72611	f
405		PO Box 47	Valley Springs	AR	72682	f
406		PO Box 492	Leslie	AR	72645	f
407		PO Box 500	Norfork	AR	72658-0500	f
408	128-15 26th Ave	PO Box 541550	Flushing	NY	11354-0108	f
409		PO Box 574	Yellville	AR	72687	f
410		PO Box 575	Harrison	AR	72602	f
411		PO Box 57	Harrison	AR	72601	f
412		PO Box 6465	Lee's Summit	MO	64064	f
413		PO Box 647	Jasper	IN	47546-0647	f
414		PO Box 65	Lead Hill	AR	72644	f
415		PO Box 6636	Pine Bluff	AR	71611	f
416		PO Box 663	Berryville	AR	72616	f
417	314 Industrial Park	PO Box 687	Harrison	AR	72602	f
418	E Hwy 14	PO Box 70	Lead Hill	AR	72644	f
419		PO Box 7105 MPO	Springfield	MO	65801	f
420		PO Box 712	Marshall	AR	72650	f
421		PO Box 730197	Dallas	TX	75373-0197	f
422		PO Box 76	Valley Springs	AR	72682	f
423		PO Box 8050	Little Rock	AR	72203-8050	f
424		PO Box 812	Yellville	AR	72687	f
425		PO Box 818	Amite	LA	70422	f
426		PO Box 832	Hollister	MO	65673	f
427		PO Box 840	Harrison	AR	72601	f
428		PO Box 850	Harrison	AR	72601	f
429		PO Box 890108	Charlotte	NC	28289-0108	f
430		PO Box 892	Harrison	AR	72602	f
431		PO Box 935	Rolla	MO	65402	f
432		PO Box 9	Lincoln	AR	72744	f
433		PO Box C	Mountain Home	AR	72653	f
434			Pyatt	AR		f
435	Rally Hill Rd					f
436	Road Runner Ln		Harrison	AR	72601	f
437		RR 2 Box 506	Dardanelle	AR	72834	f
438		Rt 1 Box 1010	Shell Knob	MO	65747	f
439		Rt 1 Box 187-H	Houston	AR	72072	f
440		Rt 1 Box 395	Western Grove	AR	72685	f
441		Rt 1 Box 430	Western Grove	AR	72685	f
442		Rt 1 Box 495	Western Grove	AR	72685	f
443		Rt 1 Box 522	Dardnell	AR	72834	f
444		Rt 1 Box 538	Western Grove	AR	72685	f
445		Rt 1 Box 	Osceola	MO	64776	f
446		Rt 5 Box 318	Harrison	AR	72601	f
447	Rt 5		Marshall	AR	72650	f
448			Springfield	MO		f
449			St. Joe	AR	72675	f
450			West Plains	MO	65775	f
451			Yellville	AR		f
\.


--
-- Data for Name: companies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.companies (id, name, is_verified, contact_id) FROM stdin;
1	A & R Building Components	f	1
2	A&C Construction	f	2
3	A+ Tire & Alignment	f	3
4	Ace Hardware	f	4
5	Advance Enterprises	f	5
6	Advertising Express	f	6
7	Affordable Builders Blacksher & Co Inc	f	7
8	Affordable Building and Design	f	8
9	Aflac	f	9
10	Alignment Plus	f	10
11	Alltel	f	11
12	Alltel Marketing	f	12
13	Amazing Grace Missionary Baptist Church	f	13
14	American Freightways	f	14
15	American Interstate Insurance Company	f	15
16	Anderson Construction	f	16
17	Appraisal Services of Arkansas Inc	f	17
18	Arkansas Building Products	f	18
19	Arkansas Capital Structures	f	19
20	Arkansas Carbide Saw & Tool Co. Inc	f	20
21	Arkansas Department of Environmental Quality	f	21
22	Arkansas Highway Department	f	22
23	Arkansas Log Homes LLC	f	23
24	Arkansas State Board of Collection Agencies	f	24
25	Arkansas Western Gas	f	25
26	Arnold Pump Service	f	26
27	Arrow Craft	f	27
28	AZ Renovation & Restoration	f	28
29	B-Line Systems Inc	f	29
30	B&B Supply	f	30
31	B&P One Stop	f	31
32	Ball & Prier Tire	f	32
33	Bank of the Ozarks (Bellefonte)	f	33
34	Bank of the Ozarks (Main Office)	f	34
35	Bank of the Ozarks (North)	f	35
36	Bar L Homes LLC	f	36
37	Baty Construction Co	f	37
38	BCB Inc	f	38
39	BCI Corporation	f	39
40	Bear Construction	f	40
41	Bear Creek Automotive	f	41
42	Bennett Lumber Company	f	42
43	Bibler Brothers Lumber Co	f	43
44	Biewer Lumber	f	44
45	Bill Parker Construction	f	45
46	Bilt-Rite Construction	f	46
47	Birdsong Builders	f	47
48	BK&P Services	f	48
49	Bob's Do-It-Best	f	49
50	Bob's Powerhouse Antiques & Construction	f	50
51	Bowser's Metal Supply LLC	f	51
52	Brewer's Truss	f	52
53	Brittney Inc	f	53
54	Brockmans Auto	f	54
55	Brooks Construction	f	55
56	Bruce Eddings Construction	f	56
57	Bruffett Construction	f	57
58	Buck Construction	f	58
59	Buffalo Signs	f	59
60	Build It Construction	f	60
61	Builders Pro Construction Services LLC	f	61
62	C.L. Construction	f	62
63	C&L Trucking	f	63
64	Campbell Insurance Agency Inc	f	64
65	Card Development LLC	f	65
66	Carter's Creations	f	66
67	CB Oil Company Inc	f	67
68	CBERG Construction LLC	f	68
69	Champlin Crane & Welding Service	f	69
70	Charles Apple & Company	f	70
71	Circle G Trusses	f	71
72	Circuit City Inc	f	72
73	Claridge Products & Equipment Co	f	73
74	Clark Office Products	f	74
75	Cobalt Truss	f	75
76	Cole-Bilt Buildings	f	76
77	Collier Auto Supply	f	77
78	Community First Bank	f	78
79	Continental Timber	f	79
80	Contractor's Supply	f	80
81	Conway Guiteau Lumber	f	81
82	Cool Town Trucking	f	82
83	Country Haven Construction	f	83
84	Crouse Construction Co	f	84
85	Curtis Heating	f	85
86	Custom Builders	f	86
87	Custom Building Concepts	f	87
88	D&H Glass	f	88
89	Dan Bennett Construction	f	89
90	Danny Norton Builders	f	90
91	Davis Roof Trus Mfg. Co. Inc.	f	91
92	DeJager Construction & Log Homes	f	92
93	Denny Smith Roofing & Construction LLC	f	93
94	Derek Townlin Roofing	f	94
95	Derickson Lumber Co LLC	f	95
96	Don Williams Construction	f	96
97	Dressi Building Company	f	97
98	Drewry Custom Builders Inc	f	98
99	E.A. Martin Company	f	99
100	Eagle Metal	f	100
101	Eastman Booth Inc	f	101
102	EcoQuest International	f	102
103	Engineering Services Inc	f	103
104	Entergy	f	104
105	Environmental	f	105
106	Evans & Associates Residential Contractors Inc	f	106
107	Evans Building Supply	f	107
108	F.B.R. Co.	f	108
109	FBR Co.	f	109
110	First Federal Bank	f	110
111	Flaming Eagle Express	f	111
112	Flemming Construction	f	112
113	Fountain Financial & Tax	f	113
114	Frank Turner Construction	f	114
115	G. L. Still Construction	f	115
116	Gary Brisco Heat Air & Electric	f	116
117	GB Services Inc	f	117
118	Glen Beach	f	118
119	Grady W Jones Company	f	119
120	Green Forest Construction	f	120
121	Guy's Sign Co.	f	121
122	H&H Construction	f	122
123	H&R Block	f	123
124	Hagston Homes & Builders	f	124
125	Hamilton Classics	f	125
126	Hammond Construction	f	126
127	Hanby Lumber Co.	f	127
128	Hancock Custom Finishing	f	128
129	Handyman Plus	f	129
130	Harness Roofing Inc	f	130
131	Harold Saeler Auto Exchange	f	131
132	Harrison Auto Salvage	f	132
133	Harrison Fire Extinguisher Co.	f	133
134	Harrison Overhead Door	f	134
135	Harrison Towing	f	135
136	Hart & Associates Inc	f	136
137	Heart Homes of Harrison	f	137
138	Helton Crane & Rigging Inc	f	138
139	Henley Construction	f	139
140	Henry Adams Inc	f	140
141	Heritage Realty	f	141
142	Hickory Hill Insurance	f	142
143	Hill Country Hardware Inc	f	143
144	Hixson Lumber Sales	f	144
145	Hoeme Distributing Co.	f	145
146	Horn Construction	f	146
147	Hostetler's Seamless Gutter	f	147
148	HOT Contractors	f	148
149	Hudson Construction	f	149
150	Hugg & Hall Equipment Company	f	150
151	Hy-Tech Auto Repair	f	151
152	Interim Personnel	f	152
153	J & B Auto Service	f	153
154	J. M. Grab Construction	f	154
155	JD's Trucking	f	155
156	Jerry Jackson Realty	f	156
157	Jim's Refuse Service	f	157
158	John's Construction	f	158
159	Johnson Enterprise	f	159
160	Judy's Insulation Co.	f	160
161	KBCN 104.3	f	161
162	KCWD	f	162
163	Keathley & Patterson Electric Co.	f	163
164	Kenny Cackley Construction	f	164
165	Kevin Beaver	f	165
166	Kimbrough Company Inc	f	166
167	Kirk's Excavation Inc	f	167
168	KTLO AM-FM	f	168
169	Kuenzle Construction	f	169
170	L & H Builders	f	170
171	L & L Construction	f	171
172	L & L Oil	f	172
173	L & R Fabracators	f	173
174	Lakewood Resort	f	174
175	Latco Wood Truss	f	175
176	LAUR	f	176
177	Lazy Hog Lodge	f	177
178	Lester Davidson / Jack Rigsby Construction	f	178
179	Liberty National Insurance	f	179
180	Liberty Tax Service	f	180
181	Lift-All Crane Service	f	181
182	Load N Go Trailer Manufacturing	f	182
183	Log Crafters	f	183
184	Lone Elk Cabins	f	184
185	Louisiana Forest Products	f	185
186	Lowe Bros Construction	f	186
187	Lowe's Construction	f	187
188	Lowes	f	188
189	Magness Oil Co	f	189
190	Martin Construction	f	190
191	Massengale Transport	f	191
192	Masterman's	f	192
193	Meek's Portable Welding	f	193
194	Meeks	f	194
195	Metro Construction	f	195
196	Mike Smith Electric	f	196
197	Mike's Heating & Cooling	f	197
198	Miller Hardware	f	198
199	MiTek	f	199
200	MiTek Collections Center	f	200
201	Mitiserve Restoration LLC	f	201
202	Modern Parts	f	202
203	NCAHBA	f	203
204	Newman's Body Shop	f	204
205	Next Door	f	205
206	No Hidden Cost Construction	f	206
207	Noah'z Ark Cabins LLC	f	207
208	North American	f	208
209	North American Products	f	209
210	North Ark Tree Svc	f	210
211	North Central Arkansas Structures	f	211
212	North Pacific	f	212
213	North Star Management	f	213
214	Northark Parts	f	214
215	Northwest Regional Housing Authority	f	215
216	Office Max	f	216
217	Oklahoma Tal. Mfg. Inc	f	217
218	Ozark Bearing and Supply Inc	f	218
219	Ozark Construction Co.	f	219
220	Ozark Custom Country Homes	f	220
221	Ozark Mountain Properties	f	221
222	Ozark Timber Freight Inc.	f	222
223	Pack's Lumber & Carpet	f	223
224	Pan Pacific Forest Products	f	224
225	Paymaster Technologies Inc	f	225
226	Payne Tool Service	f	226
227	Pella Window & Door	f	227
228	Petra Investments	f	228
229	Pine Creek Lumber Inc	f	229
230	Pitman Creek Wholesale	f	230
231	Plunkett Dstributing	f	231
232	Pole Barns Plus	f	232
233	Powell Hardware	f	233
234	Powell's Ace Hardware LLC	f	234
235	Precision Construction	f	235
236	Premium Tax Service	f	236
237	PSI Tire Center	f	237
238	Quality Construction & Remodeling LLC	f	238
239	Quality Wholesale	f	239
240	R & G Handyman & Construction	f	240
241	R W Trucking	f	241
242	Race Brothers Farm	f	242
243	Randall Dickinson Construction	f	243
244	Re/Max Unlimited Inc	f	244
245	Realco Investments	f	245
246	Reliable	f	246
247	Rent Me! Bucket Truck Service	f	247
248	Richardson Oil Co	f	248
249	Richardson's Construction	f	249
250	Rickett's Construction	f	250
251	Ridgemonte Developments LLC	f	251
252	Robbins Engineering Inc	f	252
253	Robbins Lumber Company	f	253
254	Robotham Construction	f	254
255	RRK Built Homes	f	255
256	Rusty Dees Construction	f	256
257	Sam's Club #8296	f	257
258	Screaman Freeman Conner	f	258
259	Self Help Housing	f	259
260	Shumaker Battery	f	260
261	Simpson Strong-Tie	f	261
262	SMBZ Construction & Excavation	f	262
263	Snap-On	f	263
264	Snow Construction	f	264
265	Southern Construction LLC	f	265
266	State Line Crane Service	f	266
267	Steve Gilliam Construction	f	267
268	Steve Roberts Construction	f	268
269	Steve's Renovation	f	269
270	Stewart Construction and Electric LLC	f	270
271	Straigh Line Construction LLC	f	271
272	Structural Systems Engineering	f	272
273	Superior Builders	f	273
274	Table Rock Development LLC	f	274
275	Tanksley & Randalph Construction	f	275
276	Tanner Hardware & Lumber	f	276
277	The Lumber Shed Truss Co.	f	277
278	The Paymaster System	f	278
279	The Wood Connection LLC	f	279
280	Three Oaks Construction Inc	f	280
281	Tim Hottinger Construction Company Inc	f	281
282	Timberline Forest Products LLC	f	282
283	TLD Construction LLC	f	283
284	TM Ramsey Investments LLC	f	284
285	Todd's Construction	f	285
286	Todd's Hydraulics	f	286
287	Tom's Welding	f	287
288	Town-N-Country Mini Barns	f	288
289	Tractor Supply	f	289
290	Travers Tool Co. Inc.	f	290
291	Trogdon Repair Service	f	291
292	Truebuild Construction	f	292
293	Truslock Inc	f	293
294	Unemployment	f	294
295	United Country	f	295
296	United Insurance	f	296
297	United-Bilt Homes	f	297
298	UPS	f	298
299	USDOT	f	299
300	Valley Springs Fire Department	f	300
301	Valley Springs School	f	301
302	Valley Springs Water Department	f	302
303	VLS Construction Inc	f	303
304	Wal-Mart	f	304
305	Wallace Construction	f	305
306	We Can Do It	f	306
307	Wes Meyers Construction LLC	f	307
308	Windstream	f	308
309	Wood's Wrecker Service	f	309
310	Worley's Tire	f	310
311	Worth Tax & Bookkeeping Service	f	311
312	WPL Weatherization Partners Ltd.	f	312
313	Xero Fax Inc	f	313
314	Yeager Auto Salvage	f	314
315	Yover & Sons Construction Inc	f	315
\.


--
-- Data for Name: contacts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.contacts (contact_id, person_id, company_id, status_id) FROM stdin;
1	\N	1	1
2	\N	2	1
3	\N	3	1
4	\N	4	1
5	\N	5	1
6	\N	6	1
7	\N	7	1
8	\N	8	1
9	\N	9	1
10	\N	10	1
11	\N	11	1
12	\N	12	1
13	\N	13	1
14	\N	14	1
15	\N	15	1
16	\N	16	1
17	\N	17	1
18	\N	18	1
19	\N	19	1
20	\N	20	1
21	\N	21	1
22	\N	22	1
23	\N	23	1
24	\N	24	1
25	\N	25	1
26	\N	26	1
27	\N	27	1
28	\N	28	1
29	\N	29	1
30	\N	30	1
31	\N	31	1
32	\N	32	1
33	\N	33	1
34	\N	34	1
35	\N	35	1
36	\N	36	1
37	\N	37	1
38	\N	38	1
39	\N	39	1
40	\N	40	1
41	\N	41	1
42	\N	42	1
43	\N	43	1
44	\N	44	1
45	\N	45	1
46	\N	46	1
47	\N	47	1
48	\N	48	1
49	\N	49	1
50	\N	50	1
51	\N	51	1
52	\N	52	1
53	\N	53	1
54	\N	54	1
55	\N	55	1
56	\N	56	1
57	\N	57	1
58	\N	58	1
59	\N	59	1
60	\N	60	1
61	\N	61	1
62	\N	62	1
63	\N	63	1
64	\N	64	1
65	\N	65	1
66	\N	66	1
67	\N	67	1
68	\N	68	1
69	\N	69	1
70	\N	70	1
71	\N	71	1
72	\N	72	1
73	\N	73	1
74	\N	74	1
75	\N	75	1
76	\N	76	1
77	\N	77	1
78	\N	78	1
79	\N	79	1
80	\N	80	1
81	\N	81	1
82	\N	82	1
83	\N	83	1
84	\N	84	1
85	\N	85	1
86	\N	86	1
87	\N	87	1
88	\N	88	1
89	\N	89	1
90	\N	90	1
91	\N	91	1
92	\N	92	1
93	\N	93	1
94	\N	94	1
95	\N	95	1
96	\N	96	1
97	\N	97	1
98	\N	98	1
99	\N	99	1
100	\N	100	1
101	\N	101	1
102	\N	102	1
103	\N	103	1
104	\N	104	1
105	\N	105	1
106	\N	106	1
107	\N	107	1
108	\N	108	1
109	\N	109	1
110	\N	110	1
111	\N	111	1
112	\N	112	1
113	\N	113	1
114	\N	114	1
115	\N	115	1
116	\N	116	1
117	\N	117	1
118	\N	118	1
119	\N	119	1
120	\N	120	1
121	\N	121	1
122	\N	122	1
123	\N	123	1
124	\N	124	1
125	\N	125	1
126	\N	126	1
127	\N	127	1
128	\N	128	1
129	\N	129	1
130	\N	130	1
131	\N	131	1
132	\N	132	1
133	\N	133	1
134	\N	134	1
135	\N	135	1
136	\N	136	1
137	\N	137	1
138	\N	138	1
139	\N	139	1
140	\N	140	1
141	\N	141	1
142	\N	142	1
143	\N	143	1
144	\N	144	1
145	\N	145	1
146	\N	146	1
147	\N	147	1
148	\N	148	1
149	\N	149	1
150	\N	150	1
151	\N	151	1
152	\N	152	1
153	\N	153	1
154	\N	154	1
155	\N	155	1
156	\N	156	1
157	\N	157	1
158	\N	158	1
159	\N	159	1
160	\N	160	1
161	\N	161	1
162	\N	162	1
163	\N	163	1
164	\N	164	1
165	\N	165	1
166	\N	166	1
167	\N	167	1
168	\N	168	1
169	\N	169	1
170	\N	170	1
171	\N	171	1
172	\N	172	1
173	\N	173	1
174	\N	174	1
175	\N	175	1
176	\N	176	1
177	\N	177	1
178	\N	178	1
179	\N	179	1
180	\N	180	1
181	\N	181	1
182	\N	182	1
183	\N	183	1
184	\N	184	1
185	\N	185	1
186	\N	186	1
187	\N	187	1
188	\N	188	1
189	\N	189	1
190	\N	190	1
191	\N	191	1
192	\N	192	1
193	\N	193	1
194	\N	194	1
195	\N	195	1
196	\N	196	1
197	\N	197	1
198	\N	198	1
199	\N	199	1
200	\N	200	1
201	\N	201	1
202	\N	202	1
203	\N	203	1
204	\N	204	1
205	\N	205	1
206	\N	206	1
207	\N	207	1
208	\N	208	1
209	\N	209	1
210	\N	210	1
211	\N	211	1
212	\N	212	1
213	\N	213	1
214	\N	214	1
215	\N	215	1
216	\N	216	1
217	\N	217	1
218	\N	218	1
219	\N	219	1
220	\N	220	1
221	\N	221	1
222	\N	222	1
223	\N	223	1
224	\N	224	1
225	\N	225	1
226	\N	226	1
227	\N	227	1
228	\N	228	1
229	\N	229	1
230	\N	230	1
231	\N	231	1
232	\N	232	1
233	\N	233	1
234	\N	234	1
235	\N	235	1
236	\N	236	1
237	\N	237	1
238	\N	238	1
239	\N	239	1
240	\N	240	1
241	\N	241	1
242	\N	242	1
243	\N	243	1
244	\N	244	1
245	\N	245	1
246	\N	246	1
247	\N	247	1
248	\N	248	1
249	\N	249	1
250	\N	250	1
251	\N	251	1
252	\N	252	1
253	\N	253	1
254	\N	254	1
255	\N	255	1
256	\N	256	1
257	\N	257	1
258	\N	258	1
259	\N	259	1
260	\N	260	1
261	\N	261	1
262	\N	262	1
263	\N	263	1
264	\N	264	1
265	\N	265	1
266	\N	266	1
267	\N	267	1
268	\N	268	1
269	\N	269	1
270	\N	270	1
271	\N	271	1
272	\N	272	1
273	\N	273	1
274	\N	274	1
275	\N	275	1
276	\N	276	1
277	\N	277	1
278	\N	278	1
279	\N	279	1
280	\N	280	1
281	\N	281	1
282	\N	282	1
283	\N	283	1
284	\N	284	1
285	\N	285	1
286	\N	286	1
287	\N	287	1
288	\N	288	1
289	\N	289	1
290	\N	290	1
291	\N	291	1
292	\N	292	1
293	\N	293	1
294	\N	294	1
295	\N	295	1
296	\N	296	1
297	\N	297	1
298	\N	298	1
299	\N	299	1
300	\N	300	1
301	\N	301	1
302	\N	302	1
303	\N	303	1
304	\N	304	1
305	\N	305	1
306	\N	306	1
307	\N	307	1
308	\N	308	1
309	\N	309	1
310	\N	310	1
311	\N	311	1
312	\N	312	1
313	\N	313	1
314	\N	314	1
315	\N	315	1
316	1	\N	1
317	2	\N	1
318	3	\N	1
319	4	\N	1
320	5	\N	1
321	6	\N	1
322	7	\N	1
323	8	\N	1
324	9	\N	1
325	10	\N	1
326	11	\N	1
327	12	\N	1
328	13	\N	1
329	14	\N	1
330	15	\N	1
331	16	\N	1
332	17	\N	1
333	18	\N	1
334	19	\N	1
335	20	\N	1
336	21	\N	1
337	22	\N	1
338	23	\N	1
339	24	\N	1
340	25	\N	1
341	26	\N	1
342	27	\N	1
343	28	\N	1
344	29	\N	1
345	30	\N	1
346	31	\N	1
347	32	\N	1
348	33	\N	1
349	34	\N	1
350	35	\N	1
351	36	\N	1
352	37	\N	1
353	38	\N	1
354	39	\N	1
355	40	\N	1
356	41	\N	1
357	42	\N	1
358	43	\N	1
359	44	\N	1
360	45	\N	1
361	46	\N	1
362	47	\N	1
363	48	\N	1
364	49	\N	1
365	50	\N	1
366	51	\N	1
367	52	\N	1
368	53	\N	1
369	54	\N	1
370	55	\N	1
371	56	\N	1
372	57	\N	1
373	58	\N	1
374	59	\N	1
375	60	\N	1
376	61	\N	1
377	62	\N	1
378	63	\N	1
379	64	\N	1
380	65	\N	1
381	66	\N	1
382	67	\N	1
383	68	\N	1
384	69	\N	1
385	70	\N	1
386	71	\N	1
387	72	\N	1
388	73	\N	1
389	74	\N	1
390	75	\N	1
391	76	\N	1
392	77	\N	1
393	78	\N	1
394	79	\N	1
395	80	\N	1
396	81	\N	1
397	82	\N	1
398	83	\N	1
399	84	\N	1
400	85	\N	1
401	86	\N	1
402	87	\N	1
403	88	\N	1
404	89	\N	1
405	90	\N	1
406	91	\N	1
407	92	\N	1
408	93	\N	1
409	94	\N	1
410	95	\N	1
411	96	\N	1
412	97	\N	1
413	98	\N	1
414	99	\N	1
415	100	\N	1
416	101	\N	1
417	102	\N	1
418	103	\N	1
419	104	\N	1
420	105	\N	1
421	106	\N	1
422	107	\N	1
423	108	\N	1
424	109	\N	1
425	110	\N	1
426	111	\N	1
427	112	\N	1
428	113	\N	1
429	114	\N	1
430	115	\N	1
431	116	\N	1
432	117	\N	1
433	118	\N	1
434	119	\N	1
435	120	\N	1
436	121	\N	1
437	122	\N	1
438	123	\N	1
439	124	\N	1
440	125	\N	1
441	126	\N	1
442	127	\N	1
443	128	\N	1
444	129	\N	1
445	130	\N	1
446	131	\N	1
447	132	\N	1
448	133	\N	1
449	134	\N	1
450	135	\N	1
451	136	\N	1
452	137	\N	1
453	138	\N	1
454	139	\N	1
455	140	\N	1
456	141	\N	1
457	142	\N	1
458	143	\N	1
459	144	\N	1
460	145	\N	1
461	146	\N	1
462	147	\N	1
463	148	\N	1
464	149	\N	1
465	150	\N	1
466	151	\N	1
467	152	\N	1
468	153	\N	1
469	154	\N	1
470	155	\N	1
471	156	\N	1
472	157	\N	1
473	158	\N	1
474	159	\N	1
475	160	\N	1
476	161	\N	1
477	162	\N	1
478	163	\N	1
479	164	\N	1
480	165	\N	1
481	166	\N	1
482	167	\N	1
483	168	\N	1
484	169	\N	1
485	170	\N	1
486	171	\N	1
487	172	\N	1
488	173	\N	1
489	174	\N	1
490	175	\N	1
491	176	\N	1
492	177	\N	1
493	178	\N	1
494	179	\N	1
495	180	\N	1
496	181	\N	1
497	182	\N	1
498	183	\N	1
499	184	\N	1
500	185	\N	1
501	186	\N	1
502	187	\N	1
503	188	\N	1
504	189	\N	1
505	190	\N	1
506	191	\N	1
507	192	\N	1
508	193	\N	1
509	194	\N	1
510	195	\N	1
511	196	\N	1
512	197	\N	1
513	198	\N	1
514	199	\N	1
515	200	\N	1
516	201	\N	1
517	202	\N	1
518	203	\N	1
519	204	\N	1
520	205	\N	1
521	206	\N	1
522	207	\N	1
523	208	\N	1
524	209	\N	1
525	210	\N	1
526	211	\N	1
527	212	\N	1
528	213	\N	1
529	214	\N	1
530	215	\N	1
531	216	\N	1
532	217	\N	1
533	218	\N	1
534	219	\N	1
535	220	\N	1
536	221	\N	1
537	222	\N	1
538	223	\N	1
539	224	\N	1
540	225	\N	1
541	226	\N	1
542	227	\N	1
543	228	\N	1
544	229	\N	1
545	230	\N	1
546	231	\N	1
547	232	\N	1
548	233	\N	1
549	234	\N	1
550	235	\N	1
551	236	\N	1
552	237	\N	1
553	238	\N	1
554	239	\N	1
555	240	\N	1
556	241	\N	1
557	242	\N	1
558	243	\N	1
559	244	\N	1
560	245	\N	1
561	246	\N	1
562	247	\N	1
563	248	\N	1
564	249	\N	1
565	250	\N	1
566	251	\N	1
567	252	\N	1
568	253	\N	1
569	254	\N	1
570	255	\N	1
571	256	\N	1
572	257	\N	1
573	258	\N	1
574	259	\N	1
575	260	\N	1
576	261	\N	1
577	262	\N	1
578	263	\N	1
579	264	\N	1
580	265	\N	1
581	266	\N	1
582	267	\N	1
583	268	\N	1
584	269	\N	1
585	270	\N	1
586	271	\N	1
587	272	\N	1
588	273	\N	1
589	274	\N	1
590	275	\N	1
591	276	\N	1
592	277	\N	1
593	278	\N	1
594	279	\N	1
595	280	\N	1
596	281	\N	1
597	282	\N	1
598	283	\N	1
599	284	\N	1
600	285	\N	1
601	286	\N	1
602	287	\N	1
603	288	\N	1
604	289	\N	1
605	290	\N	1
606	291	\N	1
607	292	\N	1
608	293	\N	1
609	294	\N	1
610	295	\N	1
611	296	\N	1
612	297	\N	1
613	298	\N	1
614	299	\N	1
615	300	\N	1
616	301	\N	1
617	302	\N	1
618	303	\N	1
619	304	\N	1
620	305	\N	1
621	306	\N	1
622	307	\N	1
623	308	\N	1
624	309	\N	1
625	310	\N	1
626	311	\N	1
627	312	\N	1
628	313	\N	1
629	314	\N	1
630	315	\N	1
631	316	\N	1
632	317	\N	1
633	318	\N	1
634	319	\N	1
635	320	\N	1
636	321	\N	1
637	322	\N	1
638	323	\N	1
639	324	\N	1
640	325	\N	1
641	326	\N	1
642	327	\N	1
643	328	\N	1
644	329	\N	1
645	330	\N	1
646	331	\N	1
647	332	\N	1
648	333	\N	1
649	334	\N	1
650	335	\N	1
651	336	\N	1
652	337	\N	1
653	338	\N	1
654	339	\N	1
655	340	\N	1
656	341	\N	1
657	342	\N	1
658	343	\N	1
659	344	\N	1
660	345	\N	1
661	346	\N	1
662	347	\N	1
663	348	\N	1
664	349	\N	1
665	350	\N	1
666	351	\N	1
667	352	\N	1
668	353	\N	1
669	354	\N	1
670	355	\N	1
671	356	\N	1
672	357	\N	1
673	358	\N	1
674	359	\N	1
675	360	\N	1
676	361	\N	1
677	362	\N	1
678	363	\N	1
679	364	\N	1
680	365	\N	1
681	366	\N	1
682	367	\N	1
683	368	\N	1
684	369	\N	1
685	370	\N	1
686	371	\N	1
687	372	\N	1
688	373	\N	1
689	374	\N	1
690	375	\N	1
691	376	\N	1
692	377	\N	1
693	378	\N	1
694	379	\N	1
695	380	\N	1
696	381	\N	1
697	382	\N	1
698	383	\N	1
699	384	\N	1
700	385	\N	1
701	386	\N	1
702	387	\N	1
703	388	\N	1
704	389	\N	1
705	390	\N	1
706	391	\N	1
707	392	\N	1
708	393	\N	1
709	394	\N	1
710	395	\N	1
711	396	\N	1
712	397	\N	1
713	398	\N	1
714	399	\N	1
715	400	\N	1
716	401	\N	1
717	402	\N	1
718	403	\N	1
719	404	\N	1
720	405	\N	1
721	406	\N	1
722	407	\N	1
723	408	\N	1
724	409	\N	1
725	410	\N	1
726	411	\N	1
727	412	\N	1
728	413	\N	1
729	414	\N	1
730	415	\N	1
731	416	\N	1
732	417	\N	1
733	418	\N	1
734	419	\N	1
735	420	\N	1
736	421	\N	1
737	422	\N	1
738	423	\N	1
739	424	\N	1
740	425	\N	1
741	426	\N	1
742	427	\N	1
743	428	\N	1
744	429	\N	1
745	430	\N	1
\.


--
-- Data for Name: email_addresses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.email_addresses (id, email_address, is_verified) FROM stdin;
\.


--
-- Data for Name: fax_numbers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fax_numbers (id, fax_number, is_verified) FROM stdin;
1	417-869-6961	f
2	870-580-0584	f
3	918-626-3741	f
4	501-372-5383	f
5	248-280-1679	f
6	870-741-0121	f
7	870-743-5518	f
8	870-751-2941	f
9	810-561-5761	f
10	870-741-0226	f
11	870-204-6311	f
12	417-866-1350	f
13	870-741-1098	f
14	479-751-8746	f
15	870-365-3739	f
16	501-967-8139	f
17	618-654-1917	f
18	501-890-8565	f
19	870-349-2883	f
20	870-429-6490	f
21	870-741-4714	f
22	870-435-6031	f
23	870-741-3828	f
24	870-741-9812	f
25	870-425-0757	f
26	870-741-7461	f
27	870-391-8025	f
28	501-872-8103	f
29	479-751-0218	f
30	870-499-3271	f
31	417-544-1985	f
32	870-743-5997	f
33	870-741-8532	f
34	870-448-5380	f
35	870-424-4044	f
36	870-446-5239	f
37	870-365-0886	f
38	903-887-1723	f
39	870-741-7864	f
40	870-425-9747	f
41	413-812-5682	f
42	479-253-9182	f
43	870-424-3333	f
44	870-438-6572	f
45	870-741-8853	f
46	870-741-6630	f
47	870-743-6686	f
48	479-751-5090	f
49	501-354-3279	f
50	870-741-3016	f
51	870-741-8986	f
52	870-741-8024	f
53	417-335-5706	f
54	870-743-4030	f
55	870-743-2226	f
56	870-743-9491	f
57	479-253-0241	f
58	870-741-0137	f
59	479-750-1095	f
60	417-336-2233	f
61	501-759-2885	f
62	870-429-5279	f
63	870-741-2700	f
64	870-743-1168	f
65	870-741-9702	f
66	870-424-4314	f
67	417-785-9810	f
68	417-334-3692	f
69	870-741-7480	f
70	314-434-1587	f
71	417-332-0325	f
72	503-590-7421	f
73	800-525-0396	f
74	870-741-8148	f
75	870-743-6510	f
76	870-741-8103	f
77	870-741-0970	f
78	314-851-8529	f
79	870-425-5950	f
80	870-423-6330	f
81	870-741-7896	f
82	870-741-2741	f
83	870-449-5579	f
84	870-741-9234	f
85	870-741-9246	f
86	817-633-4174	f
87	870-467-5114	f
88	601-735-2602	f
89	501-745-4911	f
90	417-778-7411	f
91	870-741-0788	f
92	870-438-4858	f
93	870-427-3825	f
94	870-438-6927	f
95	870-423-2034	f
96	479-253-0010	f
97	479-789-2724	f
98	870-438-6030	f
99	870-365-7750	f
100	870-743-3126	f
101	606-346-2127	f
102	870-743-4122	f
103	847-758-0123	f
104	870-741-6412	f
105	870-782-0044	f
106	870-365-0363	f
107	501-945-1202	f
108	501-945-0506	f
109	870-436-3877	f
110	870-743-1897	f
111	336-855-3583	f
112	870-715-5204	f
113	870-741-5412	f
114	870-741-8023	f
115	870-741-9818	f
116	501-623-5662	f
117	870-994-7505	f
118	972-542-5379	f
119	870-741-9223	f
120	417-334-3841	f
121	870-436-7404	f
122	800-326-3233	f
123	813-978-8626	f
124	866-550-0225	f
125	870-438-5782	f
126	479-253-9313	f
127	417-334-2353	f
128	870-426-2099	f
129	870-426-2267	f
130	870-934-8906	f
131	870-536-2917	f
132	800-722-0703	f
133	501-268-8140	f
134	501-362-2329	f
135	479-968-9251	f
136	870-773-0516	f
137	479-783-6321	f
138	816-246-0442	f
139	816-228-4129	f
140	479-824-3474	f
141	870-741-9609	f
142	866-690-9004	f
143	870-743-4711	f
144	870-365-5812	f
145	870-741-0505	f
146	870-280-2138	f
147	614-754-8148	f
148	479-253-2007	f
149	864-859-8414	f
150	870-741-7040	f
151	870-704-8151	f
\.


--
-- Data for Name: people; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.people (id, first_name, last_name, is_verified, contact_id) FROM stdin;
1	first_name	last_name	f	316
2	Aaron	Smith	f	317
3	Afton	Campbell	f	318
4	AJ	Hudson	f	319
5	Alan	Beery	f	320
6	Andrew	Guynes	f	321
7	Angie	Mitchell	f	322
8	Anthony	Irwin	f	323
9	Antone	Luneau	f	324
10	Art	Rogers	f	325
11	Barry	Kielian	f	326
12	Bear	Brockelman	f	327
13	Ben		f	328
14	Benny	Gustavasson	f	329
15	Bernie	McCabe	f	330
16	Betty		f	331
17	Beverly	Ingram	f	332
18	Bill	Hudson	f	333
19	Bill	Nichols	f	334
20	Bill	Parker	f	335
21	Bill	Robertson	f	336
22	Billy	Lawrence	f	337
23	Bo	Phillips	f	338
24	Bob	Bogen	f	339
25	Bob	Swafford	f	340
26	Bobby	Gross	f	341
27	Bobby	Poutek	f	342
28	Boyd	Falconer	f	343
29	Brad	Parsley	f	344
30	Brandon	Foster	f	345
31	Brandon	Harris	f	346
32	Bray	Claud	f	347
33	Brian	Dirst	f	348
34	Brian	Felland	f	349
35	Brian	Kramer	f	350
36	Brian	Neptune	f	351
37	Brian	Warner	f	352
38	Brion	Simmons	f	353
39	Bruce	Eddings	f	354
40	Bruce	Foster	f	355
41	Bruce	Trogdon	f	356
42	Buel	Bearden	f	357
43	Butch	May	f	358
44	Calvin	Laughlin	f	359
45	Cameron	Ashley	f	360
46	Carl	Hurst	f	361
47	Carroll	Anderson	f	362
48	Celia	Warren	f	363
49	Charles	Apple	f	364
50	Charles	Creamer	f	365
51	Charles	Hamilton	f	366
52	Chris		f	367
53	Chris	Baugh	f	368
54	Chuck	Bennett	f	369
55	Chuck	Jack	f	370
56	Chuck	Wofford	f	371
57	Cindy	Taylor	f	372
58	Clay	Powell	f	373
59	Cliff	Collin	f	374
60	Clyde	Phillips	f	375
61	Clyde	Still	f	376
62	Cody	Austin	f	377
63	Cody	Leach	f	378
64	Cole	Klineline	f	379
65	Connie	Kelley	f	380
66	Corey/Larry/Grace		f	381
67	Craig/Cathy		f	382
68	Curtis	Melton	f	383
69	Custer	Feather	f	384
70	Dale	Johnston	f	385
71	Dale	Scott	f	386
72	Dan	Hostetler	f	387
73	Dan	Wilkinson	f	388
74	Daniel	Benton	f	389
75	Daniel	Foster	f	390
76	Daniel	Henderson	f	391
77	Daniel	Jones	f	392
78	Danny		f	393
79	Danny	Guynn	f	394
80	Danny	Merritt	f	395
81	Danny	Youngblood	f	396
82	Darrel	Halsted	f	397
83	Daryl	King	f	398
84	Dave	LeMar	f	399
85	David	Cardoza	f	400
86	David	Casey	f	401
87	David	Dooley	f	402
88	David	Evans	f	403
89	David	Ingram	f	404
90	David	Mecke	f	405
91	David	Olson	f	406
92	David	Roland	f	407
93	David	Wallis	f	408
94	David	Wilkinson	f	409
95	Dean	Wilkinson	f	410
96	Debbie	Payton	f	411
97	Delbert	Chappell	f	412
98	Delbert	Headings	f	413
99	Delbert	Jones	f	414
100	Denny	Smith	f	415
101	Derek	Carlson	f	416
102	Derick	Guidall	f	417
103	Dessa	Emerson	f	418
104	Don	Berry	f	419
105	Don	Davis	f	420
106	Don	Hamilton	f	421
107	Don	McMillin	f	422
108	Don	Sanders	f	423
109	Don	Spillwell	f	424
110	Don	Wray	f	425
111	Donald	Hartman	f	426
112	Donald	Hodges	f	427
113	Donald	Wilbert	f	428
114	Donnie		f	429
115	Donnie	Campbell	f	430
116	Doug	Hammond	f	431
117	Doug	Ogburn	f	432
118	Doyle	Wheeler	f	433
119	Dwayne	Richardson	f	434
120	E.G.	Martin	f	435
121	Earl	Phillips	f	436
122	Earl	Raney	f	437
123	Ed	Brewer	f	438
124	Ed	McElroy	f	439
125	Ed	Mooney	f	440
126	Eddie	Adams	f	441
127	Eddie	Getman	f	442
128	Elson	Mast	f	443
129	Eric	Britter	f	444
130	Erich	Spoonhour	f	445
131	Eugene	Coffman	f	446
132	Farrel	Raney	f	447
133	Ford	Clifford	f	448
134	Frank	Dickinson	f	449
135	Frank	Hale	f	450
136	Frank	Pfeifer	f	451
137	Frank	Turner	f	452
138	Fred	Farmer	f	453
139	Garry	Carlton	f	454
140	Gary	Atwell	f	455
141	Gary	Edwards	f	456
142	Gary	Hammond	f	457
143	Gary	Harlin	f	458
144	Gator	Horton	f	459
145	Gene	Rowbotham	f	460
146	Gene	Taylor	f	461
147	Geneva	Deaton	f	462
148	George	Photives	f	463
149	Glen		f	464
150	Glen	Lane	f	465
151	Glen	Smith	f	466
152	Glenn	Smith	f	467
153	Grant	Smith	f	468
154	Greg	Boren	f	469
155	Greg	Farmer	f	470
156	Guy	Nichols	f	471
157	Hal	Hudgins	f	472
158	Hank	Hartman	f	473
159	Harold	Bennett	f	474
160	Herman	Deaton	f	475
161	J.L.	Freeman	f	476
162	Jack	Goff	f	477
163	James	Brantley	f	478
164	James	Estes	f	479
165	James	Fowler	f	480
166	James	Horn	f	481
167	James	Hudson	f	482
168	James	Kelley	f	483
169	James	Manns	f	484
170	James	Melton	f	485
171	James	Minge	f	486
172	James	Norton	f	487
173	James	Richardson	f	488
174	Jamie	Blackshert	f	489
175	Jamie	Phillips	f	490
176	Jason	Adams	f	491
177	Jason	Bryant	f	492
178	Jason	Dubwig	f	493
179	Jason	Still	f	494
180	Jeff		f	495
181	Jeff	Breckenridge	f	496
182	Jeff	Brooke	f	497
183	Jeff	Buck	f	498
184	Jeff	Dewitt	f	499
185	Jeff	Hearn	f	500
186	Jeff	Hudson	f	501
187	Jeff	Humphrey	f	502
188	Jeff	Laur	f	503
189	Jeffrey	Ricketts	f	504
190	Jennifer	Henson	f	505
191	Jeremy/Abigail	Bowser	f	506
192	Jerry	Johnson	f	507
193	Jerry	Parsley	f	508
194	Jerry	Taylor	f	509
195	Jesse	Morrell	f	510
196	Jessie	Raver	f	511
197	Jim	Best	f	512
198	Jim	Chrietzberg	f	513
199	Jim	Ferrari	f	514
200	Jim	Hodge	f	515
201	Jim	Leask	f	516
202	Jim	Rushing	f	517
203	Jimmy	Smith	f	518
204	Joel	Ratchford	f	519
205	Joey	Singleton	f	520
206	John	Atkinson	f	521
207	John	Berry	f	522
208	John	Bosland	f	523
209	John	Busland	f	524
210	John	Dunn	f	525
211	John	Hardin	f	526
212	John	Jenacaro	f	527
213	John	Kurz	f	528
214	John	Payne	f	529
215	Johnathan	Franklin	f	530
216	Johnny	Beauchamp	f	531
217	Johnny	Burleson	f	532
218	Johnny	Phillips	f	533
219	Johnny	Wyatt	f	534
220	Jon	Thompson	f	535
221	Josh	O'Neal	f	536
222	Journey	Powell	f	537
223	Juanita	Gilbert	f	538
224	Kathleen	Breedlove	f	539
225	Kathy	Peach	f	540
226	Katy	Parker	f	541
227	Kayla	Buck	f	542
228	Kayla	Tanner	f	543
229	Keith	Honeycutt	f	544
230	Keith	Pace	f	545
231	Kelly	Shipman	f	546
232	Ken	Gilbert	f	547
233	Ken	Parks	f	548
234	Ken	Ply	f	549
235	Kenneth	Taylor	f	550
236	Kennth	Clark	f	551
237	Kenny	Halsted	f	552
238	Kenny	Morisak	f	553
239	Kenny	Snow	f	554
240	Kenny	Underdown	f	555
241	Kerry	Kindall	f	556
242	Kevin	Rogers	f	557
243	Kevin	Schubert	f	558
244	Kimberly		f	559
245	Kirk	Powell	f	560
246	Kris	Farmer	f	561
247	Kristina	Clanton	f	562
248	Kurtis	Buck	f	563
249	Kurtis	Lowe	f	564
250	Kyle	Howe	f	565
251	LaDel	Falconer	f	566
252	Ladonna	Foster	f	567
253	Laguanna		f	568
254	Larry		f	569
255	Larry	Davis	f	570
256	Larry	Johns	f	571
257	Larry	Phillips	f	572
258	Larry	Pombo	f	573
259	Lawrence	Drewry	f	574
260	Lee	Johns	f	575
261	LeRoy	Brewer	f	576
262	Leland	Neptune	f	577
263	Leroy	Eickmann	f	578
264	Lester	Davidson	f	579
265	Linda	Perme	f	580
266	Lisa	Mallett	f	581
267	Lloyd	Monday	f	582
268	Lonie		f	583
269	Lonnie	Castleman	f	584
270	Loyd	Mahoney	f	585
271	Mabel	Little	f	586
272	Macy	Koehn	f	587
273	Mark	Akers	f	588
274	Mark	Bailey	f	589
275	Mark	Howard	f	590
276	Mark	Rawer	f	591
277	Mark	Richardson	f	592
278	Marty	Hammond	f	593
279	Matt		f	594
280	Matt	Massengale	f	595
281	Matt	Mills	f	596
282	Matt	Snow	f	597
283	Matthew	Greene	f	598
284	McKinley	Shatwell	f	599
285	Melissa	Shamlin	f	600
286	Melvin	Griffin	f	601
287	Michael	Irwin	f	602
288	Michael	Smith	f	603
289	Michael	Valentine	f	604
290	Mickey	Horn	f	605
291	Mike	Case	f	606
292	Mike	Chamberlain	f	607
293	Mike	Jones	f	608
294	Mike	McFarland	f	609
295	Mike	Miller	f	610
296	Mike	Noland	f	611
297	Mike	Pitts	f	612
298	Mike	Ragland	f	613
299	Mike	Smith	f	614
300	Mike	Terbrock	f	615
301	Mike	Wohlgmuth	f	616
302	Missy	Keeter	f	617
303	Nathaniel	Hamilton	f	618
304	Neal	Gibson	f	619
305	Norman	Brooks	f	620
306	Norman	Massengale	f	621
307	Pat	Nichols	f	622
308	Patricia	Turney	f	623
309	Paul	Helton	f	624
310	Paul	Darracq	f	625
311	Ralphie	Kelley	f	626
312	Randall	Dickinson	f	627
313	Randy	Merritt	f	628
314	Randy	Roberts	f	629
315	Randy	Savage	f	630
316	Randy	Smith	f	631
317	Reggie	King	f	632
318	Regina	Worth	f	633
319	Rex	Bolin	f	634
320	Rex	Knapp	f	635
321	Richard	Alonzo	f	636
322	Richard	Evans	f	637
323	Richard	Hostetler	f	638
324	Rick	Bolte	f	639
325	Rick	Curtis	f	640
326	Rick	DeJager	f	641
327	Rick	Jay	f	642
328	Rick	Turner	f	643
329	Rick	Wilburn	f	644
330	Rick	Wyatt	f	645
331	Ricky	Brisco	f	646
332	Rob	Dodson	f	647
333	Rob	Slape	f	648
334	Robert	Hefley	f	649
335	Robert	Hudson	f	650
336	Robert	Lefever	f	651
337	Robert	Martin	f	652
338	Robert	Woods	f	653
339	Rocky	Valentin	f	654
340	Rod	Dressi	f	655
341	Rod	Swanson	f	656
342	Rodger	Robinson	f	657
343	Rodney		f	658
344	Rodney	Daniels	f	659
345	Roger	Clayborn	f	660
346	Roger	Eddings	f	661
347	Roger	Turner	f	662
348	Roman	Berry	f	663
349	Ron	Maness	f	664
350	Ron	Williams	f	665
351	Ronnie	Smith	f	666
352	Ronnie	Ramsey	f	667
353	Ross		f	668
354	Roy	Hibbard	f	669
355	Russel	Kish	f	670
356	Russel	Murray	f	671
357	Russell	Virst	f	672
358	Sadie		f	673
359	Sara	Younes	f	674
360	Scott	Boaz	f	675
361	Scott	FitzGerald	f	676
362	Scott	Matlock	f	677
363	Scott	Peterson	f	678
364	Scott	Wilkinson	f	679
365	Scott	Worley	f	680
366	Shane		f	681
367	Shane	Gilliam	f	682
368	Shawn		f	683
369	Sherry	Maples	f	684
370	Stephen	Fitzpatrick	f	685
371	Steve	Berry	f	686
372	Steve	Harrington	f	687
373	Steve	Ingram	f	688
374	Steve	Jackson	f	689
375	Steve	Miller	f	690
376	Steve	Morgan	f	691
377	Steve	Pleuger	f	692
378	Steve	Roberts	f	693
379	Steve	Ross	f	694
380	Steve	Thomas	f	695
381	Steve	Tkachuk	f	696
382	Steve	Villines	f	697
383	Steven	Kleffman	f	698
384	Steven	Peach	f	699
385	Susie	Thompson	f	700
386	T.J.	Hunter	f	701
387	Ted	Jordan	f	702
388	Terry	Leal	f	703
389	Terry	Patton	f	704
390	Terry	Woods	f	705
391	Thomas	Hudson	f	706
392	Tiffany	Worth	f	707
393	Tim		f	708
394	Tim	Emerson	f	709
395	Tim	Fredenberg	f	710
396	Tim	Graves	f	711
397	Tim	Irwin	f	712
398	Tim	Morrell	f	713
399	Tim	Saul	f	714
400	Timothy	Dale	f	715
401	Todd	Ford	f	716
402	Todd	Hawkins	f	717
403	Todd	Hunter	f	718
404	Tom	Flemming	f	719
405	Tom	Moore	f	720
406	Tom	Powell	f	721
407	Tom	Riggins	f	722
408	Tom	Riley	f	723
409	Tom	Thompson	f	724
410	Tommy	Johnson	f	725
411	Tony	Davenport	f	726
412	Tony	Hudson	f	727
413	Tony	Rogers	f	728
414	Tony	William	f	729
415	Troy		f	730
416	Van	Younes	f	731
417	Vern	Richardson	f	732
418	Vernon	Flippo	f	733
419	Vicilly	Neptune	f	734
420	Vickey		f	735
421	Victor	Sanchez	f	736
422	Warin	West	f	737
423	Warren	Campbell	f	738
424	Wayne	Mancinelli	f	739
425	Wes	Meyers	f	740
426	William	Carter	f	741
427	William	Drewry	f	742
428	William	Turner	f	743
429	William	Whitescarver	f	744
430	Zack	Kuenzle	f	745
\.


--
-- Data for Name: people_companies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.people_companies (person_id, company_id, is_verified) FROM stdin;
\.


--
-- Data for Name: phone_numbers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.phone_numbers (id, phone_number, is_verified) FROM stdin;
1	870-743-3609	f
2	870-743-6607	f
3	870-743-4343	f
4	870-741-8471	f
5	870-741-8376	f
6	870-743-9155	f
7	217-480-7236	f
8	248-280-0210	f
9	270-898-3365	f
10	281-224-4396	f
11	314-434-1200	f
12	314-851-7496	f
13	314-949-935?	f
14	316-755-2361	f
15	317-644-5061	f
16	336-855-3471	f
17	401-945-8990	f
18	404-788-4630	f
19	417-230-2384	f
20	417-256-8997	f
21	417-270-0855	f
22	417-271-3299	f
23	417-271-3801	f
24	417-294-4681	f
25	417-334-1675	f
26	417-334-6219	f
27	417-334-7992	f
28	417-334-8622	f
29	417-335-5046	f
30	417-335-5659	f
31	417-337-0090	f
32	417-337-1169	f
33	417-337-3331	f
34	417-339-6941	f
35	417-365-3920	f
36	417-399-2944	f
37	417-527-2654	f
38	417-544-1620	f
39	417-581-2463	f
40	417-581-2625	f
41	417-593-1144	f
42	417-593-7451	f
43	417-631-1515	f
44	417-646-8369	f
45	417-669-0379	f
46	417-773-8965	f
47	417-778-7241	f
48	417-779-4822	f
49	417-779-5654	f
50	417-785-4325	f
51	417-858-2626	f
52	417-865-5561	f
53	417-866-8686	f
54	417-881-1588	f
55	417-882-4487	f
56	417-882-6112	f
57	417-294-4549	f
58	405-224-1200	f
59	479-229-2010	f
60	479-236-4017	f
61	479-236-5815	f
62	479-238-4235	f
63	479-244-5012	f
64	479-253-0000	f
65	479-253-4421	f
66	479-253-6567	f
67	479-253-7139	f
68	479-253-9182	f
69	479-253-9774	f
70	479-256-0573	f
71	479-292-8862	f
72	479-381-0599	f
73	479-422-1471	f
74	479-685-5664	f
75	479-750-1080	f
76	479-750-5205	f
77	479-751-1102	f
78	479-751-5020	f
79	479-783-8666	f
80	479-789-5111	f
81	479-824-3282	f
82	479-871-0007	f
83	479-951-8733	f
84	479-957-3648	f
85	501-244-3559	f
86	501-253-0702	f
87	501-257-4722	f
88	501-268-3025	f
89	501-276-4774	f
90	501-278-6234	f
91	501-293-4569	f
92	501-354-1503	f
93	501-365-2304	f
94	501-371-1438	f
95	501-372-3965	f
96	501-376-1337	f
97	501-409-3500	f
98	501-569-2505	f
99	501-623-3310	f
100	501-745-2698	f
101	501-745-4048	f
102	501-759-2885	f
103	501-783-3385	f
104	501-872-8100	f
105	501-945-3442	f
106	501-967-4399	f
107	501-968-1556	f
108	503-590-5485	f
109	504-455-1309	f
110	561-352-7196	f
111	573-265-7094	f
112	601-357-6001	f
113	601-671-3215	f
114	605-660-4540	f
115	606-346-2121	f
116	614-668-2084	f
117	614-725-6613	f
118	614-754-8147	f
119	618-444-3941	f
120	618-654-2184	f
121	636-221-5943	f
122	661-363-3799	f
123	718-886-7200	f
124	765-299-9033	f
125	765-585-8180	f
126	775-636-2014	f
127	800-221-0270	f
128	800-242-1615	f
129	800-280-7994	f
130	800-282-1299	f
131	800-285-4800	f
132	800-288-9835	f
133	800-325-8075	f
134	800-333-1800	f
135	800-359-5000	f
136	800-368-3749	f
137	800-388-3870	f
138	800-432-9727	f
139	800-433-0655	f
140	800-445-6570	f
141	800-462-4977	f
142	800-479-6661	f
143	800-525-3313	f
144	800-622-4345	f
145	800-632-3500	f
146	800-655-4345	f
147	800-731-3215	f
148	800-735-4000	f
149	800-748-8637	f
150	800-833-4393	f
151	800-835-0050	f
152	800-874-4723	f
153	800-933-7185	f
154	800-999-5099	f
155	800-HRBLOCK	f
156	810-561-5861	f
157	812-482-2000	f
158	813-972-1135 ext 361	f
159	813-972-1135 ext. 260	f
160	816-246-0969	f
161	816-668-5622	f
162	817-640-1282	f
163	845-346-0615	f
164	847-758-1234	f
165	850-423-2843	f
166	864-859-0153	f
167	866-248-8961	f
168	866-964-9663	f
169	870-204-0089	f
170	870-204-2858	f
171	870-204-3256	f
172	870-204-3418	f
173	870-204-4454	f
174	870-204-6497	f
175	870-221-1604	f
176	870-253-5748	f
177	870-280-9678	f
178	870-321-0832	f
179	870-350-0784	f
180	870-365-0069	f
181	870-365-0182	f
182	870-365-0433	f
183	870-365-0434	f
184	870-365-0492	f
185	870-365-0507	f
186	870-365-0684	f
187	870-365-0714	f
188	870-365-0743	f
189	870-365-0754	f
190	870-365-2650	f
191	870-365-3523	f
192	870-365-3667	f
193	870-365-3738	f
194	870-365-3955	f
195	870-365-5457	f
196	870-365-5458	f
197	870-365-5514	f
198	870-365-5536	f
199	870-365-5537	f
200	870-365-5651	f
201	870-365-5741	f
202	870-365-5845	f
203	870-365-5871	f
204	870-365-5926	f
205	870-365-5933	f
206	870-365-6043	f
207	870-365-6103	f
208	870-365-6198	f
209	870-365-6205	f
210	870-365-6468	f
211	870-365-6584	f
212	870-365-6659	f
213	870-365-6776	f
214	870-365-6850	f
215	870-365-7120	f
216	870-365-7133	f
217	870-365-7390	f
218	870-365-7443	f
219	870-365-7444	f
220	870-365-7755	f
221	870-365-7846	f
222	870-365-8052	f
223	870-365-8074	f
224	870-365-8124	f
225	870-365-8369	f
226	870-365-8400	f
227	870-365-8900	f
228	870-365-9213	f
229	870-365-9280	f
230	870-365-9470	f
231	870-365-9563	f
232	870-365-9616	f
233	870-365-9797	f
234	870-375-0312	f
235	870-391-1520	f
236	870-391-1705	f
237	870-391-1773	f
238	870-391-1775	f
239	870-391-1950	f
240	870-391-1953	f
241	870-391-3679	f
242	870-391-3849	f
243	870-391-4425	f
244	870-391-5910	f
245	870-391-5915	f
246	870-391-6053	f
247	870-391-6059	f
248	870-391-6176	f
249	870-391-6569	f
250	870-391-6696	f
251	870-391-8055	f
252	870-391-8250	f
253	870-391-8400	f
254	870-391-9137	f
255	870-391-9422	f
256	870-391-9425	f
257	870-391-9488	f
258	870-391-9924	f
259	870-391-9977	f
260	870-404-4080	f
261	870-404-5282	f
262	870-404-5403	f
263	870-404-6561	f
264	870-404-6779	f
265	870-404-7317	f
266	870-404-7644	f
267	870-404-9278	f
268	870-404-9525	f
269	870-405-2014	f
270	870-405-2359	f
271	870-405-2402	f
272	870-405-2795	f
273	870-405-7755	f
274	870-414-1393	f
275	870-414-1485	f
276	870-414-1487	f
277	870-416-0773	f
278	870-416-0984	f
279	870-416-2094	f
280	870-416-2620	f
281	870-416-4019	f
282	870-416-4118	f
283	870-416-4151	f
284	870-416-4526	f
285	870-416-7069	f
286	870-416-8268	f
287	870-416-8559	f
288	870-416-8619	f
289	870-416-9218	f
290	870-416-9579	f
291	870-420-3281	f
292	870-420-3425	f
293	870-420-3433	f
294	870-420-3486	f
295	870-420-3538	f
296	870-421-2620	f
297	870-421-5556	f
298	870-422-2252	f
299	870-423-2053	f
300	870-423-2076	f
301	870-423-2096	f
302	870-423-2756	f
303	870-423-3239	f
304	870-423-3914	f
305	870-423-6325	f
306	870-423-6358	f
307	870-423-6671	f
308	870-423-7048	f
309	870-423-7444	f
310	870-423-7633	f
311	870-423-7663	f
312	870-423-7808	f
313	870-423-7876	f
314	870-423-8123	f
315	870-423-8374	f
316	870-423-8405	f
317	870-423-8436	f
318	870-423-8437	f
319	870-423-8555	f
320	870-423-8565	f
321	870-423-8767	f
322	870-424-2044	f
323	870-424-3335	f
324	870-425-3101	f
325	870-425-4407	f
326	870-425-4696	f
327	870-425-5118	f
328	870-425-6323	f
329	870-425-6936	f
330	870-425-6959	f
331	870-425-9093	f
332	870-426-2099	f
333	870-426-2267	f
334	870-426-3330	f
335	870-426-3676	f
336	870-426-3935	f
337	870-426-4237	f
338	870-426-4990	f
339	870-426-5235	f
340	870-426-5329	f
341	870-426-5461	f
342	870-426-5880	f
343	870-427-2253	f
344	870-427-2304	f
345	870-427-2373	f
346	870-427-2624	f
347	870-427-3039	f
348	870-427-3223	f
349	870-427-3261	f
350	870-427-3344	f
351	870-427-3579	f
352	870-427-3732	f
353	870-427-5469	f
354	870-427-5581	f
355	870-427-5638	f
356	870-427-5655	f
357	870-427-6687	f
358	870-427-7527	f
359	870-428-5209	f
360	870-428-5456	f
361	870-429-5217	f
362	870-429-5259	f
363	870-429-5346	f
364	870-429-5365	f
365	870-429-5432	f
366	870-429-5489	f
367	870-429-5500	f
368	870-429-5525	f
369	870-429-5664	f
370	870-429-5791	f
371	870-429-5813	f
372	870-429-5862	f
373	870-429-5980	f
374	870-429-6118	f
375	870-429-6123	f
376	870-429-6145	f
377	870-429-6152	f
378	870-429-6355	f
379	870-429-6436	f
380	870-429-6698	f
381	870-429-6767	f
382	870-429-8122	f
383	870-429-8694	f
384	870-429-8782	f
385	870-4296231	f
386	870-431-5556	f
387	870-431-8353	f
388	870-434-5250	f
389	870-434-5584	f
390	870-434-5599	f
391	870-435-8000	f
392	870-436-1553	f
393	870-436-2258	f
394	870-436-3450	f
395	870-436-4714	f
396	870-436-4717	f
397	870-436-5314	f
398	870-436-5554	f
399	870-436-5703	f
400	870-436-5888	f
401	870-437-2723	f
402	870-437-2886	f
403	870-437-5651	f
404	870-438-4749	f
405	870-438-5994	f
406	870-438-6068	f
407	870-438-6316	f
408	870-438-6510	f
409	870-438-6561	f
410	870-438-6588	f
411	870-439-2153	f
412	870-439-2212	f
413	870-439-2508	f
414	870-439-2666	f
415	870-439-2670	f
416	870-445-4646	f
417	870-446-2202	f
418	870-446-2663	f
419	870-446-2690	f
420	870-446-2858	f
421	870-446-2865	f
422	870-446-5943	f
423	870-446-7642	f
424	870-448-2675	f
425	870-448-3139	f
426	870-448-3312	f
427	870-448-3435	f
428	870-448-5160	f
429	870-448-5180	f
430	870-448-5332	f
431	870-448-6039	f
432	870-448-7280	f
433	870-448-7950	f
434	870-449-2246	f
435	870-449-4255	f
436	870-449-4533	f
437	870-449-4579	f
438	870-449-5337	f
439	870-449-5340	f
440	870-449-6636	f
441	870-449-6779	f
442	870-449-6913	f
443	870-449-6926	f
444	870-453-2912	f
445	870-467-5169	f
446	870-480-2116	f
447	870-480-2905	f
448	870-480-3272	f
449	870-480-3520	f
450	870-480-6293	f
451	870-480-7152	f
452	870-480-7171	f
453	870-488-2294	f
454	870-499-3270	f
455	870-504-0959	f
456	870-504-1186	f
457	870-504-1368	f
458	870-504-1809	f
459	870-504-5078	f
460	870-508-4200	f
461	870-536-5871	f
462	870-553-2022	f
463	870-553-2607	f
464	870-577-0099	f
465	870-577-0199	f
466	870-577-0468	f
467	870-577-1060	f
468	870-577-1091	f
469	870-577-1352	f
470	870-577-1374	f
471	870-577-1468	f
472	870-577-1483	f
473	870-577-1739	f
474	870-577-1791	f
475	870-577-2005	f
476	870-577-2121	f
477	870-577-2215	f
478	870-577-2218	f
479	870-577-2387	f
480	870-577-2541	f
481	870-577-2642	f
482	870-577-2893	f
483	870-577-3124	f
484	870-577-3413	f
485	870-577-3538	f
486	870-577-3778	f
487	870-577-4002	f
488	870-577-4027	f
489	870-577-4184	f
490	870-577-4656	f
491	870-577-4720	f
492	870-577-4818	f
493	870-577-4931	f
494	870-577-5040	f
495	870-577-5129	f
496	870-577-5789	f
497	870-577-5829	f
498	870-577-5867	f
499	870-577-7069	f
500	870-577-7191	f
501	870-577-7351	f
502	870-580-0585	f
503	870-654-2208	f
504	870-654-3791	f
505	870-654-4058	f
506	870-654-6157	f
507	870-656-0697	f
508	870-656-2341	f
509	870-656-2342	f
510	870-656-6446	f
511	870-656-9006	f
512	870-688-0063	f
513	870-688-0076	f
514	870-688-0404	f
515	870-688-1230	f
516	870-688-1436	f
517	870-688-2035	f
518	870-688-2367	f
519	870-688-2788	f
520	870-688-3271	f
521	870-688-3733	f
522	870-688-3757	f
523	870-688-3952	f
524	870-688-4046	f
525	870-688-4106	f
526	870-688-4125	f
527	870-688-5024	f
528	870-688-6105	f
529	870-688-6230	f
530	870-688-6715	f
531	870-688-8398	f
532	870-688-8449	f
533	870-688-9192	f
534	870-688-9501	f
535	870-688-9774	f
536	870-704-8062	f
537	870-704-9074	f
538	870-704-9097	f
539	870-704-9290	f
540	870-704-9899	f
541	870-715-0382	f
542	870-715-0477	f
543	870-715-0508	f
544	870-715-0653	f
545	870-715-0683	f
546	870-715-0787	f
547	870-715-0803	f
548	870-715-2357	f
549	870-715-5078	f
550	870-715-5089	f
551	870-715-5204	f
552	870-715-5211	f
553	870-715-5225	f
554	870-715-5328	f
555	870-715-5559	f
556	870-715-5644	f
557	870-715-5806	f
558	870-715-5906	f
559	870-715-5972	f
560	870-715-7168	f
561	870-715-7392	f
562	870-715-7488	f
563	870-715-7541	f
564	870-715-7694	f
565	870-715-7789	f
566	870-715-7887	f
567	870-715-7904	f
568	870-715-8262	f
569	870-715-8306	f
570	870-715-8655	f
571	870-715-8712	f
572	870-715-9159	f
573	870-715-9301	f
574	870-715-9313	f
575	870-715-9319	f
576	870-715-9412	f
577	870-716-8104	f
578	870-741-0140	f
579	870-741-0245	f
580	870-741-0258	f
581	870-741-0266	f
582	870-741-0350	f
583	870-741-0361	f
584	870-741-0535	f
585	870-741-1000	f
586	870-741-1032	f
587	870-741-1115	f
588	870-741-1171	f
589	870-741-1354	f
590	870-741-1400	f
591	870-741-1402	f
592	870-741-1730	f
593	870-741-1775	f
594	870-741-2040	f
595	870-741-2100	f
596	870-741-2165	f
597	870-741-2167	f
598	870-741-2305	f
599	870-741-2333	f
600	870-741-2714	f
601	870-741-2716	f
602	870-741-2743	f
603	870-741-2784	f
604	870-741-2815	f
605	870-741-3001	f
606	870-741-3178	f
607	870-741-3323	f
608	870-741-3463	f
609	870-741-3493	f
610	870-741-3500	f
611	870-741-3532	f
612	870-741-3670	f
613	870-741-3749	f
614	870-741-3777	f
615	870-741-3925	f
616	870-741-4035	f
617	870-741-4266	f
618	870-741-4490	f
619	870-741-4664	f
620	870-741-4757	f
621	870-741-4797	f
622	870-741-4951	f
623	870-741-5077	f
624	870-741-5318	f
625	870-741-5423	f
626	870-741-5522	f
627	870-741-5620	f
628	870-741-5715	f
629	870-741-5800	f
630	870-741-5810	f
631	870-741-6000	f
632	870-741-6118	f
633	870-741-6131	f
634	870-741-6430	f
635	870-741-6630	f
636	870-741-6651	f
637	870-741-6712	f
638	870-741-6739	f
639	870-741-6767	f
640	870-741-6816	f
641	870-741-7125	f
642	870-741-7152	f
643	870-741-7206	f
644	870-741-7229	f
645	870-741-7302	f
646	870-741-7387	f
647	870-741-7572	f
648	870-741-7641	f
649	870-741-7798	f
650	870-741-7848	f
651	870-741-8038	f
652	870-741-8133	f
653	870-741-8326	f
654	870-741-8408	f
655	870-741-8465	f
656	870-741-8514	f
657	870-741-8622	f
658	870-741-8646	f
659	870-741-8693	f
660	870-741-8802	f
661	870-741-8853	f
662	870-741-9046	f
663	870-741-9084	f
664	870-741-9095	f
665	870-741-9113	f
666	870-741-9198	f
667	870-741-9220	f
668	870-741-9380	f
669	870-741-9401	f
670	870-741-9461	f
671	870-741-9636	f
672	870-741-9637	f
673	870-743-0872	f
674	870-743-1157	f
675	870-743-1200	f
676	870-743-1264	f
677	870-743-1284	f
678	870-743-1355	f
679	870-743-1500	f
680	870-743-1538	f
681	870-743-1556	f
682	870-743-1597	f
683	870-743-1669	f
684	870-743-1696	f
685	870-743-1800	f
686	870-743-2137	f
687	870-743-2200	f
688	870-743-2208	f
689	870-743-2308	f
690	870-743-2323	f
691	870-743-2397	f
692	870-743-2700	f
693	870-743-3017	f
694	870-743-3090	f
695	870-743-3113	f
696	870-743-3180	f
697	870-743-3219	f
698	870-743-3638	f
699	870-743-3960	f
700	870-743-4051	f
701	870-743-4118	f
702	870-743-4400	f
703	870-743-4909	f
704	870-743-4976	f
705	870-743-5006	f
706	870-743-5117	f
707	870-743-5131	f
708	870-743-5154	f
709	870-743-5155	f
710	870-743-5400	f
711	870-743-5757	f
712	870-743-5814	f
713	870-743-6131	f
714	870-743-6686	f
715	870-743-6704	f
716	870-743-6779	f
717	870-743-6800	f
718	870-743-6923	f
719	870-743-7787	f
720	870-743-9006	f
721	870-743-9040	f
722	870-743-9248	f
723	870-743-9366	f
724	870-743-9448	f
725	870-743-9465	f
726	870-745-1601	f
727	870-749-2526	f
728	870-749-2574	f
729	870-749-2717	f
730	870-751-6302	f
731	870-754-1207	f
732	870-754-3742	f
733	870-754-4085	f
734	870-754-7467	f
735	870-754-9346	f
736	870-769-2107	f
737	870-773-6866	f
738	870-782-2190	f
739	870-793-3713	f
740	870-793-7905	f
741	870-861-5636	f
742	870-934-8503	f
743	870-965-1555	f
744	870-967-3632	f
745	870-994-7500	f
746	8770-365-9753	f
747	8770-741-5412	f
748	888-829-5649	f
749	888-872-8108	f
750	903-275-9889	f
751	903-887-3581	f
752	918-486-4137	f
753	918-626-3837	f
754	918-649-5208	f
755	918-847-2244	f
\.


--
-- Data for Name: status; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.status (id, text) FROM stdin;
1	Active
2	Inactive
3	Banned
\.


--
-- Name: addresses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.addresses_id_seq', 451, true);


--
-- Name: companies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.companies_id_seq', 315, true);


--
-- Name: contacts_contact_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.contacts_contact_id_seq', 745, true);


--
-- Name: email_addresses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.email_addresses_id_seq', 1, false);


--
-- Name: fax_numbers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fax_numbers_id_seq', 151, true);


--
-- Name: people_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.people_id_seq', 430, true);


--
-- Name: phone_numbers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.phone_numbers_id_seq', 755, true);


--
-- Name: status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.status_id_seq', 3, true);


--
-- Name: addresses addresses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.addresses
    ADD CONSTRAINT addresses_pkey PRIMARY KEY (id);


--
-- Name: companies companies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.companies
    ADD CONSTRAINT companies_pkey PRIMARY KEY (id);


--
-- Name: contacts contacts_person_id_company_id_unique; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_person_id_company_id_unique UNIQUE (person_id, company_id);


--
-- Name: contacts contacts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_pkey PRIMARY KEY (contact_id);


--
-- Name: email_addresses email_addresses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.email_addresses
    ADD CONSTRAINT email_addresses_pkey PRIMARY KEY (id);


--
-- Name: fax_numbers fax_numbers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fax_numbers
    ADD CONSTRAINT fax_numbers_pkey PRIMARY KEY (id);


--
-- Name: people_companies people_companies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.people_companies
    ADD CONSTRAINT people_companies_pkey PRIMARY KEY (person_id, company_id);


--
-- Name: people people_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.people
    ADD CONSTRAINT people_pkey PRIMARY KEY (id);


--
-- Name: phone_numbers phone_numbers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.phone_numbers
    ADD CONSTRAINT phone_numbers_pkey PRIMARY KEY (id);


--
-- Name: status status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.status
    ADD CONSTRAINT status_pkey PRIMARY KEY (id);


--
-- Name: companies companies_contact_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.companies
    ADD CONSTRAINT companies_contact_id_fkey FOREIGN KEY (contact_id) REFERENCES public.contacts(contact_id);


--
-- Name: contacts contacts_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(id);


--
-- Name: contacts contacts_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.people(id);


--
-- Name: contacts contacts_status_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_status_id_fkey FOREIGN KEY (status_id) REFERENCES public.status(id);


--
-- Name: people_companies people_companies_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.people_companies
    ADD CONSTRAINT people_companies_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(id) ON DELETE CASCADE;


--
-- Name: people_companies people_companies_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.people_companies
    ADD CONSTRAINT people_companies_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.people(id) ON DELETE CASCADE;


--
-- Name: people people_contact_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.people
    ADD CONSTRAINT people_contact_id_fkey FOREIGN KEY (contact_id) REFERENCES public.contacts(contact_id);


--
-- PostgreSQL database dump complete
--

