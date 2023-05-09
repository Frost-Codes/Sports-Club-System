CHOICES = (
    ('FB', 'Football'),
    ('BB', 'Basketball'),
    ('VB', 'Volleyball'),
    ('HY', 'Hockey'),
    ('BM', 'Badminton'),
    ('TT', 'Table Tennis'),
    ('CS', 'Chess'),
    ('NB', 'Netball'),
    ('HB', 'Handball'),
    ('RB', 'Rugby'),
    ('AL', 'All'),
)

GENDER_CHOICES = (
    ('Male', 'Male'), ('Female', 'Female')
)

SPECIAL_NEEDS = (('Yes', 'Yes'), ('No', 'No'))

COUNTIES = (
    ('Baringo', 'BARINGO'), ('Bomet', 'BOMET'), ('Bungoma', 'BUNGOMA'), ('Busia', 'BUSIA'),
    ('Elgeyo Marakwet', 'ELGEYO MARAKWET'), ('Embu', 'EMBU'), ('Garissa', 'GARISSA'),
    ('Homa Bay', 'HOMA BAY'), ('Isiolo', 'ISIOLO'), ('Kajiado', 'KAJIADO'), ('Kakamega', 'KAKAMEGA'),
    ('Kericho', 'KERICHO'), ('Kiambu', 'KIAMBU'), ('Kilifi', 'KILIFI'), ('Kirinyaga', 'KIRINYAGA'),
    ('Kisii', 'KISII'), ('Kisumu', 'KISUMU'), ('Kitui', 'KITUI'), ('Kwale', 'KWALE'),
    ('Laikipia', 'LAIKIPIA'), ('Lamu', 'LAMU'), ('Machakos', 'MACHAKOS'), ('Makueni', 'MAKUENI'),
    ('Mandera', 'MANDERA'), ('Meru', 'MERU'), ('Migori', 'MIGORI'), ('Marsabit', 'MARSABIT'),
    ('Mombasa', 'MOMBASA'), ('Muranga', "MURANG'A"), ('Nairobi', 'NAIROBI'), ('Nakuru', 'NAKURU'),
    ('Nandi', 'NANDI'), ('Narok', 'NAROK'), ('Nyandarua', 'NYANDARUA'), ('Nyamira', 'NYAMIRA'),
    ('Nyeri', 'NYERI'), ('Samburu', 'SAMBURU'), ('Siaya', 'SIAYA'), ('Taita Taveta', 'TAITA TAVETA'),
    ('Tana River', 'TANA RIVER'), ('Tharaka Nithi', 'THARAKA NITHI'), ('Trans Nzoia', 'TRANS NZOIA'),
    ('Turkana', 'TURKANA'), ('Uasin Gishu', 'UASIN GISHU'), ('Vihiga', 'VIHIGA'), ('Wajir', 'WAJIR'),
    ('West Pokot', 'WEST POKOT')

)

TOWNS = (
    ('Kabarnet', 'KABARNET'), ('Eldama Ravine', 'ELDAMA RAVINE'), ('Marigat', 'MARIGAT'),
    ('Sacho', 'SACHO'), ('Maji Mazuri', 'MAJI MAZURI'), ('Bomet', 'BOMET'), ('Ndanai', 'NDANAI'),
    ('Chemaner', 'CHEMANER'), ('Ndamichoni', 'NDAMICHONI'), ('Kamugeno', 'KAMUGENO'),
    ('Kimilili', 'KIMILILI'), ('Webuye', 'WEBUYE'), ('Malakisi', 'MALAKISI'), ('Sirisia', 'SIRISIA'),
    ('Bumula', 'BUMULA'), ('Busia', 'BUSIA'), ('Malaba', 'MALABA'), ('Matayos', 'MATAYOS'),
    ('Port Bunyala', 'PORT BUNYALA'), ('Nambale', 'NAMBALE'), ('Elgeyo Marakwet', 'ELGEYO MARAKWET'),
    ('Kaptarakwa', 'KAPTARAKWA'), ('Chepkorio', 'CHEPKORIO'), ('Iten', 'ITEN'), ('Chesoi', 'CHESOI'),
    ('Embu', 'EMBU'), ('Runyenjes', 'RUNYENJES'), ('Siakago', 'SIAKAGO'), ('Manyatta', 'MANYATTA'),
    ('Kiritiri', 'KIRITIRI'), ('Garissa', 'GARISSA'), ('Homa Bay', 'HOMA BAY'), ('Oyugis', 'OYUGIS'),
    ('Mbita', 'MBITA'), ('Kendu Bay', 'KENDU BAY'), ('Isiolo', 'ISIOLO'), ('Merti', 'MERTI'),
    ('Modogoshe', 'MODOGOSHE'), ('Muddo Gashi', 'MUDDO GASHI'), ('Ngong', 'NGONG'),
    ('Kitengela', 'KITENGELA'), ('Ongata Rongai', 'ONGATA RONGAI'), ('Kiserian', 'KISERIAN'),
    ('Kajiado', 'KAJIADO'), ('Loitokitok', 'LOITOKITOK'), ('Namanga', 'NAMANGA'),
    ('Kakamega', 'KAKAMEGA'), ('Mumias', 'MUMIAS'), ('Lurambi', 'LURAMBI'), ('Shinyalu', 'SHINYALU'),
    ('Malava', 'MALAVA'), ('Kericho', 'KERICHO'), ('Liten', 'LITEN'), ('Londiani', 'LONDIANI'),
    ('Chemasit', 'CHEMASIT'), ('Kapsaos', 'KAPSAOS'), ('Kiambu', 'KIAMBU'), ('Juja', 'JUJA'),
    ('Thika', 'THIKA'), ('Limuru', 'LIMURU'), ('Ruiru', 'RUIRU'), ('Gatundu', 'GATUNDU'),
    ('Kabete', 'KABETE'), ('Kijabe', 'KIJABE'), ('Kikuyu', 'KIKUYU'), ('Uthiru', 'UTHIRU'),
    ('Ruaka', 'RUAKA'), ('Kilifi', 'KILIFI'), ('Malindi', 'MALINDI'), ('Watamu', 'WATAMU'),
    ('Mariakani', 'MARIAKANI'), ('Mtwapa', 'MTWAPA'), ('Mwea', 'MWEA'), ('Kerugoya', 'KERUGOYA'),
    ('Kutus', 'KUTUS'), ('Sagana', 'SAGANA'), ('Gacharu', 'GACHARU'), ('Kagumo', 'KAGUMO'),
    ('Kisii', 'KISII'), ('Ogembo', 'OGEMBO'), ('Suneka', 'SUNEKA'), ('Kanyenya', 'KANYENYA'),
    ('Masimba', 'MASIMBA'), ('Keumbu', 'KEUMBU'), ('Kisumu', 'KISUMU'), ('Ahero', 'AHERO'),
    ('Muhoroni', 'MUHORONI'), ('Maseno', 'MASENO'), ('Kombewa', 'KOMBEWA'), ('Kitui', 'KITUI'),
    ('Mwingi', 'MWINGI'), ('Mutomo', 'MUTOMO'), ('Kiyuso', 'KIYUSO'), ('Kawelu', 'KAWELU'),
    ('Bazo', 'BAZO'),
    ('Dololo', 'DOLOLO'), ('Nanyuki', 'NANYUKI'), ('Nyahururu', 'NYAHURURU'), ('Rumuruti', 'RUMURUTI'),
    ('Lamu', 'LAMU'), ('Mpeketoni', 'MPEKETONI'), ('Faza', 'FAZA'), ('Machakos', 'MACHAKOS'),
    ('Kangundo', 'KANGUNDO'), ('Athi River', 'ATHI RIVER'), ('Tala', 'TALA'), ('Mlolongo', 'MLOLONGO'),
    ('Konza', 'KONZA'), ('Wote', 'WOTE'), ('Mtito Andei', 'MTITO ANDEI'), ('Makindu', 'MAKINDU'),
    ('Kibwezi', 'KIBWEZI'), ('Mbooni', 'MBOONI'), ('Mandera', 'MANDERA'), ('Meru', 'MERU'),
    ('Maua', 'MAUA'), ('Nkubu', 'NKUBU'), ('Mikinduri', 'MIKINDURI'),
    ('Kampi Ya Chumvi', 'KAMPI YA CHUMVI'), ('Migori', 'MIGORI'), ('Rongo', 'RONGO'),
    ('Marsabit', 'MARASABIT'), ('Sololo', 'SOLOLO'), ('Mombasa', 'MOMBASA'), ('Bamburi', 'BAMBURI'),
    ('Likoni', 'LIKONI'), ('Muranga', "MURANG'A"), ('Makuyu', 'MAKUYU'), ('Kangema', 'KANGEMA'),
    ('Kasarani', 'KASARANI'), ('Githurahi', 'GITHURAHI'), ('Kahawa', 'KAHAWA'),
    ('Muthaiga', 'MUTHAIGA'), ('Kileleshwa', 'KILELESHWA'), ("Lang'ata", "LANG'ATA"),
    ('Dagoretti', 'DAGORETTI'), ('Nakuru', 'NAKURU'), ('Naivasha', 'NAIVASHA'), ('Gilgil', 'GILGIL'),
    ('Njoro', 'NJORO'), ('Molo', 'MOLO'), ('Kapsabet', 'KAPSABET'), ('Nandi Hills', 'NANDI HILLS'),
    ('Kabiyet', 'KABIYET'), ('Narok', 'NAROK'), ('Kilgoris', 'KILGORIS'), ('Maji Moto', 'MAJI MOTO'),
    ('Nyandarua', 'NYANDARUA'), ('Njabini', 'NJABINI'), ('Nyeri', 'NYERI'), ('Kiganjo', 'KIGANJO'),
    ('Othaya', 'OTHAYA'), ('Bunyunya', 'BUNYUNYA'), ('Samburu', 'SAMBURU'), ('Maralal', 'MARALAL'),
    ('Archers Post', 'ARCHERS POST'), ('Siaya', 'SIAYA'), ('Bondo', 'BONDO'), ('Ugunja', 'UGUNJA'),
    ('Taveta', 'TAVETA'), ('Voi', 'VOI'), ('Wundanyi', 'WUNDANYI'), ('Mbale', 'MBALE'),
    ('Mikinduni', 'MIKINDUNI'), ('Chuka', 'CHUKA'), ('Chogoria', 'CHOGORIA'), ('Kanwa', 'KANWA'),
    ('Kitale', 'KITALE'), ('Kiminini', 'KIMININI'), ('Endebess', 'ENDEBESS'), ('Lodwar', 'LODWAR'),
    ('Kalok', 'KALOK'), ('Eldoret', 'ELDORET'), ('Turbo', 'TURBO'), ('Kesses', 'KESSES'),
    ('Kapsaret', 'KAPSARET'), ('Luanda', 'LUANDA'), ('Chavakali', 'CHAVAKALI'), ('Wajir', 'WAJIR'),
    ('Kapenguria', 'KAPENGURIA'), ('Chepareria', 'CHEPARERIA')
)

SUB_COUNTIES = (('Kasa', 'Kasarani'),
                ('Westi', 'Westlands'),
                ('Makadara', 'Makadara'),
                ('Starehe', 'Starehe'),
                ('Matahare', 'Matahare'),
                ('Roysambu', 'Roysambu'),
                ('Ruaraka', 'Ruaraka'),
                ('Langata', 'Langata'),
                ('Emba Central', 'Embakasi Central'),
                ('Emba North', 'Embakasi North'),
                ('Emba South', 'Embakasi South'),
                ('Meru South', 'Meru South'),
                ('Maara', 'Maara')
                )

GAMES = (
    ('Football', 'Football'),
    ('Basketball', 'Basketball'),
    ('Volleyball', 'Volleyball'),
    ('Hockey', 'Hockey'),
    ('Badminton', 'Badminton'),
    ('Table Tennis', 'Table Tennis'),
    ('Chess', 'Chess'),
    ('Netball', 'Netball'),
    ('Handball', 'Handball'),
    ('Rugby', 'Rugby'),
    ('Swimming', 'Swimming'),
    ('Pool', 'Pool'),

)

NEXT_OF_KIN = (
    ('Father', 'Father'),
    ('Mother', 'Mother'),
    ('Relative', 'Relative'),
    ('Other', 'Other')
)


STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('Out for Delivery', 'Out for Delivery'),
    ('Delivered', 'Delivered'),
    ('Canceled', 'Canceled'),

)

API_PUBLISHABLE_KEY = 'ISPubKey_test_e74e4771-6f9c-45f9-bbcb-fe6dd9b6dc4a'

API_TOKEN = 'ISSecretKey_test_1ebb5743-01f2-46b3-92f8-3b242d715db2'

