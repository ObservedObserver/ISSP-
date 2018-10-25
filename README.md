# ISSP-Web-Crawler
(BJTU-ISSP-2018课程大作业) 研究国内信息安全事件对不同公司的影响。本项目包含数据爬取与分析两部分主要功能。
## Project Structure
+ analysis
+ baidu
+ dataset
+ stockHistory
+ toutiao

## 流程说明

### 获取信息安全攻击数据
+ `baidu/index.py`
+ `toutiao/index.py`

### 数据关系构建
1. 数据获取: `/dataset/bj_safe_baiduall.json`获取时间数据， `/dataset/stock.csv`获取股市数据。
2. 数据格式化: `/analysis/relation/buildRelation.py`既可以进行相关度计算也可以格式化数据
3. 计算权值: 由于python的运行效率较低，我们对于分析算法使用node运行`faster_buildRelation.js`来完成。