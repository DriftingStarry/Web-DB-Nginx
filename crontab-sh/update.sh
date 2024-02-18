#!/bin/bash
rclone rclone copyto ../compose/MariaDb/data/hddata/news.csv aly-oss:hd-news-data/news.csv
