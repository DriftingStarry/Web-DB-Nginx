#!/bin/bash
rclone copy ../compose/MariaDb/data/hddata/news.csv aly-oss:hd-news-data
rclone sync ../compose/MariaDb/data/hddata/news.csv aly-oss:hd-news-data
