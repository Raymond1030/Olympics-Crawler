<div align="center">
  <h1>Olympics Crawler ◯‍◯‍◯‍◯‍◯</h1>     
  <p align="center">
    🤗<a href="README.md">English</a> • 
    🤗 <a href="README-CN.md">中文</a> • 
  </p>
</div>


本项目用于从[奥林匹克官网](https://olympics.com)爬取历届奥运会的基本信息、比赛项目及详细比赛结果数据，支持中英文双语数据抓取。


---

## 文件说明

1. **GetOlympics_Name_Year.py**  
   - 功能：从预定义的URL列表中提取奥运会名称和年份，生成`olympic_games.csv`。
   - 输出文件：`Olympics_event/olympic_games.csv`

2. **GetSport.py**  
   - 功能：使用Selenium爬取每届奥运会的比赛项目列表，保存为`[奥运会名称]_events.csv`。
   - 输出文件：`Olympics_event/[奥运会名称]_events.csv`

3. **GetOlympics.py**  
   - 功能：根据比赛项目列表，爬取每项比赛的详细结果（包括奖牌、运动员、国家信息），支持中英文数据。
   - 输出目录：`Olympics-result-zh/`（中文）和`Olympics-result-en/`（英文）

---

## 依赖项

- Python 3.8+
- 必要库：
  ```bash
  pip install pandas beautifulsoup4 requests selenium openpyxl tqdm

- 浏览器驱动：[Microsoft Edge Driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
  （需与Edge浏览器版本匹配，驱动路径需在系统环境变量中）

  

  
## 使用步骤

### 1. 生成奥运会列表

运行脚本生成奥运会基本信息：

```
python GetOlympics_Name_Year.py
```

### 2. 获取每届奥运会的比赛项目

  运行脚本爬取比赛项目列表：

  ```
  python GetSport.py
  ```

  **注意**：首次运行需登录浏览器并手动接受Cookie，后续会自动加载用户配置文件。

  ### 3. 爬取比赛结果数据

  - 中文数据：

    ```
python GetOlympics.py
    ```

  - 英文数据（需取消`main_en()`注释）：

    ```
    # 在GetOlympics.py中取消注释：
    # main_en()
    python GetOlympics.py
    ```
    
## 注意事项


1. **Selenium配置**

   - 确保已安装Edge浏览器并下载匹配版本的EdgeDriver。

   - 如需修改浏览器配置文件路径，请更新`GetSport.py`中的配置：

```
     options.add_argument("user-data-dir=/Your/Profile/Path")
```

2. **网络稳定性**
   部分页面加载较慢，建议在低网络延迟环境下运行。

3. **反爬机制**
   若频繁触发反爬，可调整`GetSport.py`中的滚动次数和等待时间：

   ```
   scroll_pause_time = 2   # 滚动后等待时间（秒）
   total_scrolls = 5       # 滚动次数
   ```

---

## 目录结构

```
├── Olympics_event/                # 奥运会列表和比赛项目
│   ├── olympic_games.csv          # 所有奥运会名称及年份
│   └── [奥运会名称]_events.csv     # 单届奥运会的比赛项目
│
├── Olympics-result-zh/            # 中文比赛结果（按奥运会分目录）
│   └── [奥运会名称]/
│       └── [项目名称].xlsx
│
├── Olympics-result-en/            # 英文比赛结果（同上）
│
├── GetOlympics_Name_Year.py       # 脚本1
├── GetSport.py                    # 脚本2
└── GetOlympics.py                 # 脚本3
```

------

### 比赛结果Excel文件

| Sport    | Event      | Medal | Athlete Link  | Athlete Name | NOC  | Country       |
| :------- | :--------- | :---- | :------------ | :----------- | :--- | :------------ |
| Swimming | Men's 100m | Gold  | /athletes/... | John Smith   | USA  | United States |

## 许可证

Apache License