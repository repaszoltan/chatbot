from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import random
import datetime

import re

def start(bot, update):
	#Üdvözlet és csekkoljuk ki a főnök
	#Később lesz olyan függvény amit csak én szeretnák használni
	chat_id = update.message.chat_id
	if chat_id == 'my chat id number':
		update.message.reply_text('Szervusz kisgazdám, rendelkezz velem.')
	else:
		update.message.reply_text('Szervusz, Kisfiú vagyok! Válasz a lehetséges parancsok közül.')

#Via: freecodecamp.org-->
def get_url():
	contents = requests.get('https://random.dog/woof.json').json()
	url = contents['url']
	return url

def bop(bot, update):
	url = get_url()
	chat_id = update.message.chat_id
	update.message.reply_text('Nézdcsak milyen cuki:')
	bot.send_photo(chat_id=chat_id, photo=url)
	#<-- freecodecamp.org

def gis(bot, update):
	#Bullshit pool
	bs_1 = ['Erőforrás-alapú megközelítéssel kell',
	'Alapvető fontosságú',
	'Kiemelt projektünk',
	'A térinformatikai menedzsment célja',
	'Teljes összhangban kell',
	'Teamworkben szükséges',
	'Napjaink információs társadalmában muszáj',
	'A térinformatika célja',
	'Kiemelt fontosságú feladat',
	'Ennek szellemében kell',
	'Térinformatikai alapon kellene',
	'Alkotó folyamat keretében kell',
	'A térinformatikai paradigmaváltás következtében muszáj',
	'A térinformatika, mint távcső, lehetőséget ad',
	'A Térinformatikai Tudástárnak köszönhetően lehetővé vált',
	'A térinformatika atyjának elvei szerint kell',
	'A térinformatikai menedzsment szeretné',
	'A tudományág szeretné',
	'Az adatgyűjtésben szükséges',
	'Küldetésünk:',
	'A Térinformatikai Tudásközpont célja',
	'A tervezési fázisban kell',
	'A lényeg:',
	'Tudásközpontunk feladata:',
	'Küldetésünk:',
	'A mai legfontosabb prioritás:',
	'A szakirányú továbbképzés feladata',
	'Megkíséreljük',
	'Salzburgi partnereinkkel megkíséreljük',
	'Küldetésünk:',
	'GIS-koncepció szerint kell',
	'Azonnal szükséges',
	'Egy megoldás van:',
	'A térinformatikában kreatív módon kell',
	'Küldetésünk:',
	'A UNIGIS célja:',
	'GIS Open konferenciáinkon segítünk',
	'Küldetésünk:',
	'A megvalósítási fázisban kell',
	'Kreatív módon kell',
	'Elemzések segítségével kell',
	'Kreatív módon kéne',
	'A térbeli döntéselőkészítés lényege',
	'Az ESRI ArcGIS rendszerével könnyedén lehet',
	'Professzionális módon kell']

	bs_2 = ['implementálni',
	'átültetni',
	'aktívan menedzselni',
	'meghatározó szerepet betölteni',
	'analizálni',
	'meghatározó szerepet betölteni',
	'arányosítani',
	'meghatározó szerepet betölteni',
	'betanítani',
	'befolyásolni',
	'benchmark tesztelni',
	'analizálni',
	'szintetizálni',
	'bővíteni',
	'ellenőrizni',
	'elemezni',
	'életre kelteni',
	'fejleszteni',
	'felszabadítani',
	'forradalmasítani',
	'generálni',
	'hasznosítani',
	'hatékonyabbá tenni',
	'innovatívan fejleszteni',
	'integrálni',
	'interpretálni',
	'leválogatni',
	'kihasználni',
	'kiterjeszteni',
	'lehetővé tenni',
	'meghatározni',
	'megváltoztatni',
	'menedzselni',
	'megtervezni',
	'motiválni',
	'növelni',
	'optimalizálni',
	'ösztönözni',
	'kiépíteni',
	'rávilágítani',
	'racionálisan végiggondolni',
	'racionalizálni',
	'struktúrálni',
	'szakmailag felügyelni',
	'szimulálni',
	'szinergizálni',
	'szinkronba hozni',
	'sztenderdizálni',
	'szintetizálni',
	'támogatni',
	'testreszabni',
	'tipizálni',
	'transzformálni',
	'túlteljesíteni',
	'új kontextusba helyezni',
	'újra feltalálni',
	'újra meghatározni',
	'újradefiniálni',
	'újrapozícionálni',
	'újratermelni',
	'vizionálni',
	'vizualizálni']

	bs_3 = ['a normáknak megfelelő',
	'a centralizált',
	'a dinamikusan növekvo',
	'a GIS specifikus',
	'a fontos',
	'a felvállalható',
	'a forradalmian új',
	'a funkció-specifikus',
	'a globális preferenciák szerinti',
	'a lokális preferenciák szerinti',
	'a természetvédelmi előírásoknak megfelelő',
	'a hibátlan',
	'az önkormányzati szinten elvárt',
	'a kihívást jelentő',
	'az analóg',
	'a konzisztens',
	'a korrigálható',
	'a korreláló',
	'a költséghatékony',
	'a digitális',
	'a kritikus',
	'a kvázi-projekt-szerű',
	'a marketing-szemléletű',
	'a menedzsment-szemléletű',
	'a menedzsment-szemléletű',
	'a megtérülő',
	'a metakommunkiációs',
	'a hatékony menedzsment szemléletű',
	'az összehangolt',
	'a piacvezető',
	'a proaktív',
	'az innovatív',
	'a geomarketingen alapuló',
	'a térszemléletű',
	'a racionális',
	'a rendszeres',
	'a rugalmas',
	'a sajátos',
	'a technológia-orientált',
	'a stratégiai céloknak megfelelő',
	'a stratégiáknak megfelelő',
	'a súrlódásmentes',
	'a további bullshiteket generáló',
	'a széles körben használt',
	'a személyre szabott',
	'a szinergizált',
	'a tudatos',
	'a technológia-orientált',
	'a vállalható',
	'a valós idejű',
	'a technológia-orientált',
	'a világszínvonalú',
	'a virtuális',
	'a topográfiai',
	'a XXI. századi színvonalú',
	'a GIS alapú',
	'a GIS központú',
	'a GIS-re épülő',
	'a térinformatikai',
	'az intézményközi',
	'a rutinos',
	'a geodéziai',
	'az átlátható',
	'a geodéziában megszokott',
	'az egységes',
	'az együttműködő',
	'a geodéziaitól eltérő',
	'az információs',
	'a távérzékelésben használatos',
	'a hibaelméleti',
	'az értéknövelt',
	'az európai színvonalú',
	'az európai uniós',
	'az extenzív',
	'az adatpolitikai',
	'az intézetigazgató úr által is említett',
	'az innovatív',
	'az integrált',
	'az interaktív',
	'a földrajzi helyhez köthető',
	'az irányvonalnak megfelelő',
	'az felhasználóbarát',
	'az felhasználóközpontú',
	'az felhasználóoldali',
	'a GNSS-támogatott',
	'a 3D-s']

	bs_4 = ['szinergiákat',
	'adatbázist',
	'nyilvántartási munkamegosztást',
	'pilot-projekteket',
	'geoinformatikát',
	'beruházási megtérülést',
	'menedzsmentet',
	'megjelenítést',
	'térinformatikai képzést',
	'csatornákat',
	'felhasználót',
	'adatminőséget',
	'egységköltséget',
	'adattömörítést',
	'adatkonzisztenciát',
	'humán erőforrást',
	'erőforrás-menedzsmentet',
	'erőforrásokat',
	'elméleti modellt',
	'értéknövelt adatokat',
	'fejlesztéseket',
	'feladatmegosztást',
	'adatokból nyert információkat',
	'felhasználói bázist',
	'helyfüggő szolgáltatásokat',
	'minőségbiztosítást',
	'topológiát',
	'tájtervezést',
	'rendszereket',
	'háttérszolgáltatásokat',
	'térinformatikai infrastruktúrát',
	'imázs-alakítást',
	'infrastruktúrákat',
	'intermodalitást',
	'interoperabilitást',
	'INSPIRE irányelveket',
	'rendszerirányítási filozófiát',
	'továbbképzési lehetőségeket',
	'kapacitás-kihasználtságot',
	'kínai kapcsolatokat',
	'újszerű kezdeményezéseket',
	'koncepciót',
	'környezetelemzést',
	'kritériumokat',
	'adatbányászatot',
	'döntéstámogatást',
	'geomarketinget',
	'marketing-szemléletet',
	'alternatív megoldásokat',
	'mérföldköveket',
	'térbeli szolgáltatásokat',
	'minoség-monitoringot',
	'frémwörköt',
	'optimalizálási koncepciót',
	'feedbacket',
	'paradigmákat',
	'webes megjelenést',
	'webes potenciált',
	'adatréseket',
	'webes trendeket',
	'informatikai piacokat',
	'pilot projektet',
	'platformokat',
	'projekteket',
	'GIS rendszereket',
	'rendszertervezési technológiát',
	'felsőfokú oktatást',
	'stratégiai célokat',
	'szabványosítást',
	'sztenderdizációt',
	'támogató tevékenységet',
	'oktatási palettát',
	'technológiákat',
	'tudásközpontot',
	'felhasználókat',
	'supportot',
	'felhasználó-kiszolgálást',
	'felhasználóorientált trendeket',
	'projektmenetet',
	'felsőoktatási imázst',
	'felsőfokú oktatást',
	'versenyhelyzetet',
	'felsőfokú oktatást']
	b1 = random.choice(bs_1)
	b2 = random.choice(bs_2)
	b3 = random.choice(bs_3)
	b4 = random.choice(bs_4)
	bullshit = b1+' '+b2+' '+b3+' '+b4+'.'
	chat_id = update.message.chat_id
	update.message.reply_text(bullshit)

def doki(bot, update):
	#Mikor rendel Dénes'bá :)
	chat_id = update.message.chat_id
	#Mai dátum:
	myDate = datetime.datetime.now()
	#Hanyadik hét van:
	weekNum = int(myDate.strftime("%W"))

	#Mikor rendel a adatpolitikai
	if weekNum%2 == 0:
		update.message.reply_text('Dénes doki a héten délután rendel.')
	else:
		update.message.reply_text('Dénes doki a héten délelőtt rendel.')



def main():
	updater = Updater('YOUR_API_KEY')
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start',start))
	dp.add_handler(CommandHandler('vau',bop))
	dp.add_handler(CommandHandler('gis',gis))
	dp.add_handler(CommandHandler('doki',doki))
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
    main()
