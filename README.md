![Python >= 3.6](https://img.shields.io/badge/python->=3.6-red.svg) [![](https://badgen.net/github/release/deedy5/vm_ddgsearch)](https://github.com/deedy5/vm_ddgsearch/releases) [![](https://badge.fury.io/py/duckduckgo-search.svg)](https://pypi.org/project/duckduckgo-search) 
## vm_ddgsearch

Search for words, documents, images, news, maps and text translation using the DuckDuckGo.com search engine. This is a fork of https://github.com/deedy5/duckduckgo_search.

***Install***
```python
pip install -U vm_ddgsearch
```
### Table of Contents  
[Duckduckgo search operators](#duckduckgo-search-operators)  
[1. ddg()](#1-ddg---search-by-duckduckgocom)</br>
[2. ddg_images()](#2-ddg_images---image-search-by-duckduckgocom)</br> 
[3. ddg_news()](#3-ddg_news---news-search-by-duckduckgocom)</br>
[4. ddg_maps()](#4-ddg_maps---map-search-by-duckduckgocom)</br>
[5. ddg_translate()](#5-ddg_translate---translation-by-duckduckgocom)</br>
___
## Duckduckgo search operators

| Keywords example |	Result|
| ---     | ---   |
| cats dogs |	Results about cats or dogs |
| "cats and dogs" |	Results for exact term "cats and dogs". If no results are found, related results are shown. |
| cats -dogs |	Fewer dogs in results |
| cats +dogs |	More dogs in results |
| cats filetype:pdf |	PDFs about cats. Supported file types: pdf, doc(x), xls(x), ppt(x), html |
| dogs site:example.com  |	Pages about dogs from example.com |
| cats -site:example.com |	Pages about cats, excluding example.com |
| intitle:dogs |	Page title includes the word "dogs" |
| inurl:cats  |	Page url includes the word "cats" |
___
## 1. ddg() - search by duckduckgo.com

*WARNING!*: set a delay of at least **0.75** seconds between function calls.

```python
from vm_ddgsearch import ddg

def ddg(keywords, region='wt-wt', safesearch='Moderate', time=None, max_results=28):
    ''' DuckDuckGo search
    keywords: keywords for query;
    safesearch: On (kp = 1), Moderate (kp = -1), Off (kp = -2);
    region: country of results - wt-wt (Global), us-en, uk-en, ru-ru, etc.;
    time: 'd' (day), 'w' (week), 'm' (month), 'y' (year), or 'year-month-date..year-month-date';    
    max_results = 28 gives a number of results not less than 28,   
    maximum DDG gives out about 200 results.
    '''
```
***Returns***
```python
[{'title': title of result,
  'href': href of result,
  'body': body of result,},
 {'title': title of result,
  'href': href of result,
  'body': body of result,}, ...]
```
***Example 1. Text search***
```python
from vm_ddgsearch import ddg

keywords = 'Bella Ciao'
results = ddg(keywords, region='wt-wt', safesearch='Moderate', time='y', max_results=28)
print(results)
```
```python
[
{'title': 'Bella Ciao - Original Italian Lyrics & English Translation ...', 'href': 'https://dailyitalianwords.com/bella-ciao-original-italian-lyrics-english-translation/', 'body': 'Bella Ciao - English Meaning (Mondine version) In the morning as soon as I get up oh goodbye beautiful, goodbye beautiful, goodbye beautiful, bye, bye, bye In the morning as soon as I get up I have to go to the paddy fields. And between insects and mosquitoes oh goodbye beautiful, goodbye beautiful, goodbye beautiful, bye, bye, bye'},
{'title': "What's the meaning of Bella Ciao | Italian song explained", 'href': 'https://www.thinkinitalian.com/bella-ciao-meaning/', 'body': "Bella Ciao is probably the most famous Italian folk song. It has been sung anywhere in the world for years, and the TV series Money Heist made it even more popular. But what does it talk about? What's the story behind its lyrics? This is a perfect chance to learn some more Italian with the meaning of Bella Ciao. Italian culture Michele"},
...
]
```
***Example 2. Searching for pdf files***
```python
from vm_ddgsearch import ddg

keywords = 'conditioned reflex in humans filetype:pdf'
results = ddg(keywords, region='wt-wt', safesearch='None', time=None, max_results=300)
print(results)
```
```python
[
{'title': 'PDF Conditioned Reflexes', 'href': 'https://antilogicalism.com/wp-content/uploads/2019/04/conditioned-reflexes.pdf', 'body': '302 CONDITIONED REFLEXES. in the strength of the reflexes, a state of ;affair.~ which lasted for many. days, the relation between the magnitudes of the reflexes and the Other dogs those of the inhibitable type suffered a functional disturbance of the cortical activities for a very considerable period.'},
{'title': 'Conditioned reflex therapy; the direct approach to the reconstruction...', 'href': 'https://archive.org/details/conditionedrefle00salt', 'body': "Two chapters were rewritten and expanded from the author's What is hypnosis. One was reprinted from the South west review. Bibliography: p. 321-340."},
{'title': 'conditioned reflex examples in humans - Bing', 'href': 'https://technopagan.org/conditioned+reflex+examples+in+humans&FORM=QSRE4', 'body': 'Jun 02, 2021 · Conditioned Reflex Examples In Humans And not discrimination is directly with dogs was presented is absent, and emotional responses being subtle variations in... When they hear thunder, in conditioned reflex was sent to humans are allowed early contributions ivan to know about why...'},
...
]
```
___
## 2. ddg_images() - image search by duckduckgo.com
```python
from vm_ddgsearch import ddg_images

def ddg_images(keywords, region='wt-wt', safesearch='Moderate', time=None, size=None,
           color=None, type_image=None, layout=None, license_image=None, max_results=100):
    ''' DuckDuckGo images search
    keywords: keywords for query;
    safesearch: On (kp = 1), Moderate (kp = -1), Off (kp = -2);
    region: country of results - wt-wt (Global), us-en, uk-en, ru-ru, etc.;
    time: Day, Week, Month, Year;
    size: Small, Medium, Large, Wallpaper;
    color: color, Monochrome, Red, Orange, Yellow, Green, Blue, Purple, Pink, Brown, Black, Gray, Teal, White;
    type_image: photo, clipart, gif, transparent, line;
    layout: Square, Tall, Wide;
    license_image: any (All Creative Commons), Public (Public Domain), Share (Free to Share and Use),
             ShareCommercially (Free to Share and Use Commercially), Modify (Free to Modify, Share, and Use),
             ModifyCommercially (Free to Modify, Share, and Use Commercially);
    max_results: number of results, maximum ddg_images gives out 1000 results.
    '''
```
***Returns***
```python
[{'height': image height,
  'image': image url,
  'source': image source,
  'thumbnail': image thumbnail,
  'title': image title,
  'url': url where the image was found,
  'width': image width },  
 ...
 ]
```
***Example***
```python
from vm_ddgsearch import ddg_images

keywords = 'liberty tree'
r = ddg_images(keywords, region='wt-wt', safesearch='Off', size=None, 
               color='Monochrome', type_image=None, layout=None, license_image=None, max_results=300)
print(r)
```
```python
[
{'height': 1000, 'image': 'https://i5.walmartimages.com/asr/fef2dbdb-3756-4401-b7ae-502ec2ea082b_1.eb37ae35a5e3d4ae59d61ecac336c226.jpeg?odnWidth=1000&odnHeight=1000&odnBg=ffffff', 'source': 'Bing', 'thumbnail': 'https://tse2.mm.bing.net/th?id=OIP.4DhDDdx9IOAwbFm6CRGpTwHaHa&pid=Api', 'title': 'Liberty Tree 1765 Nthe Large Elm Tree At Boylston Market ...', 'url': 'https://www.walmart.com/ip/Liberty-Tree-1765-Nthe-Large-Elm-Tree-Boylston-Market-Boston-Massachusetts-Named-Liberty-Tree-Sons-Liberty-Held-Meetings-Summer-1765-Wood-Engraving-A/997377547?wmlspartner=bizratecom&affcmpid=3313893407&tmode=0000', 'width': 1000},
{'height': 2400, 'image': 'http://etc.usf.edu/clipart/13500/13570/liberty-tree_13570.tif', 'source': 'Bing', 'thumbnail': 'https://tse2.mm.bing.net/th?id=OIP.4t3AojTiUP6TZ-AFaSfCHAHaJ7&pid=Api', 'title': 'Liberty Tree | ClipArt ETC', 'url': 'http://etc.usf.edu/clipart/13500/13570/liberty-tree_13570.htm', 'width': 1790},
{'height': 297, 'image': 'https://www.blogtalkradio.com/api/image/resize/400x297/aHR0cHM6Ly9kYXNnN3h3bWxkaXg2LmNsb3VkZnJvbnQubmV0L2hvc3RwaWNzLzc1MGZhZjVhLTJhMTUtNDE5Ni1iOTQwLTA1NTc1NjVlMGM1MV9saWJlcnR5LXRyZWVfbG9nby5qcGc/750faf5a-2a15-4196-b940-0557565e0c51_liberty-tree_logo.jpg?mode=Fill', 'source': 'Bing', 'thumbnail': 'https://tse2.mm.bing.net/th?id=OIP.IQxgK4LaaFV82m7Iz9J3sgAAAA&pid=Api', 'title': 'Liberty Tree Radio Online Radio | BlogTalkRadio', 'url': 'http://www.blogtalkradio.com/libertytreeradio', 'width': 400},
...
]
```
___
## 3. ddg_news() - news search by duckduckgo.com
```python
from vm_ddgsearch import ddg_news

def ddg_news(keywords, region='wt-wt', safesearch='Moderate', time=None, max_results=30):
    ''' DuckDuckGo news search
    keywords: keywords for query;
    safesearch: On (kp = 1), Moderate (kp = -1), Off (kp = -2);
    region: country of results - wt-wt (Global), us-en, uk-en, ru-ru, etc.;
    time: 'd' (day), 'w' (week), 'm' (month);    
    max_results = 30, maximum DDG_news gives out 240 results.
    '''
```
***Returns***
```python
[{'date': datetime in isoformat,
  'title': title of result,
  'body': body of result,
  'url': url of result,
  'image': image url,
  'source': source of result, 
 ...
 ]
```
***Example***
```python
from vm_ddgsearch import ddg_news

keywords = "russia invasion ukraine"
r = ddg_news(keywords, region='wt-wt', safesearch='Off', time='d', max_results=100)
print(r)
```
```python
[
{'date': '2022-02-04T06:50:00', 'title': 'Russia denies leaking U.S. security talks document to El Pais', 'body': 'Moscow has demanded guarantees from Washington and NATO that Ukraine will not be allowed to join the military bloc. Russia has amassed over 100,000 troops close to the Ukrainian borders, but denies planning an invasion.', 'url': 'https://wdez.com/2022/02/04/russia-denies-leaking-u-s-security-talks-document-to-el-pais/', 'image': 'https://storage.googleapis.com/media.mwcradio.com/mimesis/2022-02/04/2022-02-04T060600Z_1_LYNXMPEI13053_RTROPTP_3_RUSSIA-USA-SECURITY.JPG', 'source': 'WDEZ'},
{'date': '2022-02-04T06:50:00', 'title': 'Analysis-Traders scour markets for protection amid Ukraine tensions', 'body': 'LONDON (Reuters) - Unnerved by the sabre-rattling between Russia and the West over Ukraine, traders are scouring ... a 10% probability of a full-fledged invasion. Ganry recommends a different ...', 'url': 'https://wsau.com/2022/02/04/analysis-traders-scour-markets-for-protection-amid-ukraine-tensions/', 'image': 'https://storage.googleapis.com/media.mwcradio.com/mimesis/2022-02/04/2022-02-04T061136Z_2_LYNXMPEI13058_RTROPTP_3_GLOBAL-MARKETS-TRADING.JPG', 'source': 'WSAY'},
{'date': '2022-02-04T06:47:00', 'title': "Morning news brief: US's warning on Russia-Ukraine crisis, Johnson's top aides quitting, and more", 'body': 'Russia will produce graphic propaganda video as pretext for an invasion against Ukraine: US © Provided by WION Pentagon officials said today that Russia could fabricate a pretext for an invasion of Ukraine. "As part of this fake attack, we believe that ...', 'url': 'https://www.msn.com/en-in/news/world/morning-news-brief-us-s-warning-on-russia-ukraine-crisis-johnson-s-top-aides-quitting-and-more/ar-AATs9ml', 'image': 'https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AATsnww.img?h=315&w=600&m=6&q=60&o=t&l=f&f=jpg', 'source': 'MSN'},
...
]
```
___
## 4. ddg_maps() - map search by duckduckgo.com
```python
from vm_ddgsearch import ddg_maps

def ddg_maps(keywords, place=None, street=None, city=None, county=None, state=None,
             country=None, postalcode=None, latitude=None, longitude=None, radius=0):
    ''' DuckDuckGo maps search
    keywords: keywords for query;
    place: simplified search - if set, the other parameters are not used;
    street: house number/street;
    city: city of search;
    county: county of search;
    state: state of search;
    country: country of search;
    postalcode: postalcode of search;
    latitude: geographic coordinate that specifies the north–south position;
    longitude: geographic coordinate that specifies the east–west position;
        if latitude and longitude are set, the other parameters are not used.
    radius: expand the search square by the distance in kilometers. 
    '''
```
***Returns***
```python
[{'title': title,
  'address': address,
  'country_code': country code,
  'latitude': latitude,
  'longitude': longitude,
  'url': url,
  'desc': desc,
  'phone': phone,
  'image': image,             
  'source': source,
  'links': links,
  'hours': hours,}
 ...
 ]
```
***Example 1. Simple search (if place parameter is set, the other parameters are not used)***
```python
from vm_ddgsearch import ddg_maps

keywords = 'dentists'
place = 'Los Angeles'

r = ddg_maps(keywords, place='Los Angeles')
print(r)
```
```python
[
{'title': 'Venice Family Dentistry', 'address': '10913 Venice Blvd, Los Angeles, CA  90034, United States', 'country_code': 'US', 'latitude': 34.0159528696929, 'longitude': -118.412624001503, 'url': 'http://venicefamilydentistry.com', 'desc': 'This website is for sale! venicefamilydentistry.com is your first and best source for all of the information you’re looking for. From general topics to more of what you would expect to find here, venicefamilydentistry.com has it all. We hope you find what you are searching for!', 'phone': '+13108733331', 'image': '', 'source': 'http://yelp.com/biz/EKGhduy0WGnMBpbqJCQapg', 'links': '', 'hours': {'Fri': '9AM–5PM', 'Mon': '9AM–5PM', 'Sat': '9AM–5PM', 'Wed': '9AM–5PM', 'closes_soon': 0, 'is_open': 0, 'opens_soon': 0, 'state_switch_time': '9AM'}},
{'title': 'Serenity Dental Care', 'address': '11262 W Washington Blvd, Culver City, CA  90230, United States', 'country_code': 'US', 'latitude': 34.0050049579316, 'longitude': -118.413847088814, 'url': 'https://serenitydentalcare.com', 'desc': None, 'phone': '+13103906500', 'image': None, 'source': 'http://yelp.com/biz/tD9wuIHnJhYjsPAnEGHzTQ', 'links': None, 'hours': {'Fri': '8AM–2PM', 'Mon': '10AM–7PM', 'Sat': '8AM–5PM', 'Thu': '10AM–7PM', 'Tue': '10AM–7PM', 'Wed': '8AM–5PM', 'closes_soon': 0, 'is_open': 0, 'opens_soon': 0, 'state_switch_time': '8AM'}},
...
]
```
***Example 2. Advanced search in city and country***
```python
from vm_ddgsearch import ddg_maps

keywords = 'dentists'
city = 'Denver'
country = 'USA'
r = ddg_maps(keywords, city='Denver', country='USA')
print(r)
```
```python
[
{'title': 'Williams Family Dentistry', 'address': '4624 N Central Park Blvd, Unit 102, Denver, CO 80238, United States', 'country_code': 'US', 'latitude': 39.7804958556395, 'longitude': -104.88231038524, 'url': 'http://www.margiewilliamsdds.com/', 'desc': '4624 Central Park Blvd #102 (303) 945-2699 Front Desk Mon – Thu: 7AM – 6PMFri: 7AM-4PM Talented and Caring Team At Williams Family Dentistry we strive to develop long lasting relationships with our patients and neighbors. We […]', 'phone': '+13039452699', 'image': 'https://margiewilliamsdds.com/wp-content/uploads/2021/06/Dr-Group-photo-scaled.jpg', 'source': 'http://yelp.com/biz/DgmYAIM30TXvBaB-FBSvRQ', 'links': '', 'hours': {'Fri': '7AM–4PM', 'Mon': '7AM–6PM', 'Thu': '7AM–6PM', 'Tue': '7AM–6PM', 'Wed': '7AM–6PM', 'closes_soon': 0, 'is_open': 1, 'opens_soon': 0, 'state_switch_time': '4PM'}},
{'title': 'Dentists of Central Park', 'address': '10355 E Martin Luther King Jr Blvd, Unit 110, Denver, CO 80238, United States', 'country_code': 'US', 'latitude': 39.7602729, 'longitude': -104.8673477, 'url': 'https://www.dentistsofcentralpark.com', 'desc': 'Local dentist near you in Denver. Book your dental appointment for general dentistry, teeth whitening, oral surgery, or emergency dentistry.', 'phone': '+17204038351', 'image': 'https://www.dentistsofcentralpark.com/etc/designs/pds/favicon-152x152.png', 'source': 'http://yelp.com/biz/6GULzhI8Zg6V5Diqyc_rWw', 'links': {'facebook': 'https://www.facebook.com/DentistsofCentralPark/'}, 'hours': {'Fri': '7AM–7PM', 'Mon': '7AM–7PM', 'Sat': '7AM–7PM', 'Sun': '8AM–2PM', 'Thu': '7AM–7PM', 'Tue': '7AM–7PM', 'Wed': '7AM–7PM', 'closes_soon': 0, 'is_open': 1, 'opens_soon': 0, 'state_switch_time': '7PM'}},
...
]
```
***Example 3. Advanced search by address with increasing search square***
```python
from vm_ddgsearch import ddg_maps

keywords = 'dentists'
street = 'Av. Dom Pedro Massa 639'
city = 'São Gabriel da Cachoeira'
radius = 2 #km 
r = ddg_maps(keywords, street='Av. Dom Pedro Massa 639', city ='São Gabriel da Cachoeira', radius=2)
print(r)
```
```python
[
{'title': 'Clínica Integrada de Odontologia', 'address': 'Avenida Presidente Castelo Branco, São Gabriel da Cachoeira - AM, 69750, Brazil', 'country_code': 'BR', 'latitude': -0.130427164469837, 'longitude': -67.0899445932125, 'url': '', 'desc': None, 'phone': '+559734711654', 'image': None, 'source': 'https://maps.apple.com/place?q=Cl%C3%ADnica%20Integrada%20de%20Odontologia&auid=7074519049033716214&address=Avenida%20Presidente%20Castelo%20Branco,%20S%C3%A3o%20Gabriel%20da%20Cachoeira%20-%20AM,%2069750,%20Brazil&ll=-0.13042716446983657,-67.08994459321246', 'links': None, 'hours': ''},
{'title': 'DNS Odontomedica', 'address': 'Rua Alfredo Macêdo, 102, São Gabriel da Cachoeira - AM, 69750-000, Brazil', 'country_code': 'BR', 'latitude': -0.1242364, 'longitude': -67.0890056, 'url': 'http://www.dnsodontologica.com.br', 'desc': None, 'phone': '+559734712066', 'image': None, 'source': 'https://maps.apple.com/place?q=DNS%20Odontomedica&auid=9296844468385454246&address=Rua%20Alfredo%20Mac%C3%AAdo,%20102,%20S%C3%A3o%20Gabriel%20da%20Cachoeira%20-%20AM,%2069750-000,%20Brazil&ll=-0.1242364,-67.0890056', 'links': None, 'hours': ''},

...
]
```
***Example 4. Advanced search by coordinates with increasing search square***
```python
from vm_ddgsearch import ddg_maps

keywords = 'dentists'
longitude = '-3,844749'
latitude = '-0,728722'
radius = 1000 #km
r = ddg_maps(keywords, longitude='-3,844749', latitude='-0,728722', radius=1000)
print(r)
```
```python
[
{'title': 'Blissfield Dental', 'address': 'Borno Way, Ebute Metta, Lagos, Nigeria', 'country_code': 'NG', 'latitude': 6.49685370846362, 'longitude': 3.37770581245422, 'url': '', 'desc': None, 'phone': '+2348023134407', 'image': None, 'source': 'https://maps.apple.com/place?q=Blissfield%20Dental&auid=14057124693413493763&address=Borno%20Way,%20Ebute%20Metta,%20Lagos,%20Nigeria&ll=6.496853708463621,3.3777058124542236', 'links': None, 'hours': ''},
{'title': 'pierrefabrecotedivoire', 'address': 'Rue D35, Abidjan, Côte d’Ivoire', 'country_code': 'CI', 'latitude': 5.33444294059565, 'longitude': -3.97692739963531, 'url': 'https://www.instagram.com/pierrefabrecotedivoire/', 'desc': 'Welcome back to Instagram. Sign in to check out what your friends, family & interests have been capturing & sharing around the world.', 'phone': '', 'image': 'https://www.instagram.com/static/images/ico/apple-touch-icon-180x180-precomposed.png/c06fdb2357bd.png', 'source': 'https://maps.apple.com/place?q=pierrefabrecotedivoire&auid=11515715525840432861&address=Rue%20D35,%20Abidjan,%20C%C3%B4te%20d%E2%80%99Ivoire&ll=5.334442940595645,-3.976927399635315', 'links': '', 'hours': ''},
...
]
```
___
## 5. ddg_translate() - translation by duckduckgo.com

```python
from vm_ddgsearch import ddg_translate

def ddg_translate(keywords, from_=None, to='en'):
    ''' DuckDuckGo translate
    keywords: string or a list of strings to translate;  
    from_: what language to translate from (defaults automatically),
    to: what language to translate (defaults to English). 
    '''
```
***Returns***
```python
[
{'detected_language': detected_language,
  'translated': translated text,
  'original': original text,},
 ...
 ]
```
***Example 1. Translate the string***
```python
from vm_ddgsearch import ddg_translate

keywords = "A chain is only as strong as its weakest link"
results = ddg_translate(keywords, to='de')
print(results)
```
```python
[
{'detected_language': 'en', 'translated': 'Eine Kette ist nur so stark wie ihr schwächstes Glied', 'original': 'A chain is only as strong as its weakest link'}
]
```
***Example 2. Translate the list of strings***
```python
from vm_ddgsearch import ddg_translate

keywords = ["Такие дела, брат", "You can lead a horse to water, but you can't make it drink.",
            "Ein Spatz in der Hand ist besser, als eine Taube auf dem Dach."]
results = ddg_translate(keywords, from_=None, to='tr')
print(results)
```
```python
[
{'detected_language': 'ru', 'translated': 'Böyle şeyler, kardeşim.', 'original': 'Такие дела, брат'},
{'detected_language': 'en', 'translated': 'Bir atı suya götürebilirsin ama içiremezsin.', 'original': "You can lead a horse to water, but you can't make it drink."},
{'detected_language': 'de', 'translated': 'Elinizdeki serçe çatıdaki bir güvercinden daha iyidir.', 'original': 'Ein Spatz in der Hand ist besser, als eine Taube auf dem Dach.'},
...
]
```

