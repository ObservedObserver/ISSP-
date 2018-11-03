DROP DATABASE IF EXISTS ISSP;
CREATE DATABASE ISSP CHARACTER SET utf8 COLLATE utf8_general_ci;;
USE ISSP;
-- 分类,序号,证券代码,证券简称,公司中文名称,注册地址,办公地址,邮编,公司电话,公司网站
CREATE TABLE categories (
  category VARCHAR(255) NOT NULL,
  categoryName VARCHAR(255),
  PRIMARY KEY (category)
);

CREATE TABLE companies (
  companyID INT NOT NULL,
  category VARCHAR(255),
  companyCode VARCHAR(255),
  companyName VARCHAR(255) NOT NULL,
  companyFullName VARCHAR(255),
  companyLocReg VARCHAR(255),
  companyLocReal VARCHAR(255),
  zipCode VARCHAR(255),
  companyPhone VARCHAR(255),
  companyWebsite VARCHAR(255),
  PRIMARY KEY (companyName),
  FOREIGN KEY (category) REFERENCES categories(category)
);

CREATE TABLE safetyEvents (
  title VARCHAR(255) NOT NULL,
  time DATE,
  companyName VARCHAR(255),
  articleURL VARCHAR(255),
  abstract TEXT,
  INDEX titleIndex (title),
  FOREIGN KEY (companyName) REFERENCES companies(companyName)
);
-- 日期,开盘,最高,最低,收盘,成交量,成交金额,升跌$,升跌%,company_name
CREATE TABLE stockMarket (
  companyName VARCHAR(255) NOT NULL,
  time DATE NOT NULL,
  startPrice DOUBLE,
  maxPrice DOUBLE,
  minPrice DOUBLE,
  endPrice DOUBLE,
  amount DOUBLE,
  cash DOUBLE,
  changeInCash DOUBLE,
  changeInPercent DOUBLE,
  PRIMARY KEY (companyName, time),
  FOREIGN KEY (companyName) REFERENCES companies(companyName)
);

CREATE TABLE companyKPI (
  companyName VARCHAR(255) NOT NULL,
  delta INT NOT NULL,
  relationScore DOUBLE,
  stockScore DOUBLE,
  PRIMARY KEY (companyName, delta),
  FOREIGN KEY (companyName) REFERENCES companies(companyName)
);

INSERT INTO categories (category, categoryName) VALUES 
('1', '科技'), ('2', '金融'), ('3', '其他');