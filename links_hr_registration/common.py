import random
import string

zip_codes_croatia = \
    {"ALJMAŠ": "31205",
     "ANTUNOVAC": "31216",
     "ARŽANO": "21246",
     "BABINA GREDA": "32276",
     "BABINO POLJE": "20225",
     "BADERNA": "52445",
     "BADLJEVINA": "34552",
     "BAKAR": "51222",
     "BAKARAC": "51261",
     "BALE": "52211",
     "BANOVA JARUGA": "44321",
     "BANOVCI": "32247",
     "BAPSKA": "32235",
     "BARANJSKO PETROVO SELO": "31322",
     "BARBAN": "52207",
     "BARILOVIĆ": "47252",
     "BAŠKA": "51523",
     "BAŠKA VODA": "21320",
     "BATINA": "31306",
     "BEBRINA": "35254",
     "BEDEKOVČINA": "49221",
     "BEDENICA": "10381",
     "BEDNJA": "42253",
     "BEKTEŽ": "34343",
     "BELEJ": "51555",
     "BELI": "51559",
     "BELI MANASTIR": "31300",
     "BELICA": "40319",
     "BELIŠĆE": "31551",
     "BELOVAR": "10363",
     "BENKOVAC": "23420",
     "BEREK": "43232",
     "BERETINEC": "42201",
     "BESTOVJE": "10437",
     "BETINA": "22244",
     "BIBINJE": "23205",
     "BIJELO BRDO": "31204",
     "BILJE": "31327",
     "BIOGRAD NA MORU": "23210",
     "BIZOVAC": "31222",
     "BJELOVAR": "43000",
     "BLACE": "20357",
     "BLATO": "20271",
     "BLATO NA CETINI": "21254",
     "BLINJSKI KUT": "44211",
     "BLIZNA DONJA": "21228",
     "BOBOTA": "32225",
     "BOL": "21420",
     "BOLJUN": "52434",
     "BOLMAN": "31323",
     "BOROVO": "32227",
     "BOSILJEVO": "47251",
     "BOŠNJACI": "32275",
     "BOŽAVA": "23286",
     "BRAČEVCI": "31423",
     "BRANJIN VRH": "31301",
     "BRBINJ": "23285",
     "BREGANA": "10432",
     "BRELA": "21322",
     "BRESTOVAC": "34322",
     "BREZNICA NAŠIČKA": "31225",
     "BREZNIČKI HUM": "42225",
     "BREZOVICA": "10257",
     "BRIBIR": "51253",
     "BRINJE": "53260",
     "BROD MORAVICE": "51312",
     "BROD NA KUPI": "51301",
     "BRODSKI STUPNIK": "35253",
     "BROĐANCI": "31223",
     "BRŠADIN": "32222",
     "BRSEČ": "51418",
     "BRTONIGLA": "52474",
     "BRUŠANE": "53206",
     "BRUSJE": "21454",
     "BUČJE": "34553",
     "BUDIMCI": "31432",
     "BUDINŠĆINA": "49284",
     "BUJE": "52460",
     "BUKOVLJE": "35209",
     "BULINAC": "43273",
     "BUŠEVEC": "10417",
     "BUZET": "52420",
     "ČABAR": "51306",
     "CABUNA": "33412",
     "ČAČINCI": "33514",
     "ČAĐAVICA": "33523",
     "ČAĐAVICA": "33523",
     "ČAGLIN": "34350",
     "ČAKOVCI": "32238",
     "ČAKOVEC": "40000",
     "ČARA": "20273",
     "ČAVLE": "51219",
     "CAVTAT": "20210",
     "ČAZMA": "43240",
     "ČEMINAC": "31325",
     "ČEPIN": "31431",
     "CERNA": "32272",
     "CERNIK": "35404",
     "CEROVAC VUKMANIĆKI": "47241",
     "CEROVLJE": "52402",
     "ČERVAR PORAT": "52449",
     "CESTICA": "42208",
     "CETINGRAD": "47222",
     "ČILIPI": "20213",
     "CISTA PROVO": "21256",
     "CISTA VELIKA": "21244",
     "ČISTA VELIKA": "22214",
     "CRES": "51557",
     "CRIKVENICA": "51260",
     "CRIVAC": "21229",
     "CRNAC": "33507",
     "CRNI LUG": "51317",
     "ČRNKOVCI": "31553",
     "ĆUNSKI": "51564",
     "DALJ": "31226",
     "DARDA": "31326",
     "DARUVAR": "43500",
     "DAVOR": "35425",
     "DEKANOVEC": "40318",
     "DELNICE": "51300",
     "DESINIĆ": "49216",
     "DEŽANOVAC": "43506",
     "DICMO": "21232",
     "DIVUŠA": "44435",
     "DOBRINJ": "51514",
     "DOLI": "20231",
     "DONJA BISTRA": "10298",
     "DONJA DUBRAVA": "40328",
     "DONJA LOMNICA": "10412",
     "DONJA MOTIČINA": "31513",
     "DONJA PUŠĆA": "10294",
     "DONJA STUBICA": "49240",
     "DONJA VIŠNJICA": "42255",
     "DONJA VOĆA": "42245",
     "DONJA ZELINA": "10382",
     "DONJE OGORJE": "21206",
     "DONJE PAZARIŠTE": "53213",
     "DONJI ANDRIJEVCI": "35214",
     "DONJI DOLAC": "21205",
     "DONJI DRAGONOŽEC": "10253",
     "DONJI KRALJEVEC": "40320",
     "DONJI KUKURUZARI": "44431",
     "DONJI LAPAC": "53250",
     "DONJI MARTIJANEC": "42232",
     "DONJI MIHOLJAC": "31540",
     "DONJI MUĆ": "21203",
     "DONJI PROLOŽAC": "21264",
     "DONJI VIDOVEC": "40327",
     "DRAGA BAŠĆANSKA": "51522",
     "DRAGALIĆ": "35428",
     "DRAGANIĆ": "47201",
     "DRAGLJANE": "21275",
     "DRAMALJ": "51265",
     "DRAŠKOVEC": "40325",
     "DRAŠNICE": "21328",
     "DRAŽ": "31305",
     "DRAŽICE": "51218",
     "DRENJE": "31418",
     "DRENOVCI": "32257",
     "DREŽNICA": "47313",
     "DREŽNIK GRAD": "47246",
     "DRINOVCI": "22324",
     "DRIVENIK": "51242",
     "DRNIŠ": "22320",
     "DRNJE": "48322",
     "DRVENIK": "21333",
     "DRVENIK VELIKI": "21225",
     "DUBOŠEVICA": "31304",
     "DUBRANEC": "10418",
     "DUBRAVA": "10342",
     "DUBRAVICA": "10293",
     "DUBRAVKA": "20216",
     "DUBROVNIK": "20000",
     "DUGA RESA": "47250",
     "DUGI RAT": "21315",
     "DUGO SELO": "10370",
     "DUGOPOLJE": "21204",
     "DVOR": "44440",
     "ĐAKOVO": "31400",
     "ĐELEKOVEC": "48316",
     "ĐELETOVCI": "32244",
     "ĐULOVAC": "43532",
     "ĐURĐENOVAC": "31511",
     "ĐURĐEVAC": "48350",
     "ĐURIĆI": "32263",
     "ĐURMANEC": "49225",
     "ERDUT": "31206",
     "ERNESTINOVO": "31215",
     "FARKAŠEVAC": "10344",
     "FAŽANA": "52212",
     "FERDINANDOVAC": "48356",
     "FERIČANCI": "31512",
     "FUNTANA": "52452",
     "FUŽINE": "51322",
     "GABOŠ": "32212",
     "GALIŽANA": "52216",
     "GARČIN": "35212",
     "GAREŠNICA": "43280",
     "GAT": "31554",
     "GATA": "21253",
     "GDINJ": "21467",
     "GENERALSKI STOL": "47262",
     "GEROVO": "51304",
     "GLINA": "44400",
     "GOLA": "48331",
     "GOLUBIĆ": "22301",
     "GOMIRJE": "51327",
     "GORICA SVETOJANSKA": "10453",
     "GORIČAN": "40324",
     "GORJANI": "31422",
     "GORNJA RIJEKA": "48268",
     "GORNJA STUBICA": "49245",
     "GORNJA VRBA": "35207",
     "GORNJE BAZJE": "33407",
     "GORNJE JESENJE": "49233",
     "GORNJE ZAGORJE": "47307",
     "GORNJI BOGIĆEVCI": "35429",
     "GORNJI STUPNIK": "10255",
     "GOSPIĆ": "53000",
     "GOVEĐARI": "20226",
     "GRAB": "21242",
     "GRABERJE IVANIČKO": "10313",
     "GRABOVAC": "21271",
     "GRAČAC": "23440",
     "GRAČIŠĆE": "52403",
     "GRADAC": "21330",
     "GRADEC": "10345",
     "GRADINA": "33411",
     "GRADIŠTE": "32273",
     "GRIŽANE": "51244",
     "GROHOTE": "21430",
     "GROŽNJAN": "52429",
     "GRUBIŠNO POLJE": "43290",
     "GRUDA": "20215",
     "GUDOVAC": "43251",
     "GUNDINCI": "35222",
     "GUNJA": "32260",
     "GUŠĆE": "44203",
     "GVOZD": "44410",
     "HERCEGOVAC": "43284",
     "HLEBINE": "48323",
     "HRAŠĆINA-TRGOVIŠĆE": "49283",
     "HRELJIN": "51226",
     "HRVACE": "21233",
     "HRVATSKA DUBICA": "44450",
     "HRVATSKA KOSTAJNICA": "44430",
     "HRVATSKI LESKOVAC": "10251",
     "HUM NA SUTLI": "49231",
     "HVAR": "21450",
     "IČIĆI": "51414",
     "IGRANE": "21329",
     "ILAČA": "32248",
     "ILOK": "32236",
     "ILOVIK": "51552",
     "IMOTSKI": "21260",
     "IST": "23293",
     "IVANEC": "42240",
     "IVANIĆ-GRAD": "10310",
     "IVANJA REKA": "10373",
     "IVANKOVO": "32281",
     "IVANSKA": "43231",
     "JABLANAC": "53287",
     "JABUKOVAC": "44204",
     "JADRANOVO": "51264",
     "JAGODNJAK": "31324",
     "JAKOVLJE": "10297",
     "JAKŠIĆ": "34308",
     "JALŽABET": "42203",
     "JANJINA": "20246",
     "JARMINA": "32280",
     "JASENAK": "47314",
     "JASENICE": "23243",
     "JASENOVAC": "44324",
     "JASTREBARSKO": "10450",
     "JELSA": "21465",
     "JESENICE": "21314",
     "JEZERA": "22242",
     "JEZERANE": "53262",
     "JOSIPDOL": "47303",
     "JOSIPOVAC": "31221",
     "JURDANI": "51213",
     "KALI": "23272",
     "KALINOVAC": "48361",
     "KALJE": "10456",
     "KALNIK": "48269",
     "KAMANJE": "47282",
     "KAMENMOST": "21262",
     "KANFANAR": "52352",
     "KANIŠKA IVA": "43283",
     "KAPELA": "43203",
     "KAPRIJE": "22235",
     "KAPTOL": "34334",
     "KARANAC": "31315",
     "KARIN": "23452",
     "KARLOBAG": "53288",
     "KARLOVAC": "47000",
     "KAROJBA": "52423",
     "KAŠINA": "10362",
     "KAŠT": "47284",
     "KASTAV": "51215",
     "KAŠTEL GOMILICA": "21213",
     "KAŠTEL KAMBELOVAC": "21214",
     "KAŠTEL LUKŠIĆ": "21215",
     "KAŠTEL ŠTAFILIĆ": "21217",
     "KAŠTEL STARI": "21216",
     "KAŠTEL SUĆURAC": "21212",
     "KAŠTELIR": "52464",
     "KIJEVO": "22310",
     "KISTANJE": "22305",
     "KLANA": "51217",
     "KLANAC": "53212",
     "KLANJEC": "49290",
     "KLEK": "20356",
     "KLENOVICA": "51252",
     "KLENOVNIK": "42244",
     "KLIS": "21231",
     "KLOŠTAR IVANIĆ": "10312",
     "KLOŠTAR PODRAVSKI": "48362",
     "KLOŠTAR VOJAKOVAČKI": "48264",
     "KNEŽEVI VINOGRADI": "31309",
     "KNEŽEVO": "31302",
     "KNIN": "22300",
     "KOLAN": "23251",
     "KOLOČEP": "20221",
     "KOMIN": "10383",
     "KOMIN": "20344",
     "KOMIŽA": "21485",
     "KOMLETINCI": "32253",
     "KONČANICA": "43505",
     "KONJŠČINA": "49282",
     "KOPRIVNICA": "48000",
     "KOPRIVNIČKI IVANEC": "48314",
     "KORČULA": "20260",
     "KORENICA": "53230",
     "KORNIĆ": "51517",
     "KOROMAČNO": "52222",
     "KOSINJ": "53203",
     "KOŠKA": "31224",
     "KOSTANJE": "21207",
     "KOSTANJEVAC": "10455",
     "KOSTRENA": "51221",
     "KOTORIBA": "40329",
     "KRALJEVEC NA SUTLI": "49294",
     "KRALJEVICA": "51262",
     "KRAPINA": "49000",
     "KRAPINSKE TOPLICE": "49217",
     "KRAPJE": "44325",
     "KRAŠIĆ": "10454",
     "KRASICA": "51224",
     "KRASNO": "53274",
     "KRATEČKO": "44213",
     "KRAVARSKO": "10413",
     "KRIVI PUT": "53271",
     "KRIVODOL": "21263",
     "KRIŽ": "10314",
     "KRIŽEVCI": "48260",
     "KRIŽIŠĆE": "51241",
     "KRIŽPOLJE": "53261",
     "KRK": "51500",
     "KRNICA": "52208",
     "KRNJAK": "47242",
     "KRŠAN": "52232",
     "KUČIĆE": "21208",
     "KUĆIŠTE": "20267",
     "KUKLJICA": "23271",
     "KUKULJANOVO": "51227",
     "KULA NORINSKA": "20341",
     "KUMROVEC": "49295",
     "KUNA": "20243",
     "KUNOVEC": "48311",
     "KUPJAK": "51313",
     "KUPLJENOVO": "10295",
     "KUTINA": "44320",
     "KUTJEVO": "34340",
     "KUŽELJ": "51302",
     "KUZMICA": "34311",
     "LABIN": "52220",
     "LANIŠĆE": "52422",
     "LASINJA": "47206",
     "LASLOVO": "31214",
     "LASTOVO": "20290",
     "LEĆEVICA": "21202",
     "LEDENICE": "51251",
     "LEGRAD": "48317",
     "LEKENIK": "44272",
     "LEPAJCI": "49224",
     "LEPOGLAVA": "42250",
     "LEVANJSKA VAROŠ": "31416",
     "LIČ": "51323",
     "LIČKI OSIK": "53201",
     "LIČKO LEŠĆE": "53224",
     "LIČKO PETROVO SELO": "53233",
     "LIJEVI DUBROVČAK": "10316",
     "LIPIK": "34551",
     "LIPOVAC": "32246",
     "LIPOVLJANI": "44322",
     "LIVADE": "52427",
     "LIŽNJAN": "52204",
     "LJUBEŠĆICA": "42222",
     "LOBOR": "49253",
     "LOKVA ROGOZNICA": "21317",
     "LOKVE": "51316",
     "LONJICA": "10341",
     "LOPAR": "51281",
     "LOPATINEC": "40311",
     "LOPUD": "20222",
     "LOVAS": "32237",
     "LOVINAC": "53244",
     "LOVIŠTE": "20269",
     "LOVRAN": "51415",
     "LOVREĆ": "21257",
     "LOŽIŠĆA": "21404",
     "LOZOVAC": "22221",
     "LUČKO": "10250",
     "LUDBREG": "42230",
     "LUG": "31328",
     "LUKA": "10296",
     "LUKAČ": "33406",
     "LUKORAN": "23274",
     "LUKOVDOL": "51328",
     "LUKOVO ŠUGARJE": "53289",
     "LUMBARDA": "20263",
     "LUN": "53294",
     "LUPOGLAV": "52426",
     "LUŽANI": "35257",
     "MAČE": "49251",
     "MACINEC": "40306",
     "MAGADENOVAC": "31542",
     "MAHIČNO": "47286",
     "MAKARSKA": "21300",
     "MALA SUBOTICA": "40321",
     "MALI BUKOVEC": "42231",
     "MALI ERJAVEC": "47281",
     "MALI LOŠINJ": "51550",
     "MALINSKA": "51511",
     "MARANOVIĆI": "20224",
     "MARČANA": "52206",
     "MARIJA BISTRICA": "49246",
     "MARIJA GORICA": "10299",
     "MARIJANCI": "31555",
     "MARINA": "21222",
     "MARKUŠICA": "32213",
     "MARTINŠĆICA": "51556",
     "MARTINSKA VES": "44201",
     "MARUŠEVEC": "42243",
     "MATULJI": "51211",
     "MEDULIN": "52203",
     "METKOVIĆ": "20350",
     "MIHOLJAČKI POREČ": "31543",
     "MIHOVLJAN": "49252",
     "MIKLEUŠ": "33517",
     "MILNA": "21405",
     "MIMICE": "21318",
     "MLINI": "20207",
     "MLINIŠTE": "20353",
     "MOKOŠICA": "20236",
     "MOLAT": "23292",
     "MOLVE": "48327",
     "MORAVICE": "51325",
     "MORNJAN": "52462",
     "MOŠĆENICA": "44253",
     "MOŠĆENIČKA DRAGA": "51417",
     "MOTOVUN": "52424",
     "MRAVINCE": "21209",
     "MRKOPALJ": "51315",
     "MURSKO SREDIŠĆE": "40315",
     "MURTER": "22243",
     "NARTA": "43247",
     "NAŠICE": "31500",
     "NEDELIŠĆE": "40305",
     "NEDEŠĆINA": "52231",
     "NEGOSLAVCI": "32239",
     "NEORIĆ": "21247",
     "NEREZINE": "51554",
     "NEREŽIŠĆA": "21423",
     "NETRETIĆ": "47271",
     "NEVIĐANE": "23264",
     "NIJEMCI": "32245",
     "NIN": "23232",
     "NJIVICE": "51512",
     "NOVA BUKOVICA": "33518",
     "NOVA GRADIŠKA": "35400",
     "NOVA KAPELA": "10343",
     "NOVA KAPELA": "35410",
     "NOVA RAČA": "43272",
     "NOVA SELA": "20278",
     "NOVA VAS": "52446",
     "NOVALJA": "53291",
     "NOVI MAROF": "42220",
     "NOVI VINODOLSKI": "51250",
     "NOVIGRAD": "23312",
     "NOVIGRAD": "52466",
     "NOVIGRAD PODRAVSKI": "48325",
     "NOVO ČIČE": "10415",
     "NOVO VIRJE": "48355",
     "NOVOSELEC": "10315",
     "NOVSKA": "44330",
     "NUŠTAR": "32221",
     "OBOROVO": "10372",
     "OBROVAC": "23450",
     "OBROVAC SINJSKI": "21241",
     "OGULIN": "47300",
     "OKLAJ": "22303",
     "OKRUG GORNJI": "21223",
     "OKUČANI": "35430",
     "OLIB": "23296",
     "OMIŠ": "21310",
     "OMIŠALJ": "51513",
     "OPATIJA": "51410",
     "OPATOVAC": "32233",
     "OPRISAVCI": "35213",
     "OPRTALJ": "52428",
     "OPUZEN": "20355",
     "ORAHOVICA": "33515",
     "ORAŠAC": "20234",
     "OREBIĆ": "20250",
     "OREHOVEC": "48267",
     "OREHOVICA": "40322",
     "ORIOVAC": "35250",
     "ORLE": "10411",
     "OROLIK": "32243",
     "OROSLAVJE": "49243",
     "ORUBICA": "35424",
     "OSIJEK": "31000",
     "OSKORUŠNO": "20242",
     "OŠTARIJE": "47302",
     "OSTROVO": "32211",
     "OTOČAC": "53220",
     "OTOK": "21238",
     "OTOK": "32252",
     "OTRIĆ SEOCI": "20342",
     "OZALJ": "47280",
     "PAG": "23250",
     "PAKOŠTANE": "23211",
     "PAKRAC": "34550",
     "PAŠMAN": "23262",
     "PAZIN": "52000",
     "PERKOVIĆ": "22205",
     "PERUŠIĆ": "53202",
     "PETERANEC": "48321",
     "PETLOVAC": "31321",
     "PETRČANE": "23231",
     "PETRIJANEC": "42206",
     "PETRIJEVCI": "31208",
     "PETRINJA": "44250",
     "PETROVCI": "32229",
     "PETROVSKO": "49234",
     "PIĆAN": "52332",
     "PIROVAC": "22213",
     "PISAROVINA": "10451",
     "PIŠKOREVCI": "31417",
     "PITOMAČA": "33405",
     "PIVNICA SLAVONSKA": "33533",
     "PLAŠKI": "47304",
     "PLEŠCE": "51303",
     "PLETERNICA": "34310",
     "PLITVIČKA JEZERA": "53231",
     "PLOČE": "20340",
     "PLOČICE": "20218",
     "PLOMIN": "52234",
     "PODACA": "21335",
     "PODCRKAVLJE": "35201",
     "PODGAJCI PODRAVSKI": "31552",
     "PODGORA": "21327",
     "PODGORAČ": "31433",
     "PODLAPAČA": "53236",
     "PODPIĆAN": "52333",
     "PODRAVSKA MOSLAVINA": "31530",
     "PODRAVSKE SESVETE": "48363",
     "PODŠPILJE": "21483",
     "PODSTRANA": "21312",
     "PODTUREN": "40317",
     "PODVINJE": "35107",
     "POKUPSKO": "10414",
     "POLAČA": "23423",
     "POLIČNIK": "23241",
     "POLJANA": "34543",
     "POPOVAC": "31303",
     "POPOVAČA": "44317",
     "POREČ": "52440",
     "POSAVSKI BREGI": "10311",
     "POSAVSKI PODGAJCI": "32258",
     "POSEDARJE": "23242",
     "POSTIRA": "21410",
     "POTOMJE": "20244",
     "POVLJA": "21413",
     "POVLJANA": "23249",
     "POŽEGA": "34000",
     "PRAPUTNJAK": "51225",
     "PRAŽNICA": "21424",
     "PREDAVAC": "43211",
     "PREGRADA": "49218",
     "PREKO": "23273",
     "PRELOG": "40323",
     "PREMUDA": "23294",
     "PRESEKA": "10346",
     "PREZID": "51307",
     "PRGOMELJE": "43252",
     "PRGOMET": "21201",
     "PRIDRAGA": "23226",
     "PRIDVORJE": "20217",
     "PRIGORJE BRDOVEČKO": "10291",
     "PRIMORSKI DOLAC": "21227",
     "PRIMOŠTEN": "22202",
     "PRIVLAKA": "23233",
     "PRIVLAKA": "32251",
     "PRNJAVOR": "35216",
     "PROMAJNA": "21323",
     "PRVIĆ LUKA": "22233",
     "PRVIĆ ŠEPURINE": "22234",
     "PUČIŠĆA": "21412",
     "PULA": "52100",
     "PUNAT": "51521",
     "PUNITOVCI": "31424",
     "PUPNAT": "20274",
     "PUTNIKOVIĆ": "20248",
     "RAB": "51280",
     "RABAC": "52221",
     "RAČINOVCI": "32262",
     "RAČIŠĆE": "20264",
     "RADATOVIĆI": "47285",
     "RADOBOJ": "49232",
     "RADOVAN": "42242",
     "RAJEVO SELO": "32261",
     "RAJIĆ": "44323",
     "RAKOV POTOK": "10436",
     "RAKOVEC": "10347",
     "RAKOVICA": "47245",
     "RAŠA": "52223",
     "RASINJA": "48312",
     "RATKOVICA": "34315",
     "RAVA": "23283",
     "RAVEN": "48265",
     "RAVNA GORA": "51314",
     "RAŽANAC": "23248",
     "REČICA": "47203",
     "REŠETARI": "35403",
     "RETKOVCI": "32282",
     "RIBNIK": "47272",
     "RIČICE": "21267",
     "RIJEKA": "51000",
     "ROČ": "52425",
     "ROGOTIN": "20343",
     "ROGOZNICA": "22203",
     "ROKOVCI": "32271",
     "ROVINJ": "52210",
     "ROVIŠĆE": "43212",
     "RUNOVIĆI": "21261",
     "RUŠČICA": "35208",
     "RUŽIĆ": "22322",
     "SABORSKO": "47306",
     "SALI": "23281",
     "SAMOBOR": "10430",
     "ŠANDROVAC": "43227",
     "ŠAPJANE": "51214",
     "ŠARENGRAD": "32234",
     "SATNICA ĐAKOVAČKA": "31421",
     "SAVUDRIJA": "52475",
     "SELA": "44273",
     "SELCA": "21425",
     "SELCE": "51266",
     "SELCI ĐAKOVAČKI": "31415",
     "SELNICA": "40314",
     "SEMELJCI": "31402",
     "SENJ": "53270",
     "ŠENKOVEC": "10292",
     "ŠESTANOVAC": "21250",
     "SESTRUNJ": "23291",
     "SESVETE-KRALJEVEC": "10361",
     "SEVERIN": "43274",
     "SEVERIN NA KUPI": "51329",
     "ŠIBENIK": "22000",
     "ŠIBENIK-ZABLAĆE": "22030",
     "SIBINJ": "35252",
     "SIKIREVCI": "35224",
     "SILBA": "23295",
     "ŠILO": "51515",
     "SINJ": "21230",
     "ŠIPANJSKA LUKA": "20223",
     "SIRAČ": "43541",
     "ŠIROKE": "22204",
     "SISAK": "44000",
     "SISAK-CAPRAG": "44010",
     "ŠIŠLJAVIĆ": "47204",
     "SIVERIĆ": "22321",
     "ŠKABRNJA": "23223",
     "SKAKAVAC": "47212",
     "SKRAD": "51311",
     "SKRADIN": "22222",
     "ŠKRLJEVO": "51223",
     "SLAKOVCI": "32242",
     "SLANO": "20232",
     "SLATINA": "33520",
     "SLATINE": "21224",
     "SLAVONSKI BROD": "35000",
     "SLAVONSKI KOBAŠ": "35255",
     "SLAVONSKI ŠAMAC": "35220",
     "SLIVNO": "21272",
     "SLUNJ": "47240",
     "SMILJAN": "53211",
     "SMOKVICA": "20272",
     "ŠMRIKA": "51263",
     "SOKOLOVAC": "48306",
     "SOLIN": "21210",
     "SOLJANI": "32255",
     "SOPJE": "33525",
     "SOŠICE": "10457",
     "SOTIN": "32232",
     "ŠPIŠIĆ BUKOVICA": "33404",
     "SPLIT": "21000",
     "SRAČINEC": "42209",
     "SRB": "23445",
     "SRINJINE": "21292",
     "STANKOVCI": "23422",
     "STARA GRADIŠKA": "35435",
     "STARI GRAD": "21460",
     "STARI JANKOVCI": "32241",
     "STARI MIKANOVCI": "32284",
     "STARIGRAD": "23244",
     "STARO PETROVO SELO": "35420",
     "STAŠEVICA": "20345",
     "ŠTEFANJE": "43246",
     "ŠTITAR": "32274",
     "STOBREČ": "21311",
     "STOMORSKA": "21432",
     "STON": "20230",
     "ŠTRIGOVA": "40312",
     "STRIZIVOJNA": "31410",
     "STRMEC SAMOBORSKI": "10434",
     "STROŠINCI": "32256",
     "STUDENCI": "21265",
     "SUĆURAJ": "21469",
     "SUHOPOLJE": "33410",
     "SUKOŠAN": "23206",
     "SUNJA": "44210",
     "SUPETAR": "21400",
     "SUSAK": "51561",
     "ŠUŠNJEVICA": "52233",
     "SUTIVAN": "21403",
     "SUZA": "31308",
     "SVETA MARIJA": "40326",
     "SVETA NEDELJA": "10431",
     "SVETI ĐURĐ": "42233",
     "SVETI FILIP I JAKOV": "23207",
     "SVETI ILIJA": "42214",
     "SVETI IVAN ŽABNO": "48214",
     "SVETI IVAN ZELINA": "10380",
     "SVETI JURAJ": "53284",
     "SVETI KRIŽ ZAČRETJE": "49223",
     "SVETI LOVREČ": "52448",
     "SVETI MARTIN NA MURI": "40313",
     "SVETI MARTIN POD OKIĆEM": "10435",
     "SVETI PETAR U ŠUMI": "52404",
     "SVETVINČENAT": "52342",
     "TAR": "52465",
     "TENJA": "31207",
     "TIJARICA": "21245",
     "TINJAN": "52444",
     "TISNO": "22240",
     "TKON": "23212",
     "TOPOLO": "20205",
     "TOPOLOVAC": "44202",
     "TOPUSKO": "44415",
     "TORDINCI": "32214",
     "TOUNJ": "47264",
     "TOVARNIK": "32249",
     "TRAKOŠĆAN": "42254",
     "TRGET": "52224",
     "TRIBALJ": "51243",
     "TRIBANJ": "23245",
     "TRIBUNJ": "22212",
     "TRILJ": "21240",
     "TRNAVA": "31411",
     "TRNJANI": "35211",
     "TRNOVEC BARTOLOVEČKI": "42202",
     "TRNOVITIČKI POPOVAC": "43233",
     "TROGIR": "21220",
     "TRPANJ": "20240",
     "TRPINJA": "32224",
     "TRŠĆE": "51305",
     "TRSTENIK": "20245",
     "TRSTENO": "20233",
     "TUČEPI": "21325",
     "TUGARE": "21252",
     "TUHELJ": "49215",
     "TURČIN": "42204",
     "UDBINA": "53234",
     "UGLJAN": "23275",
     "UGLJANE": "21243",
     "ULJANIK": "43507",
     "UMAG": "52470",
     "UNEŠIĆ": "22323",
     "UNIJE": "51562",
     "VALPOVO": "31550",
     "VARAŽDIN": "42000",
     "VARAŽDINSKE TOPLICE": "42223",
     "VELA LUKA": "20270",
     "VELE MUNE": "51212",
     "VELI IŽ": "23284",
     "VELI LOŠINJ": "51551",
     "VELI RAT": "23287",
     "VELIKA": "34330",
     "VELIKA GORICA": "10410",
     "VELIKA KOPANICA": "35221",
     "VELIKA LUDINA": "44316",
     "VELIKA MLAKA": "10408",
     "VELIKI BASTAJI": "43531",
     "VELIKI GRĐEVAC": "43270",
     "VELIKI PROLOG": "21277",
     "VELIKI ZDENCI": "43293",
     "VELIKO TRGOVIŠĆE": "49214",
     "VELIKO TROJSTVO": "43226",
     "VELIKO VUKOVJE": "43282",
     "VETOVO": "34335",
     "VID": "20352",
     "VIDOVEC": "42205",
     "VILJEVO": "31531",
     "VINICA": "42207",
     "VINIŠĆE": "21226",
     "VINJERAC": "23247",
     "VINKOVCI": "32100",
     "VIR": "23234",
     "VIRJE": "48326",
     "VIROVITICA": "33000",
     "VIS": "21480",
     "VIŠKOVCI": "31401",
     "VIŠKOVO": "51216",
     "VIŠNJAN": "52463",
     "VIŠNJEVAC": "31220",
     "VIVODINA": "47283",
     "VIŽINADA": "52447",
     "VLADISLAVCI": "31404",
     "VOĆIN": "33522",
     "VODICE": "22211",
     "VODNJAN": "52215",
     "VOĐINCI": "32283",
     "VOJNIĆ": "47220",
     "VOLODER": "44318",
     "VRATNIK": "53273",
     "VRBANJ": "21462",
     "VRBANJA": "32254",
     "VRBJE": "35423",
     "VRBNIK": "51516",
     "VRBOSKA": "21463",
     "VRBOVA": "35414",
     "VRBOVEC": "10340",
     "VRBOVSKO": "51326",
     "VRGORAC": "21276",
     "VRHOVINE": "53223",
     "VRLIKA": "21236",
     "VRPOLJE": "35210",
     "VRSAR": "52450",
     "VRSI": "23235",
     "VUKA": "31403",
     "VUKOVAR": "32000",
     "VUKOVINA": "10419",
     "ZABOK": "49210",
     "ZADAR": "23000",
     "ZADVARJE": "21255",
     "ZAGORSKA SELA": "49296",
     "ZAGREB": "10000",
     "ZAGREB": "10110",
     "ZAGREB-DUBRAVA": "10040",
     "ZAGREB-NOVI ZAGREB": "10020",
     "ZAGREB-SLOBOŠTINA": "10010",
     "ZAGREB-SUSEDGRAD": "10090",
     "ZAGVOZD": "21270",
     "ŽAKANJE": "47276",
     "ZAOSTROG": "21334",
     "ZAPOLJE": "35422",
     "ZAPREŠIĆ": "10290",
     "ZASTRAŽIŠĆE": "21466",
     "ZATON": "22215",
     "ZATON VELIKI": "20235",
     "ŽDALA": "48332",
     "ZDENCI": "33513",
     "ŽDRELAC": "23263",
     "ZELČIN": "31227",
     "ZEMUNIK": "23222",
     "ŽIRJE": "22236",
     "ZLARIN": "22232",
     "ZLATAR": "49250",
     "ZLATAR BISTRICA": "49247",
     "ZLOBIN": "51324",
     "ZMAJEVAC": "31307",
     "ŽMAN": "23282",
     "ZMIJAVCI": "21266",
     "ŽMINJ": "52341",
     "ZRINSKI TOPOLOVAC": "43202",
     "ŽRNOVNICA": "21251",
     "ŽRNOVO": "20275",
     "ZUBOVIĆI": "53296",
     "ŽULJANA": "20247",
     "ŽUPA": "21273",
     "ŽUPANJA": "32270",
     "ZVEČAJ": "47261"}

months = ["siječanj", "veljača", "ožujak", "travanj", "svibanj", "lipanj", "srpanj", "kolovoz", "rujan", "listopad",
          "studeni", "prosinac"]


def choose_zipcode():
    return random.choice(list(zip_codes_croatia.items()))


def random_string():
    return ''.join(
        random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=random.randint(0, 20)))