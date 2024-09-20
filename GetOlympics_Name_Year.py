import re
import pandas as pd

# 示例数据
item_list = [
#     {  "@type":"ListItem",
# "position": 1,
# "url": "https://www.olympics.com/olympic-games/salt-lake-city-utah-2034"
# }, {
#     "@type": "ListItem",
#     "position": 2,
#     "url": "https://www.olympics.com/olympic-games/brisbane-2032"
# }, {
#     "@type": "ListItem",
#     "position": 3,
#     "url": "https://www.olympics.com/olympic-games/french-alps-2030"
# }, {
#     "@type": "ListItem",
#     "position": 4,
#     "url": "https://www.olympics.com/olympic-games/los-angeles-2028"
# }, {
#     "@type": "ListItem",
#     "position": 5,
#     "url": "https://www.olympics.com/olympic-games/milano-cortina-2026"
# },
    {
    "@type": "ListItem",
    "position": 6,
    "url": "https://www.olympics.com/olympic-games/beijing-2022"
}, {
    "@type": "ListItem",
    "position": 7,
    "url": "https://www.olympics.com/olympic-games/tokyo-2020"
}, {
    "@type": "ListItem",
    "position": 8,
    "url": "https://www.olympics.com/olympic-games/pyeongchang-2018"
}, {
    "@type": "ListItem",
    "position": 9,
    "url": "https://www.olympics.com/olympic-games/rio-2016"
}, {
    "@type": "ListItem",
    "position": 10,
    "url": "https://www.olympics.com/olympic-games/sochi-2014"
}, {
    "@type": "ListItem",
    "position": 11,
    "url": "https://www.olympics.com/olympic-games/london-2012"
}, {
    "@type": "ListItem",
    "position": 12,
    "url": "https://www.olympics.com/olympic-games/vancouver-2010"
}, {
    "@type": "ListItem",
    "position": 13,
    "url": "https://www.olympics.com/olympic-games/beijing-2008"
}, {
    "@type": "ListItem",
    "position": 14,
    "url": "https://www.olympics.com/olympic-games/turin-2006"
}, {
    "@type": "ListItem",
    "position": 15,
    "url": "https://www.olympics.com/olympic-games/athens-2004"
}, {
    "@type": "ListItem",
    "position": 16,
    "url": "https://www.olympics.com/olympic-games/salt-lake-city-2002"
}, {
    "@type": "ListItem",
    "position": 17,
    "url": "https://www.olympics.com/olympic-games/sydney-2000"
}, {
    "@type": "ListItem",
    "position": 18,
    "url": "https://www.olympics.com/olympic-games/nagano-1998"
}, {
    "@type": "ListItem",
    "position": 19,
    "url": "https://www.olympics.com/olympic-games/atlanta-1996"
}, {
    "@type": "ListItem",
    "position": 20,
    "url": "https://www.olympics.com/olympic-games/lillehammer-1994"
}, {
    "@type": "ListItem",
    "position": 21,
    "url": "https://www.olympics.com/olympic-games/barcelona-1992"
}, {
    "@type": "ListItem",
    "position": 22,
    "url": "https://www.olympics.com/olympic-games/albertville-1992"
}, {
    "@type": "ListItem",
    "position": 23,
    "url": "https://www.olympics.com/olympic-games/seoul-1988"
}, {
    "@type": "ListItem",
    "position": 24,
    "url": "https://www.olympics.com/olympic-games/calgary-1988"
}, {
    "@type": "ListItem",
    "position": 25,
    "url": "https://www.olympics.com/olympic-games/los-angeles-1984"
}, {
    "@type": "ListItem",
    "position": 26,
    "url": "https://www.olympics.com/olympic-games/sarajevo-1984"
}, {
    "@type": "ListItem",
    "position": 27,
    "url": "https://www.olympics.com/olympic-games/moscow-1980"
}, {
    "@type": "ListItem",
    "position": 28,
    "url": "https://www.olympics.com/olympic-games/lake-placid-1980"
}, {
    "@type": "ListItem",
    "position": 29,
    "url": "https://www.olympics.com/olympic-games/montreal-1976"
}, {
    "@type": "ListItem",
    "position": 30,
    "url": "https://www.olympics.com/olympic-games/innsbruck-1976"
}, {
    "@type": "ListItem",
    "position": 31,
    "url": "https://www.olympics.com/olympic-games/munich-1972"
}, {
    "@type": "ListItem",
    "position": 32,
    "url": "https://www.olympics.com/olympic-games/sapporo-1972"
}, {
    "@type": "ListItem",
    "position": 33,
    "url": "https://www.olympics.com/olympic-games/mexico-city-1968"
}, {
    "@type": "ListItem",
    "position": 34,
    "url": "https://www.olympics.com/olympic-games/grenoble-1968"
}, {
    "@type": "ListItem",
    "position": 35,
    "url": "https://www.olympics.com/olympic-games/tokyo-1964"
}, {
    "@type": "ListItem",
    "position": 36,
    "url": "https://www.olympics.com/olympic-games/innsbruck-1964"
}, {
    "@type": "ListItem",
    "position": 37,
    "url": "https://www.olympics.com/olympic-games/rome-1960"
}, {
    "@type": "ListItem",
    "position": 38,
    "url": "https://www.olympics.com/olympic-games/squaw-valley-1960"
}, {
    "@type": "ListItem",
    "position": 39,
    "url": "https://www.olympics.com/olympic-games/melbourne-1956"
}, {
    "@type": "ListItem",
    "position": 40,
    "url": "https://www.olympics.com/olympic-games/cortina-d-ampezzo-1956"
}, {
    "@type": "ListItem",
    "position": 41,
    "url": "https://www.olympics.com/olympic-games/helsinki-1952"
}, {
    "@type": "ListItem",
    "position": 42,
    "url": "https://www.olympics.com/olympic-games/oslo-1952"
}, {
    "@type": "ListItem",
    "position": 43,
    "url": "https://www.olympics.com/olympic-games/london-1948"
}, {
    "@type": "ListItem",
    "position": 44,
    "url": "https://www.olympics.com/olympic-games/st-moritz-1948"
}, {
    "@type": "ListItem",
    "position": 45,
    "url": "https://www.olympics.com/olympic-games/berlin-1936"
}, {
    "@type": "ListItem",
    "position": 46,
    "url": "https://www.olympics.com/olympic-games/garmisch-partenkirchen-1936"
}, {
    "@type": "ListItem",
    "position": 47,
    "url": "https://www.olympics.com/olympic-games/los-angeles-1932"
}, {
    "@type": "ListItem",
    "position": 48,
    "url": "https://www.olympics.com/olympic-games/lake-placid-1932"
}, {
    "@type": "ListItem",
    "position": 49,
    "url": "https://www.olympics.com/olympic-games/amsterdam-1928"
}, {
    "@type": "ListItem",
    "position": 50,
    "url": "https://www.olympics.com/olympic-games/st-moritz-1928"
}, {
    "@type": "ListItem",
    "position": 51,
    "url": "https://www.olympics.com/olympic-games/paris-1924"
}, {
    "@type": "ListItem",
    "position": 52,
    "url": "https://www.olympics.com/olympic-games/chamonix-1924"
}, {
    "@type": "ListItem",
    "position": 53,
    "url": "https://www.olympics.com/olympic-games/antwerp-1920"
}, {
    "@type": "ListItem",
    "position": 54,
    "url": "https://www.olympics.com/olympic-games/stockholm-1912"
}, {
    "@type": "ListItem",
    "position": 55,
    "url": "https://www.olympics.com/olympic-games/london-1908"
}, {
    "@type": "ListItem",
    "position": 56,
    "url": "https://www.olympics.com/olympic-games/st-louis-1904"
}, {
    "@type": "ListItem",
    "position": 57,
    "url": "https://www.olympics.com/olympic-games/paris-1900"
}, {
    "@type": "ListItem",
    "position": 58,
    "url": "https://www.olympics.com/olympic-games/athens-1896"
}
]

# 提取奥运会名称和年份的正则表达式
pattern = re.compile(r'/olympic-games/([^/]+)$')

# 用于存储结果的列表
olympic_games = []

# 提取数据
for item in item_list:
    match = pattern.search(item["url"])
    if match:
        olympic_games.append({"Olympic Game": match.group(1)})

# 将结果转换为DataFrame
df = pd.DataFrame(olympic_games)

# 保存为CSV文件
output_file = "Olympics_event/olympic_games.csv"
df.to_csv(output_file, index=False)

print(f"数据已保存到 {output_file}")