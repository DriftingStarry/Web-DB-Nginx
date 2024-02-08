#!/bin/bash
rclone copy ../MariaDb/data/hddata/news.csv aly-oss:hd-news-data
rclone sync ../MariaDb/data/hddata/news.csv aly-oss:hd-news-data
