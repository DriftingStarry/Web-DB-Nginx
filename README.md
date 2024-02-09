# Intro
Sends 23级作业  
使用 `docker-compose`部署`nginx` `mariadb` `python爬虫` `flask站点`   
效果可访问 https://121.199.32.74/  

# To do list
- [x] Web实时更新数据
- [x] 爬虫不重复爬取
  - [x] 数据表增加 id 主键
  - [x] 爬虫抓取htm前数字
- [ ] Nginx反代
  - [x] html页面
  - [ ] 外部静态资源
- [x] Rclone
- [ ] gitlabCI
- [ ] GitHub Actions
  - [ ] 自动测试代码
  - [x] 自动部署
- [x] crontab定时任务
