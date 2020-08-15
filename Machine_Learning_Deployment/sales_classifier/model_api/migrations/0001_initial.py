# Generated by Django 3.0.8 on 2020-08-02 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('July', 'July'), ('Aug', 'Aug'), ('Sep', 'Sep'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], max_length=100)),
                ('lead_type', models.CharField(choices=[('New Lead', 'New Lead'), ('Existing Lead', 'Existing Lead')], max_length=100)),
                ('lead_priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=100)),
                ('lead_source', models.CharField(choices=[('MARKET PLACE', 'MARKET PLACE'), ('SEO', 'SEO'), ('INSIDE SALES', 'INSIDE SALES'), ('DIRECT', 'DIRECT'), ('SMO', 'SMO')], max_length=100)),
                ('marketplace_subsource', models.CharField(choices=[('UPWORK', 'UPWORK'), ('FREELANCER', 'FREELANCER'), ('PPH', 'PPH'), ('GURU', 'GURU'), ('OTHERS', 'OTHERS')], max_length=100)),
                ('country', models.CharField(choices=[('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('American Samoa', 'American Samoa'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antarctica', 'Antarctica'), ('Antigua And Barbuda', 'Antigua And Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Aruba', 'Aruba'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahrain', 'Bahrain'), ('Bangkok', 'Bangkok'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Benin'), ('Botswana', 'Botswana'), ('Bouvet Island', 'Bouvet Island'), ('Brazil', 'Brazil'), ('British Indian Ocean Territory', 'British Indian Ocean Territory'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'), ('Cape Verde', 'Cape Verde'), ('Cayman Islands', 'Cayman Islands'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Costa Rica', 'Costa Rica'), ('Cote DIvoire (Ivory Coast)', "Cote D'Ivoire (Ivory Coast)"), ('Croatia (Hrvatska)', 'Croatia (Hrvatska)'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Democratic Republic Of The Congo', 'Democratic Republic Of The Congo'), ('Denmark', 'Denmark'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('Fiji Islands', 'Fiji Islands'), ('Finland', 'Finland'), ('France', 'France'), ('French Guiana', 'French Guiana'), ('Gabon', 'Gabon'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Greece', 'Greece'), ('Greenland', 'Greenland'), ('Grenada', 'Grenada'), ('Guernsey & Alderney', 'Guernsey and Alderney'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Haiti', 'Haiti'), ('Hong Kong', 'Hong Kong'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Isle of Man', 'Isle of Man'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kiribati', 'Kiribati'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Macau S.A.R.', 'Macau S.A.R.'), ('Macedonia', 'Macedonia'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Mauritania', 'Mauritania'), ('Mayotte', 'Mayotte'), ('Mexico', 'Mexico'), ('Moldova', 'Moldova'), ('Mongolia', 'Mongolia'), ('Morocco', 'Morocco'), ('Myanmar', 'Myanmar'), ('Namibia', 'Namibia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('Netherlands Antilles', 'Netherlands Antilles'), ('New Zealand', 'New Zealand'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Niue', 'Niue'), ('Norfolk Island', 'Norfolk Island'), ('North Korea', 'North Korea'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Others', 'Others'), ('Pakistan', 'Pakistan'), ('Palau', 'Palau'), ('Palestinian Territory Occupied', 'Palestinian Territory Occupied'), ('Panama', 'Panama'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Pitcairn Island', 'Pitcairn Island'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Qatar', 'Qatar'), ('Republic Of The Congo', 'Republic Of The Congo'), ('Romania', 'Romania'), ('Russia', 'Russia'), ('Rwanda', 'Rwanda'), ('Saint Helena', 'Saint Helena'), ('Saint Lucia', 'Saint Lucia'), ('Saint Vincent And The Grenadines', 'Saint Vincent And The Grenadines'), ('Samoa', 'Samoa'), ('Saudi Arabia', 'Saudi Arabia'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Singapore', 'Singapore'), ('Slovakia', 'Slovakia'), ('South Africa', 'South Africa'), ('South Korea', 'South Korea'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Swaziland', 'Swaziland'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Taiwan', 'Taiwan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('The Bahamas', 'The Bahamas'), ('Trinidad And Tobago', 'Trinidad And Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Turks And Caicos Islands', 'Turks And Caicos Islands'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('United Kingdom', 'United Kingdom'), ('United States', 'United States'), ('Uruguay', 'Uruguay'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], max_length=100)),
                ('business_potential', models.IntegerField()),
                ('company_size', models.CharField(choices=[('Small company', 'Small company'), ('Midsize company', 'Midsize company'), ('Large company', 'Large company'), ('Multinational company', 'Multinational company')], max_length=100)),
                ('platform', models.CharField(choices=[('MOBILE APP + BACKEND', 'MOBILE APP + BACKEND'), ('IOT', 'IOT'), ('GAME', 'GAME'), ('MOBILE APP', 'MOBILE APP'), ('Open Backend', 'Open Backend'), ('Blockchain- ICO Launch', 'Blockchain- ICO Launch'), ('Blockchain- Crypto Exchange', 'Blockchain- Crypto Exchange'), ('WEB', 'WEB'), ('BOTS', 'BOTS'), ('Blockchain- ICO Marketing', 'Blockchain- ICO Marketing'), ('Native Mobile', 'Native Mobile'), ('Blockchain- Crypto Wallet', 'Blockchain- Crypto Wallet'), ('Blockchain- DApp', 'Blockchain- DApp'), ('Blockchain- Smart Contract Development & Audit', 'Blockchain- Smart Contract Development and Audit'), ('DIGITAL MARKETING', 'DIGITAL MARKETING'), ('Others', 'Others')], max_length=100)),
            ],
        ),
    ]