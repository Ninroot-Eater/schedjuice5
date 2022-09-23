# Generated by Django 4.0.5 on 2022-08-12 08:24

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Campus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        max_length=256,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Field must only contain basic Latin characters, numbers and spaces.",
                                regex="[a-zA-Z0-9 ]",
                            )
                        ],
                    ),
                ),
                ("opening_time", models.TimeField()),
                ("closing_time", models.TimeField()),
                (
                    "house_number",
                    models.CharField(
                        max_length=16,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Field must match this: '[a-zA-Z0-9_\\-\\(\\) ]'",
                                regex="[a-zA-Z0-9_\\-\\(\\) ]",
                            )
                        ],
                    ),
                ),
                (
                    "block_number",
                    models.CharField(
                        max_length=16,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Field must match this: '[a-zA-Z0-9_\\-\\(\\) ]'",
                                regex="[a-zA-Z0-9_\\-\\(\\) ]",
                            )
                        ],
                    ),
                ),
                (
                    "street_name",
                    models.CharField(
                        max_length=32,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Field must only contain basic Latin characters, numbers and spaces.",
                                regex="[a-zA-Z0-9 ]",
                            )
                        ],
                    ),
                ),
                (
                    "township",
                    models.CharField(
                        max_length=32,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Field must only contain basic Latin characters, numbers and spaces.",
                                regex="[a-zA-Z0-9 ]",
                            )
                        ],
                    ),
                ),
                ("city", models.CharField(max_length=64)),
                (
                    "country",
                    models.CharField(
                        choices=[
                            ("AF", "AFGHANISTAN"),
                            ("AL", "ALBANIA"),
                            ("DZ", "ALGERIA"),
                            ("AS", "AMERICAN SAMOA"),
                            ("AD", "ANDORRA"),
                            ("AO", "ANGOLA"),
                            ("AI", "ANGUILLA"),
                            ("AQ", "ANTARCTICA"),
                            ("AG", "ANTIGUA AND BARBUDA"),
                            ("AR", "ARGENTINA"),
                            ("AM", "ARMENIA"),
                            ("AW", "ARUBA"),
                            ("AU", "AUSTRALIA"),
                            ("AT", "AUSTRIA"),
                            ("AZ", "AZERBAIJAN"),
                            ("BS", "BAHAMAS"),
                            ("BH", "BAHRAIN"),
                            ("BD", "BANGLADESH"),
                            ("BB", "BARBADOS"),
                            ("BY", "BELARUS"),
                            ("BE", "BELGIUM"),
                            ("BZ", "BELIZE"),
                            ("BJ", "BENIN"),
                            ("BM", "BERMUDA"),
                            ("BT", "BHUTAN"),
                            ("BO", "BOLIVIA"),
                            ("BA", "BOSNIA AND HERZEGOVINA"),
                            ("BW", "BOTSWANA"),
                            ("BV", "BOUVET ISLAND"),
                            ("BR", "BRAZIL"),
                            ("IO", "BRITISH INDIAN OCEAN TERRITORY"),
                            ("BN", "BRUNEI DARUSSALAM"),
                            ("BG", "BULGARIA"),
                            ("BF", "BURKINA FASO"),
                            ("BI", "BURUNDI"),
                            ("KH", "CAMBODIA"),
                            ("CM", "CAMEROON"),
                            ("CA", "CANADA"),
                            ("CV", "CAPE VERDE"),
                            ("KY", "CAYMAN ISLANDS"),
                            ("CF", "CENTRAL AFRICAN REPUBLIC"),
                            ("TD", "CHAD"),
                            ("CL", "CHILE"),
                            ("CN", "CHINA"),
                            ("CX", "CHRISTMAS ISLAND"),
                            ("CC", "COCOS (KEELING) ISLANDS"),
                            ("CO", "COLOMBIA"),
                            ("KM", "COMOROS"),
                            ("CG", "CONGO"),
                            ("CD", "CONGO, THE DEMOCRATIC REPUBLIC OF"),
                            ("CK", "COOK ISLANDS"),
                            ("CR", "COSTA RICA"),
                            ("CI", "CÃ”TE D'IVOIRE"),
                            ("HR", "CROATIA"),
                            ("CU", "CUBA"),
                            ("CY", "CYPRUS"),
                            ("CZ", "CZECH REPUBLIC"),
                            ("DK", "DENMARK"),
                            ("DJ", "DJIBOUTI"),
                            ("DM", "DOMINICA"),
                            ("DO", "DOMINICAN REPUBLIC"),
                            ("EC", "ECUADOR"),
                            ("EG", "EGYPT"),
                            ("SV", "EL SALVADOR"),
                            ("GQ", "EQUATORIAL GUINEA"),
                            ("ER", "ERITREA"),
                            ("EE", "ESTONIA"),
                            ("ET", "ETHIOPIA"),
                            ("FK", "FALKLAND ISLANDS (MALVINAS)"),
                            ("FO", "FAROE ISLANDS"),
                            ("FJ", "FIJI"),
                            ("FI", "FINLAND"),
                            ("FR", "FRANCE"),
                            ("GF", "FRENCH GUIANA"),
                            ("PF", "FRENCH POLYNESIA"),
                            ("TF", "FRENCH SOUTHERN TERRITORIES"),
                            ("GA", "GABON"),
                            ("GM", "GAMBIA"),
                            ("GE", "GEORGIA"),
                            ("DE", "GERMANY"),
                            ("GH", "GHANA"),
                            ("GI", "GIBRALTAR"),
                            ("GR", "GREECE"),
                            ("GL", "GREENLAND"),
                            ("GD", "GRENADA"),
                            ("GP", "GUADELOUPE"),
                            ("GU", "GUAM"),
                            ("GT", "GUATEMALA"),
                            ("GN", "GUINEA"),
                            ("GW", "GUINEA"),
                            ("GY", "GUYANA"),
                            ("HT", "HAITI"),
                            ("HM", "HEARD ISLAND AND MCDONALD ISLANDS"),
                            ("HN", "HONDURAS"),
                            ("HK", "HONG KONG"),
                            ("HU", "HUNGARY"),
                            ("IS", "ICELAND"),
                            ("IN", "INDIA"),
                            ("ID", "INDONESIA"),
                            ("IR", "IRAN, ISLAMIC REPUBLIC OF"),
                            ("IQ", "IRAQ"),
                            ("IE", "IRELAND"),
                            ("IL", "ISRAEL"),
                            ("IT", "ITALY"),
                            ("JM", "JAMAICA"),
                            ("JP", "JAPAN"),
                            ("JO", "JORDAN"),
                            ("KZ", "KAZAKHSTAN"),
                            ("KE", "KENYA"),
                            ("KI", "KIRIBATI"),
                            ("KP", "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF"),
                            ("KR", "KOREA, REPUBLIC OF"),
                            ("KW", "KUWAIT"),
                            ("KG", "KYRGYZSTAN"),
                            ("LA", "LAO PEOPLE'S DEMOCRATIC REPUBLIC"),
                            ("LV", "LATVIA"),
                            ("LB", "LEBANON"),
                            ("LS", "LESOTHO"),
                            ("LR", "LIBERIA"),
                            ("LY", "LIBYAN ARAB JAMAHIRIYA"),
                            ("LI", "LIECHTENSTEIN"),
                            ("LT", "LITHUANIA"),
                            ("LU", "LUXEMBOURG"),
                            ("MO", "MACAO"),
                            ("MK", "MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF"),
                            ("MG", "MADAGASCAR"),
                            ("MW", "MALAWI"),
                            ("MY", "MALAYSIA"),
                            ("MV", "MALDIVES"),
                            ("ML", "MALI"),
                            ("MT", "MALTA"),
                            ("MH", "MARSHALL ISLANDS"),
                            ("MQ", "MARTINIQUE"),
                            ("MR", "MAURITANIA"),
                            ("MU", "MAURITIUS"),
                            ("YT", "MAYOTTE"),
                            ("MX", "MEXICO"),
                            ("FM", "MICRONESIA, FEDERATED STATES OF"),
                            ("MD", "MOLDOVA, REPUBLIC OF"),
                            ("MC", "MONACO"),
                            ("MN", "MONGOLIA"),
                            ("MS", "MONTSERRAT"),
                            ("MA", "MOROCCO"),
                            ("MZ", "MOZAMBIQUE"),
                            ("MM", "MYANMAR"),
                            ("NA", "NAMIBIA"),
                            ("NR", "NAURU"),
                            ("NP", "NEPAL"),
                            ("NL", "NETHERLANDS"),
                            ("AN", "NETHERLANDS ANTILLES"),
                            ("NC", "NEW CALEDONIA"),
                            ("NZ", "NEW ZEALAND"),
                            ("NI", "NICARAGUA"),
                            ("NE", "NIGER"),
                            ("NG", "NIGERIA"),
                            ("NU", "NIUE"),
                            ("NF", "NORFOLK ISLAND"),
                            ("MP", "NORTHERN MARIANA ISLANDS"),
                            ("NO", "NORWAY"),
                            ("OM", "OMAN"),
                            ("PK", "PAKISTAN"),
                            ("PW", "PALAU"),
                            ("PS", "PALESTINIAN TERRITORY, OCCUPIED"),
                            ("PA", "PANAMA"),
                            ("PG", "PAPUA NEW GUINEA"),
                            ("PY", "PARAGUAY"),
                            ("PE", "PERU"),
                            ("PH", "PHILIPPINES"),
                            ("PN", "PITCAIRN"),
                            ("PL", "POLAND"),
                            ("PT", "PORTUGAL"),
                            ("PR", "PUERTO RICO"),
                            ("QA", "QATAR"),
                            ("RE", "RÃ‰UNION"),
                            ("RO", "ROMANIA"),
                            ("RU", "RUSSIAN FEDERATION"),
                            ("RW", "RWANDA"),
                            ("SH", "SAINT HELENA"),
                            ("KN", "SAINT KITTS AND NEVIS"),
                            ("LC", "SAINT LUCIA"),
                            ("PM", "SAINT PIERRE AND MIQUELON"),
                            ("VC", "SAINT VINCENT AND THE GRENADINES"),
                            ("WS", "SAMOA"),
                            ("SM", "SAN MARINO"),
                            ("ST", "SAO TOME AND PRINCIPE"),
                            ("SA", "SAUDI ARABIA"),
                            ("SN", "SENEGAL"),
                            ("CS", "SERBIA AND MONTENEGRO"),
                            ("SC", "SEYCHELLES"),
                            ("SL", "SIERRA LEONE"),
                            ("SG", "SINGAPORE"),
                            ("SK", "SLOVAKIA"),
                            ("SI", "SLOVENIA"),
                            ("SB", "SOLOMON ISLANDS"),
                            ("SO", "SOMALIA"),
                            ("ZA", "SOUTH AFRICA"),
                            ("GS", "SOUTH GEORGIA AND SOUTH SANDWICH ISLANDS"),
                            ("ES", "SPAIN"),
                            ("LK", "SRI LANKA"),
                            ("SD", "SUDAN"),
                            ("SR", "SURINAME"),
                            ("SJ", "SVALBARD AND JAN MAYEN"),
                            ("SZ", "SWAZILAND"),
                            ("SE", "SWEDEN"),
                            ("CH", "SWITZERLAND"),
                            ("SY", "SYRIAN ARAB REPUBLIC"),
                            ("TW", "TAIWAN, PROVINCE OF CHINA"),
                            ("TJ", "TAJIKISTAN"),
                            ("TZ", "TANZANIA, UNITED REPUBLIC OF"),
                            ("TH", "THAILAND"),
                            ("TL", "TIMOR"),
                            ("TG", "TOGO"),
                            ("TK", "TOKELAU"),
                            ("TO", "TONGA"),
                            ("TT", "TRINIDAD AND TOBAGO"),
                            ("TN", "TUNISIA"),
                            ("TR", "TURKEY"),
                            ("TM", "TURKMENISTAN"),
                            ("TC", "TURKS AND CAICOS ISLANDS"),
                            ("TV", "TUVALU"),
                            ("UG", "UGANDA"),
                            ("UA", "UKRAINE"),
                            ("AE", "UNITED ARAB EMIRATES"),
                            ("GB", "UNITED KINGDOM"),
                            ("US", "UNITED STATES"),
                            ("UM", "UNITED STATES MINOR OUTLYING ISLANDS"),
                            ("UY", "URUGUAY"),
                            ("UZ", "UZBEKISTAN"),
                            ("VU", "VANUATU"),
                            ("VN", "VIET NAM"),
                            ("VG", "VIRGIN ISLANDS, BRITISH"),
                            ("VI", "VIRGIN ISLANDS, U.S."),
                            ("WF", "WALLIS AND FUTUNA"),
                            ("EH", "WESTERN SAHARA"),
                            ("YE", "YEMEN"),
                            ("ZW", "ZIMBABWE"),
                        ],
                        max_length=64,
                    ),
                ),
                (
                    "postal_code",
                    models.CharField(
                        max_length=16,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Field must contain only number and no white spaces.",
                                regex="[0-9]",
                            )
                        ],
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="VenueClassification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        max_length=256,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Field must only contain basic Latin characters and spaces.",
                                regex="[a-zA-Z ]",
                            )
                        ],
                    ),
                ),
                ("description", models.TextField()),
            ],
            options={
                "ordering": ["id"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Venue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "code",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Username must match this: '[a-zA-Z0-9_]{8,32}'",
                                regex="[a-zA-Z0-9_]{8,32}",
                            )
                        ],
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Field must match this: '[a-zA-Z0-9_\\-\\(\\) ]'",
                                regex="[a-zA-Z0-9_\\-\\(\\) ]",
                            )
                        ],
                    ),
                ),
                (
                    "campus",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_campus.campus",
                    ),
                ),
                (
                    "classification",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="app_campus.venueclassification",
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
                "abstract": False,
            },
        ),
    ]
