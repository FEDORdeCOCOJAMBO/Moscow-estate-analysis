import pandas as pd
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib

#изменение шрифта
matplotlib.rcParams['font.family'] = 'sans-serif'  
matplotlib.rcParams['font.size'] = 12  
matplotlib.rcParams['axes.labelsize'] = 12  
matplotlib.rcParams['axes.titlesize'] = 14 
matplotlib.rcParams['xtick.labelsize'] = 10 
matplotlib.rcParams['ytick.labelsize'] = 10  

##добавление линий метро
redl = [
    "Коммунарка", "Ольховая", "Прокшино", "Филатов Луг", "Саларьево",
    "Румянцево", "Тропарёво", "Юго-Западная", "Проспект Вернадского",
    "Университет", "Воробьёвы горы", "Воробьевы горы", "Спортивная", "Фрунзенская",
    "Кропоткинская", "Библиотека им. Ленина", "Библиотека и Ленина",
    "Охотный ряд", "Лубянка", "Чистые пруды", "Красносельская",
    "Сокольники", "Преображенская площадь", "Черкизовская", "Бульвар Рокоссовского", "Красные ворота", "Красные Ворота"
]
greenl = [
    "Алма-Атинская", "Красногвардейская", "Домодедовская", "Орехово",
    "Царицыно", "Кантемировская", "Каширская", "Коломенская",
    "Технопарк", "Автозаводская", "ЗИЛ",  "Новокузнецкая",
    "Театральная", "Тверская", "Маяковская", 
    "Динамо", "Аэропорт", "Сокол", "Войковская", "Водный Стадион", "Водный стадион"
    "Речной вокзал", "Ховрино", "Беломорская"
]
bluel = [
    "Щёлковская", "Первомайская", "Измайловская", "Партизанская",
    "Семёновская", "Электрозаводская", "Бауманская", 
    "Площадь Революции", "Арбатская", "Смоленская", 
    "Парк Победы", "Славянский бульвар", "Кунцевская", "Молодёжная",
    "Крылатское", "Строгино", "Мякинино", "Волоколамская", "Митино",
    "Пятницкое шоссе"
]
lightbluel = [
    "Кунцевская", "Пионерская", "Филёвский парк", "Багратионовская",
    "Фили", "Кутузовская", "Студенческая", 
    "Смоленская", "Арбатская", "Александровский сад"
]
brownl = [
    "Киевская", "Краснопресненская", "Белорусская", "Новослободская",
    "Проспект Мира", "Комсомольская", "Курская", "Таганская",
    "Павелецкая", "Добрынинская", "Октябрьская", "Парк культуры", "Парк Культуры"
]
orangel = [
    "Новоясеневская", "Ясенево", "Тёплый Стан","Тёплый стан", "Теплый стан", "Теплый Стан", "Коньково", "Беляево",
    "Калужская", "Новые Черёмушки", "Профсоюзная", "Академическая",
    "Ленинский проспект", "Шаболовская",  "Третьяковская",
    "Китай-город", "Тургеневская", "Сухаревская", "Новые черемушки", "Новые черёмушки", "Новые Черемушки"
    "Рижская", "Алексеевская", "ВДНХ", "Ботанический Сад", "Ботанический сад", "Свиблово",
    "Бабушкинская", "Медведково"
]
violetl = [
    "Планерная", "Сходненская", "Тушинская", "Спартак", "Щукинская",
    "Октябрьское поле", "Полежаевская", "Беговая", "Улица 1905 года",
    "Баррикадная", "Пушкинская", "Кузнецкий мост", "Китай-город",
     "Пролетарская", "Волгоградский проспект", "Текстильщики",
    "Кузьминки", "Рязанский Проспект", "Выхино", "Лермонтовский Проспект",
    "Жулебино", "Котельники"
]
saladl = [
    "Селигерская", "Верхние Лихоборы", "Окружная", "Петровско-Разумовская",
    "Фонвизинская", "Бутырская", "Марьина роща", "Достоевская",
    "Трубная", "Сретенский бульвар", "Чкаловская", "Римская",
    "Крестьянская застава", "Дубровка", "Кожуховская", "Печатники",
    "Волжская", "Люблино", "Братиславская", "Марьино",
    "Борисово", "Шипиловская", "Зябликово"
]
bkll = ["Савёловская","Петровский парк", "Петровский Парк",
        "ЦСКА","Хорошёвская","Народное Ополчение","Мнёвники","Терехово","Кунцевская","Давыдково","Аминьевская","Мичуринский Проспект","Проспект Вернадского","Новаторская","Воронцовская","Зюзино","Каховская","Варшавская","Каширская","Кленовый Бульвар","Нагатинский Затон","Печатники","Текстильщики","Нижегородская","Авиамоторная","Лефортово","Электрозаводская","Сокольники","Рижская","Марьина Роща"]
purplel = [
    "Некрасовка", "Лухмановская", "Улица Дмитриевского", "Косино",
    "Юго-Восточная", "Окская", "Стахановская", "Нижегородская"
]
yellowl = [
    "Новокосино", "Новогиреево", "Перово", "Шоссе Энтузиастов",
    "Авиамоторная", "Площадь Ильича", "Марксистская", "Третьяковская"
]
greyl = [
    "Бульвар Дмитрия Донского", "Аннино", "Улица Академика Янгеля", 
    "Пражская", "Южная", "Чертановская", "Севастопольская", 
    "Нахимовский проспект", "Нагорная", "Нагатинская", "Тульская", 
    "Серпуховская", "Полянка", "Боровицкая", "Чеховская", 
    "Цветной бульвар", "Менделеевская", "Савёловская", "Дмитровская", 
    "Тимирязевская", "Петровско-Разумовская", "Владыкино", 
    "Отрадное", "Бибирево", "Алтуфьево", "Трубная"
]
lightgreyl = [
    "Бульвар Дмитрия Донского", "Улица Старокачаловская", 
    "Лесопарковая", "Битцевский парк", "Новоясеневская", "Бутово", "Улица Скобелевская", "Улица Горчакова", "Бунинская аллея", "Улица Адмирала Ушакова"
]
mccl = ['Окружная',
'Владыкино',
'Ботанический Сад', 'Ботанический сад',
'Ростокино',
'Белокаменная',
'Бульвар Рокоссовского',
'Локомотив',
'Измайлово',
'Соколиная Гора',
'Шоссе Энтузиастов',
'Андроновка ',
'Нижегородская',
'Новохохловская',
'Угрешская',
'Дубровка',
'Автозаводская',
'ЗИЛ',
'Верхние Котлы', 'Верхние котлы',
'Крымская',
'Площадь Гагарина',
'Лужники',
'Кутузовская',
'Москва-Сити',
'Шелепиха',
'Хорошёво',
'Зорге',
'Панфиловская',
'Стрешнево',
'Балтийская',
'Коптево',
'Лихоборы']
lisofstations = []
colors1 = []
def colors(station):
    if station[0]==' ':
        station = station[1:]
    if station in redl:
        colors1.append('red')
    elif station in greenl:
        colors1.append('green')
    elif station in bluel:
        colors1.append('#3271C0')
    elif station in lightbluel:
        colors1.append('#59B9EE')
    elif station in brownl:
        colors1.append('#96593F')
    elif station in orangel:
        colors1.append('#ED9121')
    elif station in violetl:
        colors1.append('#8B3C8E')
    elif station in yellowl:
        colors1.append('#F4D048')
    elif station in greyl:
        colors1.append('#AFADAE')
    elif station in saladl:
        colors1.append('#BECE4E')
    elif station in bkll:
        colors1.append('#8DB4AF')
    elif station in lightgreyl:
        colors1.append('Lightgrey')
    elif station in purplel:
        colors1.append('fuchsia')
    elif station in mccl:
        colors1.append('#E56D96')
    else:
        colors1.append('black')
    return station
def lines(colors):
    if colors == 'red':
        lisofstations.append(1)
    elif colors == 'green':
        lisofstations.append(2)
    elif colors == '#3271C0':
        lisofstations.append(3)
    elif colors == '#59B9EE':
        lisofstations.append(4)
    elif colors == '#96593F':
        lisofstations.append(5)
    elif colors == '#E3873F':
        lisofstations.append(6)
    elif colors == '#8B3C8E':
        lisofstations.append(7)
    elif colors == '#F4D048':
        lisofstations.append(8)
    elif colors == '#AFADAE':
        lisofstations.append(9)
    elif colors == '#BECE4E':
        lisofstations.append(10)
    elif colors == '#8DB4AF':
        lisofstations.append(11)
    elif colors == 'Lightgrey':
        lisofstations.append(12)
    elif colors == '#E56D96':
        lisofstations.append(14)
    elif colors == 'fuchsia':
        lisofstations.append(15)
    else:
        lisofstations.append('others')
    return colors
line_names = {
    1:"Сокольническая линия",        # 1 (красная)
    2:"Замоскворецкая линия",        # 2 (зеленая)
    3:"Арбатско-Покровская линия",   # 3 (синяя)
    4:"Филёвская линия",             # 4 (голубая)
    5:"Кольцевая линия",             # 5 (коричневая)
    6:"Калужско-Рижская линия",      # 6 (оранжевая)
    7:"Таганско-Краснопресненская линия", # 7 (фиолетовая)
    8:"Калининская линия",           # 8 (жёлтая)
    9:"Серпуховско-Тимирязевская линия", # 9 (серая)
    10:"Люблинско-Дмитровская линия", # 10 (салатовая)
    11:"Большая кольцевая линия",     # 11 (бирюзовая)
    12:"Бутовская линия",             # 12 (светло-серая)
    13:"Московское центральное кольцо (МЦК)", # 13
    14:"Некрасовская линия",          # 14 (розовая)
    15:"МЦД", # 15
    'others':"Станции, не входящие в систему метро" 
}

##обработка данных
df = pd.read_csv('/Users/fedorkirsanov/Desktop/Data Science/data.csv')
df['Number of rooms'] = df['Number of rooms'].apply(int)
df['Number of floors'] = df['Number of floors'].apply(int)
df['Minutes to metro'] = df['Minutes to metro'].apply(int)
df['Floor'] = df['Floor'].apply(int)
df = df[df['Number of rooms']>0]
def mil(price):
    price = round(price/1000000, 3)
    return price
df['Price']=df['Price'].apply(mil)
##df.plot(x = 'Price', y = 'Area', kind = 'scatter')
##plt.show()
df = df.assign(PtoA = round(df['Price']/df['Area']*1000, 3))
a = df.groupby(by = 'Metro station')['PtoA'].mean()
a = pd.DataFrame(a)
a = a.reset_index()
a.columns = ['Metro station', 'PtoA']
a = a.sort_values('PtoA')
a['Metro station'] = a['Metro station'].apply(colors)
a1 = a.head()
a2 = a.tail()
a = pd.concat([a1, a2])
colors1 = []
a['Metro station'] = a['Metro station'].apply(colors)
colors_a = colors1
##fix, ax = plt.subplots()
##ax.barh(a['Metro station'], a['PtoA'], color = colors1)
##plt.show()

lisofstations = []
color1 = []

c = df.groupby(by = 'Minutes to metro')['PtoA'].mean()
c = pd.DataFrame(c)
c = c.reset_index()
c.columns = ['Minutes to metro', 'Price/Area']
c = c.sort_values('Minutes to metro')
##c.plot(x = 'Minutes to metro', y = 'Price/Area', kind = 'bar')
##plt.show()


d = df.groupby(by = 'Floor')['PtoA'].mean()
d = pd.DataFrame(d)
d = d.reset_index()
d.columns = ['Floor', 'Price/Area']
d = d.sort_values('Floor')
##d.plot(x = 'Floor', y = 'Price/Area', kind = 'bar', color = 'green')
##plt.show()

e = df.groupby(by = 'Renovation')['PtoA'].mean()
e = pd.DataFrame(e)
e = e.reset_index()
e.columns = ['Renovation', 'Price/Area']
e = e.sort_values('Renovation')
##e.plot(x = 'Renovation', y = 'Price/Area', kind = 'bar', color = 'orange')
##plt.show()

f = df[['Apartment type', 'Price', 'Area']]
apart = []
def aparts(typ):
    if typ == 'Secondary':
        apart.append('green')
    else:
        apart.append('deepskyblue')
    return typ
f = f[f['Price']<500]
f = f[f['Area']<600]
f['Apartment type'] = f['Apartment type'].apply(aparts)
fx = 10*(f['Price'].mean())
fy = 10*(f['Area'].mean())
##f.plot(title = 'Area/price ratio', x = 'Price', xlabel = 'Price \n (10000₽)', y = 'Area', ylabel = 'Area \n (m²)', kind = 'scatter', color = apart)
##plt.plot([0, fx], [0,fy], lw = '1', c = 'red')
##legend_elements = [Line2D([0],[0], marker = 'o', color = 'w', markerfacecolor = 'deepskyblue', markersize = 10, label = 'New building'), Line2D([0],[0], marker = 'o', color = 'w', markerfacecolor = 'green', markersize = 10, label = 'Secondary'), Line2D([0],[0], color = 'red', lw = 4, label = 'Mean')]
##plt.legend(handles = legend_elements, loc = 'upper left')
##plt.show()

g = df.groupby(by = 'Number of rooms')['PtoA'].mean()
##g.plot(kind = 'bar')
##plt.show()
amount = df['Metro station'].value_counts()
amount = amount.nlargest(n=10).reset_index()
lisofstations = []
amount = amount.sort_values('count')
amount['Metro station'] = amount['Metro station'].apply(colors)
##amount.plot(x = 'Metro station', y = 'count', color = colors1, kind = 'barh')
##plt.show()


lisofstations = []
colors1 = []
df['Metro station'] = df['Metro station'].apply(colors)
dfl = df.assign(Color = colors1)
dfl['Color'] = dfl['Color'].apply(lines)
listofnames = [line_names[i] for i in lisofstations]
dfl = dfl.assign(Line = listofnames)
lisofstations = []
colors1 = []
dfl1 = dfl.groupby(by = ['Line', 'Color'])['PtoA'].mean()
dfl1 = pd.DataFrame(dfl1)
dfl1 = dfl1.sort_values(by='PtoA', ascending=True)
dfl1 = dfl1.reset_index()
dfl1.columns = ['Line', 'Color', 'PtoA']
cols = dfl1['Color'].to_list()
#dfl1.plot(x = 'Line', y = 'PtoA', xlabel = 'Price per m²', ylabel = 'Metro line', kind = 'barh', color = cols, legend = False)
#plt.show()

amount_of_rooms = df['Number of rooms'].value_counts()
amount_of_rooms = amount_of_rooms.sort_index()
#amount_of_rooms.plot(kind = 'bar')
#plt.show()

fig, axs = plt.subplots(3, 2, figsize=(20, 15))
fig.subplots_adjust(hspace=0.2, wspace=0.2)

# 1. Средняя цена за м² по станциям метро

axs[0, 0].barh(a['Metro station'], a['PtoA'], color=colors_a)
axs[0, 0].set_title('Цена за м² по станциям метро')

# 2. Цена/площадь от времени до метро
axs[0, 1].bar(c['Minutes to metro'], c['Price/Area'], color='blue')
axs[0, 1].set_title('Цена за м² от времени до метро')

# 3. Цена/площадь по этажу
axs[1, 0].bar(d['Floor'], d['Price/Area'], color='green')
axs[1, 0].set_title('Цена за м² по этажу')

# 4. Цена/площадь по типу ремонта
axs[1, 1].bar(e['Renovation'], e['Price/Area'], color='orange')
names = ['Косметический', 'Дизайнер', 'Евро', 'без']
axs[1,1].set_xticklabels(names)

# Добавляем заголовок
axs[1, 1].set_title('Цена за м² по типу ремонта')

# 5. Средняя цена за м² по линиям метро
y_pos = range(len(dfl1))
axs[2, 0].barh(y_pos, dfl1['PtoA'], color=cols)
axs[2, 0].set_yticks(y_pos)
axs[2, 0].set_yticklabels([f'{line}' for line in dfl1['Line']])
axs[2, 0].set_title('Цена за м² по линиям метро')

# 6. Количество квартир по числу комнат
axs[2, 1].bar(amount_of_rooms.index, amount_of_rooms.values, color='purple')
axs[2, 1].set_title('Количество квартир по числу комнат')

fig.suptitle('Метрики для датасета продающихся квартир в Москве', fontsize=20, fontweight='bold')
plt.tight_layout()
plt.savefig('/Users/fedorkirsanov/Downloads/fullsizefig.png')