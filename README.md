# Intro  
Sends 23级作业  
使用 `docker-compose`部署`nginx` `mariadb` `python爬虫` `flask站点`    
并使用 `crontab` 进行数据备份与上传
效果可访问 https://121.199.32.74/  

# 部署  

## compose  
将项目资源下载至本地  
使用
```bash
docker compose up -d
```
一键部署在后台  

## Crontab  
使用以下命令进行编辑
```bash
crontab -e
```
键入
```crontab
*/5 * * * * [path]
```